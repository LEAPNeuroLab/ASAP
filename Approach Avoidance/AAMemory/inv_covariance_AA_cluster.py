import nibabel as nib
import os
import numpy as np
import os.path as op
import scipy
import pandas as pd
import scipy.stats
import sys

def compute_inv_shrunk_covariance(x):
	#see http://www.diedrichsenlab.org/pubs/Walther_Neuroimage_2016.pdf
	t,n = x.shape #t measurements by n voxels

	#demean
	x = x - x.mean(0)

	#compute covariance
	sample = (1.0/t) * np.dot(np.transpose(x),x)

	#copute prior
	prior = np.diag(np.diag(sample))

	#deal with occasional empty voxel by avoiding singularity
	for i in range(prior.shape[0]):
		if prior[i,i] < 1e-6:
			prior[i,i] = 1e-6
			
	#compute shrinkage
	d = 1.0/n * np.linalg.norm(sample - prior,ord = 'fro')**2
	y = np.square(x)
	r2 = 1.0/n/t**2 * np.sum(np.sum(np.dot(np.transpose(y),y)))- \
	1.0/n/t*np.sum(np.sum(np.square(sample)))

	#compute the estimator
	shrinkage = max(0,min(1,r2/d))
	sigma = shrinkage*prior + (1-shrinkage)*sample

	#compute the inverse
	try:
		inv_sigma = np.linalg.inv(sigma)
	except:
		inv_sigma = np.linalg.inv(prior) #univariate
	return inv_sigma

# choose one run; do this just once per subject.
def compute_inverse_sigma(sub,run,m,voxlist):

	mask_f = os.path.join('YourMainFolder/ASAP/AA_fMRI/process/results/' + sub + '/finalmasks/', m + '_anat_resampled_final.nii.gz')
	resid_dir = 'YourMainFolder/ASAP/AA_fMRI/process/results/'+ sub + "/run" + str(run) + '/' + sub + '_run' + str(run) + '_GLM_noTD_ST_MVPA_extended_allTrials.feat/MVPA/' #todo change

	resid = resid_dir + 'res4d_anat.nii.gz'
	res = nib.load(resid).get_fdata()
# 	mask = nib.load(mask_f).get_data().astype(bool) # orig
 
# prob masks threshold according to the mask
	mask_temp = nib.load(mask_f).get_fdata()
	if "FS" in m:
		mask_thres = mask_temp >= .05  # relevant for Free Surfer PFC probabilistic maps
	elif "AMY" in m:
		mask_thres = mask_temp >= 0.25  # relevant for Tyzka AMY subnuclei probabilistic maps
	elif "Amy" in m or 'harvardoxford' in m:
		mask_thres = mask_temp >= 0.7  # relevant for harvard-oxford probabilistic maps
	else:
		mask_thres = mask_temp >= .05  # new FS masks

	x = res[mask_thres]
	#Get number of rows of x dataframe, since the row number is voxel number
	num_rows=x.shape[0]
	# print(num_rows)
	# print(len(voxlist))
	if num_rows!=len(voxlist):
		# contain outlier
		# create a boolean mask of rows to keep
		voxoutliermask = np.isin(np.arange(x.shape[0]), voxlist)
		# filter the numpy array to remove rows with indices not in the list
		x = x[voxoutliermask]
	x = np.transpose(x)
	inv_sigma = compute_inv_shrunk_covariance(x)
	inv_sigma = scipy.linalg.fractional_matrix_power(inv_sigma,.5) #take square root

	return inv_sigma

sub='replacesub' #todo change
# beta_dir = home_dir + '/data/mri/processed/RSA/'
beta_dir="YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/" #todo change
out_dir = 'YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/prewhitenedBetas/'

# this is needed but just remove the cond in conds loop
##load betas
try:
# this is grabing the results of the extract_betas script		
	b=sub+ '_allbetas_trialwise.csv'
	allbetas = pd.read_csv(beta_dir + b)
except:
	print ('cannot read' + sub )
		
allbetas['mask']=allbetas['mask'].apply(str)
for mask in np.unique(allbetas['mask']):
	for run in np.unique(allbetas['run']):
		try:
			betas=allbetas[(allbetas['run']==run) & (allbetas['mask']==mask)] #load betas and masks
			# #parse sub, run and mask
			# # this is a silly nomenclature thing, might or might not apply
			# sub = int(np.unique(betas['sub'])[0])
			# if sub < 10:
			# 	sub = '00' + str(sub)
			# else:
			# 	sub = '0' + str(sub)
			m = mask
			betas = betas[betas['run'] == run].reset_index().sort_index() #sorts by index
			voxlist = betas['voxel'].unique()
			#compute inverse sigma
			inv_sigma = compute_inverse_sigma(sub,run,m,voxlist)

			#whiten betas
			betas = betas.set_index(['trial']).sort_index()
			for t in set(betas.index): #loop through trials
				vals = betas.loc[t,'value'].values
				whiten_vals = np.dot(inv_sigma,vals)
				betas.loc[t,'value_whiten'] = whiten_vals	#save results
			#main
# 				out_f = op.join(out_dir,'prewhitenedBetas', str(sub) + '_' + cond + '_' + mask  + '_run' + str(run) + '_allbetas_25_trialwise.csv')
			#extended
			out_f = op.join(out_dir, sub + '_' + mask  + '_run' + str(run) + '_allbetas_trialwise_extended.csv')

			# this writes all everything (all columns) that was in the oriignal file (ie extracted betas) , but now includes this "prewhitended" value, i.e. "value_whiten"
			betas = betas.reset_index().sort_values(by = ['trial','voxel']).reset_index()[['sub', 'mask', 'model', 'run', 'trial', 'voxel', 'Congruency', 'StimVal', 'Action', 'TargetVal', 'NonTargetVal', 'trialNum', 'order', 'ImgStim', 'condition', 'valmn', 'aromn', 'valsd', 'arosd', 'trialcorrect', 'RT', 'Treal_precise', 'Testimate_precise', 'Tprecise_biasabs', 'Tprecise_bias', 'Testimate_run', 'Trun_biasabs', 'Trun_bias', 'pval_PerciseChance', 'pval_RunChance', 'PercisepChanceFlag', 'PerciseBiasFlag', 'RunBias1Flag', 'RunBias2Flag', 'ReconMem', 'ConfReconMem', 'ConfCoarseMem', 'value_z', 'value','value_whiten']] #change column names to all the extra names, keep value_whiten
			betas.to_csv(out_f, index = False)
		except:
			print ("could not open " + str(sub) + ' ' + str(run) + ' ' + str(mask))
