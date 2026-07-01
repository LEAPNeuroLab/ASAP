import os

import numpy as np
import itertools
#np.set_printoptions(precision = 3)
import matplotlib.pyplot as plt
import gc
import psutil
import scipy
#get_ipython().magic('matplotlib inline')
import pandas as pd
#pd.set_option('precision',2)
import scipy.io as io
import json
import scipy.stats as stats
# import seaborn as sns
# #sns.set(color_codes=True)
# #sns.set_style('white')
import os, subprocess, sys, glob
# import nibabel as nib
# import nilearn, sklearn
# from nilearn import image,  input_data, decoding #plotting,
# import sklearn.svm
# from sklearn.pipeline import Pipeline
# #from sklearn.cross_validation import LeaveOneLabelOut, cross_val_score, permutation_test_score
# from sklearn.model_selection import LeaveOneGroupOut, cross_val_score, permutation_test_score
# from sklearn.feature_selection import SelectKBest, f_classif
# from sklearn.cross_validation import LeaveOneLabelOut

# import scipy.spatial.distance # for Euclidean

##################################################################################################################################################################################################################					
##################################################################################################################################################################################################################					
    
# maskName=str(sys.argv[1])
maskName="replacemask" #todo replacemask
# subs=['003', '004', '005', '006', '008', '009', '010', '012', '014', '017', '019', '020', '021', '022', '023', '024', '025', '026', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '069', '068', '067', '070', '071', '072', '073']
subs=['003', '004', '005', '006', '008', '009', '010', '012', '014', '017', '019', '020', '021', '022', '023', '024', '025', '026', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '069', '068', '067', '070', '071', '072', '073', '011', '015', '074', '075', '076', '077', '078', '079', '080', '082', '083']
# subs = ['005']


models=['MVPA_3mm']  # MVPA_3mm_tstat
myGLMModels=['noTD_ST'] 

runs=[1,2,3,4,5,6,7,8]
# runs=[1, 2]
regtypes=['MVPA'] #

Congruency_labels = {1:'Incon', 2:'Con', 3:'error', 4:'error'}
StimVal_labels = {1:'neg', 2:'pos'}
Action_labels = {1:'approach', 2:'avoid'}
TargetVal_labels = {1:'neg', 2:'pos'}
Nontargetval_labels = {1:'neg', 2:'pos'}
trialcorrect_labels = {1:'correct', 0:'incorrect'}
condition_labels = {1:'neg_app', 2:'pos_app', 3:'neg_avoid', 4:'pos_avoid'}
PercisepChanceFlag_labels = {1: 'MemSuccess', 2:'MemFail', 3: 'MemBetween'}
PercisepBiasFlag_labels = {1: 'MemSuccess', 2:'MemFail', 3: 'MemBetween'}
RunBias1Flag_labels = {1: 'MemSuccess', 2:'MemFail', 3: 'MemBetween'}
RunBias2Flag_labels = {1: 'MemSuccess', 2:'MemFail', 3: 'MemBetween'}

#for sub in subs:
for myGLMModel in myGLMModels:
	for model in models:
		for regtype in regtypes:
			rsa_df = {'ReconMem':[], 'ConfReconMem':[], 'ConfCoarseMem': [], 'sub':[],'model':[], 'mask':[],'run':[],'corr':[], 'corr_z':[],'trial':[], 'TR1':[], 'TR2':[], 'Congruency':[], 'StimVal':[], 'order':[],'ImgStim':[], 'trialcorrect':[],'condition':[],'valmn':[], 'aromn':[], 'RT':[],'Treal_precise':[], 'Testimate_precise': [], 'Tprecise_biasabs':[], 'Tprecise_bias':[], "Testimate_run":[], "Trun_biasabs":[], "Trun_bias":[], "pval_PerciseChance":[], "pval_RunChance":[],  "PercisepChanceFlag":[],  "PerciseBiasFlag":[],  "RunBias1Flag":[], "RunBias2Flag":[]}
			
			for sub in subs:
				print ('sub:' + sub)
				print ('maskName:' + maskName)
				# betaList = []
				try:

					# loading up whitened ones
					try:

						betas_dataframe=pd.read_csv('YourMainFolder/ASAP/AA_fMRI/process/results/TRbyTR/trialwise_matrix/'+ sub + '_TRbyTR_trialwise.csv', usecols=["ReconMem", "ConfReconMem", "ConfCoarseMem", "sub", "mask", "model","run","trial", "voxel", "Congruency", "StimVal", "trialNum", "order", "ImgStim", "trialcorrect", "condition", "valmn", "aromn", "RT", "Treal_precise", "Testimate_precise", "Tprecise_biasabs", "Tprecise_bias", "Testimate_run", "Trun_biasabs", "Trun_bias", "pval_PerciseChance", "pval_RunChance", "PercisepChanceFlag", "PerciseBiasFlag", "RunBias1Flag", "RunBias2Flag", "value_TR0", "value_TR1", "value_TR2", "value_TR3", "value_TR4", "value_TR5", "value_TR6"])

					except:
						print ("could not load dataframe for subject" + str(sub)) #some of the subjects won't have certain run due to excess motion
# 						continue

					# now compute the RSA between TRs within a trial
					TRlist= ['value_TR0', 'value_TR1', 'value_TR2', 'value_TR3', 'value_TR4', "value_TR5"]
					TR_pairs = list(itertools.combinations(TRlist, 2))

						# print (tmp_pair[0])
						# print (tmp_pair[1])
						# print (psutil.virtual_memory())
					#if run2 != run1: # tested this to see if any different; it's not
					for tmp_pair in TR_pairs:
						for trial in np.unique(betas_dataframe['trial']):
							for run in np.unique(betas_dataframe['run']):

								try:
									temp_df=betas_dataframe[(betas_dataframe['run']==run) & (betas_dataframe['trial']==trial) & (betas_dataframe['mask']==maskName)]
# 									print("current sub:" + sub)
# 									print("current run:" + str(run))
# 									print("current trial:" + str(trial))

									b1=np.asarray(temp_df[tmp_pair[0]])
									b2=np.asarray(temp_df[tmp_pair[1]])
									distance = scipy.stats.pearsonr(b1, b2)[0]  

									#Map the numeric numbers back to the strings for each condition
									Congruency=Congruency_labels[int(np.unique(temp_df['Congruency'])[0])]

									StimVal = StimVal_labels[int(np.unique(temp_df['StimVal'])[0])]


									trialcorrect = trialcorrect_labels[int(np.unique(temp_df['trialcorrect'])[0])]


									condition = condition_labels[int(np.unique(temp_df['condition'])[0])]


									PercisepChanceFlag = PercisepChanceFlag_labels[int(np.unique(temp_df['PercisepChanceFlag'])[0])]


									PerciseBiasFlag = PercisepBiasFlag_labels[
										int(np.unique(temp_df['PerciseBiasFlag'])[0])]


									RunBias1Flag = RunBias1Flag_labels[
										int(np.unique(temp_df['RunBias1Flag'])[0])]


									RunBias2Flag = RunBias2Flag_labels[
										int(np.unique(temp_df['RunBias2Flag'])[0])]


									# fill in ras_df
									rsa_df['mask'].append(maskName)
									rsa_df['sub'].append(sub)
									rsa_df['model'].append(model)
									rsa_df['run'].append(run)
									rsa_df['trial'].append(trial)
									rsa_df['corr'].append(distance)
									rsa_df['corr_z'].append(np.log(1+distance)-np.log(1-distance))
									TR1name = tmp_pair[0].replace('value_TR','')

									TR2name = tmp_pair[1].replace('value_TR', '')


									rsa_df['TR1'].append(TR1name)
									rsa_df['TR2'].append(TR2name)


									rsa_df['Congruency'].append(Congruency)


									rsa_df['StimVal'].append(StimVal)

									rsa_df['order'].append(np.unique(temp_df['order'])[0])
									rsa_df['ImgStim'].append(np.unique(temp_df['ImgStim'].astype(str))[0])

									rsa_df['condition'].append(condition)

									rsa_df['trialcorrect'].append(trialcorrect)

									rsa_df['valmn'].append(np.unique(temp_df['valmn'])[0])

									rsa_df['aromn'].append(np.unique(temp_df['aromn'])[0])

									rsa_df['RT'].append(np.unique(temp_df['RT'])[0])

									rsa_df['Treal_precise'].append(np.unique(temp_df['Treal_precise'])[0])

									rsa_df['Testimate_precise'].append(np.unique(temp_df['Testimate_precise'])[0])

									rsa_df['Tprecise_biasabs'].append(np.unique(temp_df['Tprecise_biasabs'])[0])

									rsa_df['Tprecise_bias'].append(np.unique(temp_df['Tprecise_bias'])[0])

									rsa_df['Testimate_run'].append(np.unique(temp_df['Testimate_run'])[0])

									rsa_df['Trun_biasabs'].append(np.unique(temp_df['Trun_biasabs'])[0])

									rsa_df['Trun_bias'].append(np.unique(temp_df['Trun_bias'])[0])


									rsa_df['pval_PerciseChance'].append(np.unique(temp_df['pval_PerciseChance'])[0])

									rsa_df['pval_RunChance'].append(np.unique(temp_df['pval_RunChance'])[0])

									rsa_df['PercisepChanceFlag'].append(PercisepChanceFlag)

									rsa_df['PerciseBiasFlag'].append(PerciseBiasFlag)

									rsa_df['RunBias1Flag'].append(RunBias1Flag)

									rsa_df['RunBias2Flag'].append(RunBias2Flag)

									rsa_df['ReconMem'].append(np.unique(temp_df['ReconMem'])[0])
									rsa_df['ConfReconMem'].append(np.unique(temp_df['ConfReconMem'])[0])
									rsa_df['ConfCoarseMem'].append(np.unique(temp_df['ConfCoarseMem'])[0])


								except:
									print ("failed at RSA stage " + sub+ " " + str(run))
									continue
# 						del betas_dataframe
# 						gc.collect()

				except:
					print ("could not open data run" + str(run) + str(maskName)+ "_" + sub + "_"	+ model)
					# continue


			all_rsas=pd.DataFrame(rsa_df)
			all_rsas = all_rsas.sort_values(by=['sub', 'TR1', 'TR2','mask', 'run'])
			all_rsas.to_csv('YourMainFolder/ASAP/AA_fMRI/process/results/TRbyTR/RSAbymaskNew/' +  str(maskName) + "_all_rsas_TRbyTR_trialwise_extended.csv", index=False)



