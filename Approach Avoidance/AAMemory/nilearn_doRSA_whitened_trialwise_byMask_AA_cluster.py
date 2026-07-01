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
subs=['003', '004', '005', '006', '008', '009', '010', '012', '014', '017', '019', '020', '021', '022', '023', '024', '025', '026', '029', '030', '031', '032', '033', '034', '035', '036', '037', '038', '039', '040', '041', '042', '043', '044', '045', '046', '047', '048', '049', '050', '051', '053', '054', '055', '056', '057', '058', '059', '060', '061', '062', '063', '064', '065', '066', '069', '068', '067', '070', '071', '072', '073', '011', '015', '074', '075', '076', '077', '078', '079', '080', '082', '083']
# subs = ['006']

# mayba change this later; # conds=sys.argv[2]
# outPath='/home/despoA/lapate/agng/analysis/MVPA/'

models=['MVPA_3mm']  # MVPA_3mm_tstat
myGLMModels=['noTD_ST'] 


# runs=[1,2,3,4,5,6,7,8]
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
            rsa_df = {'StimValdiff':[], 'StimValdiffabs':[], 'ReconMem1':[], 'ConfReconMem1':[], 'ConfCoarseMem1': [], 'ReconMem2':[], 'ConfReconMem2':[], 'ConfCoarseMem2': [], 'sub':[],'model':[], 'mask':[],'run':[],'corr':[], 'corr_z':[], 'DistanceIndex':[], 'trial1':[], 'trial2':[], 'triallag':[], 'crossInstr':[],'Congruency1':[], 'Congruency2':[],'StimVal1':[], 'StimVal2':[],'order':[],'ImgStim1':[],'ImgStim2':[], 'trialcorrect1':[],'trialcorrect2':[],'condition1':[],'condition2':[],'valmn1':[], 'valmn2':[], 'aromn1':[], 'aromn2':[],'RT1':[],'RT2':[],'Treal_precise1':[], 'Treal_precise2':[], 'Testimate_precise1': [], 'Testimate_precise2':[], 'Tprecise_biasabs1':[], 'Tprecise_biasabs2':[], 'Tprecise_bias1':[],'Tprecise_bias2':[], 'Testimate_run1':[], 'Testimate_run2':[], 'Trun_biasabs1':[],'Trun_biasabs2':[], 'Trun_bias1':[], 'Trun_bias2':[], 'pval_PerciseChance1':[],'pval_PerciseChance2':[], 'pval_RunChance1':[], 'pval_RunChance2':[], 'PercisepChanceFlag1':[], 'PercisepChanceFlag2':[], 'PerciseBiasFlag1':[], 'PerciseBiasFlag2':[], 'RunBias1Flag1':[],'RunBias1Flag2':[], 'RunBias2Flag1':[],'RunBias2Flag2':[],'residTprecise1':[], 'residTpreciseabs1':[], 'PreciseBiaslmFlag1':[], 'residTprecise2':[], 'residTpreciseabs2':[], 'PreciseBiaslmFlag2':[]}
            #print (sub)
            for sub in subs:
                print ('sub:' + sub)
                print ('maskName:' + maskName)
                betaList = []
                #choose good runs
                if sub=="003":
                    runs=[1, 3, 4, 6, 7, 8]
                elif sub=="006" or sub == '053' or sub == '071':
                    runs = [1, 2, 3, 4, 5, 7, 8]
                elif sub == "009":
                    runs = [1, 2, 3, 4, 7, 8]
                elif sub == "019" or sub == '024' or sub == '047' or sub == '059' or sub == '067':
                    runs = [2, 3, 4, 5, 6, 7, 8]
                elif sub == "021":
                    runs = [1, 2, 3, 6, 8]
                elif sub == "022":
                    runs = [1, 2, 3, 4, 8]
                elif sub == "023":
                    runs = [1, 2, 4, 7]
                elif sub == "026" or sub == '066':
                    runs = [1, 2, 3, 5, 7, 8]
                elif sub == "033":
                    runs = [1,2,3,4,5,8]
                elif sub == "034":
                    runs = [1,2,3,5,6,7,8]
                elif sub == "035":
                    runs = [1,3,4,5,6,7,8]
                elif sub == "037":
                    runs = [1, 2, 3, 4, 5, 6, 8]
                elif sub == "040":
                    runs = [1, 2, 3, 4, 7, 8]
                elif sub == "049":
                    runs = [1,2,4,5,6,7,8]
                elif sub == "061":
                    runs = [1,2,3,4]
                elif sub == "068" or sub =="011":
                    runs = [1,2,3,4,5,6,7]
                elif sub == "075":
                    runs = [1,2,3,4,8]
                elif sub == "077":
                    runs = [1,4,6,8]
                else:
                    runs=[1,2,3,4,5,6,7,8]
                try:
                    for run1 in runs:
                        # loading up whitened ones
                        try:
                            tmp_df=pd.read_csv('YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/prewhitenedBetas/'+ sub + '_' + maskName  + '_run' + str(run1) + '_allbetas_trialwise_extended.csv', usecols=["sub", "mask", "model","run","trial", "voxel", "Congruency", "StimVal", "trialNum", "order", "ImgStim", "trialcorrect", "condition", "valmn", "aromn", "RT", "Treal_precise", "Testimate_precise", "Tprecise_biasabs", "Tprecise_bias", "Testimate_run", "Trun_biasabs", "Trun_bias", "pval_PerciseChance", "pval_RunChance", "PercisepChanceFlag", "PerciseBiasFlag", "RunBias1Flag", "RunBias2Flag","ReconMem","ConfReconMem","ConfCoarseMem", "residTprecise", "residTpreciseabs", "PreciseBiaslmFlag", 'residTprecise', 'residTpreciseabs', 'PreciseBiaslmFlag',"value", "value_whiten"])
#                             print("Cokumn Names: ", tmp_df.columns.tolist())
                            betaList.append(tmp_df)
                        except:
                            print('YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/prewhitenedBetas/'+ sub + '_' + maskName  + '_run' + str(run1) + '_allbetas_trialwise_extended.csv')
                            print ("could not load dataframe for run" + str(run1)) #some of the subjects won't have certain run due to excess motion
                            # continue
#
                    betas_dataframe = pd.concat(betaList, axis = 0, ignore_index = True)
                    print("finished loading all runs in one dataframe")

                    trial_pairs = list(itertools.permutations(np.unique(betas_dataframe['trial']), 2))
#                     print('here2')
#                     print("runs for current sub: "+str(runs[1])+str(runs[2]))
                    for run in runs:
                        for tmp_pair in trial_pairs:

                            temp_df1=betas_dataframe[(betas_dataframe['run']==run) & (betas_dataframe['trial']==tmp_pair[0])]
                            temp_df2=betas_dataframe[(betas_dataframe['run']==run) & (betas_dataframe['trial']==tmp_pair[1])]


                            b1=np.asarray(temp_df1.value_whiten)
                            b2=np.asarray(temp_df2.value_whiten)
                            distance = scipy.stats.pearsonr(b1, b2)[0]  #
                            
                            euclidean = scipy.spatial.distance.euclidean(b1, b2)
                            # get mask voxel number
                            nvox = max(betas_dataframe['voxel']) + 1
                            DistanceIndex = euclidean / nvox

                            #Map the numeric numbers back to the strings for each condition
                            Congruency1=Congruency_labels[int(np.unique(temp_df1['Congruency'])[0])]
                            Congruency2=Congruency_labels[int(np.unique(temp_df2['Congruency'])[0])]

                            StimVal1 = StimVal_labels[int(np.unique(temp_df1['StimVal'])[0])]
                            StimVal2 = StimVal_labels[int(np.unique(temp_df2['StimVal'])[0])]
                            
                            StimValdiff = np.unique(temp_df1['StimVal'])[0] - np.unique(temp_df2['StimVal'])[0]
                            StimValdiffabs = abs(np.unique(temp_df2['StimVal'])[0] - np.unique(temp_df1['StimVal'])[0])


                            trialcorrect1 = trialcorrect_labels[int(np.unique(temp_df1['trialcorrect'])[0])]
                            trialcorrect2 = trialcorrect_labels[int(np.unique(temp_df2['trialcorrect'])[0])]

#                             print('here1')
                            condition1 = condition_labels[int(np.unique(temp_df1['condition'])[0])]
                            condition2 = condition_labels[int(np.unique(temp_df2['condition'])[0])]

                            PercisepChanceFlag1 = PercisepChanceFlag_labels[int(np.unique(temp_df1['PercisepChanceFlag'])[0])]
                            PercisepChanceFlag2 = PercisepChanceFlag_labels[int(np.unique(temp_df2['PercisepChanceFlag'])[0])]

                            PerciseBiasFlag1 = PercisepBiasFlag_labels[
                                int(np.unique(temp_df1['PerciseBiasFlag'])[0])]
                            PerciseBiasFlag2 = PercisepBiasFlag_labels[
                                int(np.unique(temp_df2['PerciseBiasFlag'])[0])]

                            RunBias1Flag1 = RunBias1Flag_labels[
                                int(np.unique(temp_df1['RunBias1Flag'])[0])]
                            RunBias1Flag2 = RunBias1Flag_labels[
                                int(np.unique(temp_df2['RunBias1Flag'])[0])]

                            RunBias2Flag1 = RunBias2Flag_labels[
                                int(np.unique(temp_df1['RunBias2Flag'])[0])]
                            RunBias2Flag2 = RunBias2Flag_labels[
                                int(np.unique(temp_df2['RunBias2Flag'])[0])]

#                             print('here0')
                            # fill in ras_df
                            rsa_df['mask'].append(maskName)
                            rsa_df['sub'].append(sub)
                            rsa_df['model'].append(model)
                            rsa_df['run'].append(run)
                            rsa_df['corr'].append(distance)
                            rsa_df['corr_z'].append(np.log(1+distance)-np.log(1-distance))
                            rsa_df['DistanceIndex'].append(DistanceIndex)
                            rsa_df['trial1'].append(tmp_pair[0])
                            rsa_df['trial2'].append(tmp_pair[1])

                            rsa_df['triallag'].append(tmp_pair[1]-tmp_pair[0])
                            #Column for crossInstr, the instr happends between trial 11 and 12
                            if tmp_pair[1] in list(range(0, 12, 1)) and tmp_pair[0] in list(range(0, 12, 1)):
                                crossInstr="within"
                            elif tmp_pair[1] in list(range(12, 24, 1)) and tmp_pair[0] in list(range(12, 24, 1)):
                                crossInstr = "within"
                            else:
                                crossInstr = "between"
                            rsa_df['crossInstr'].append(crossInstr)
                            rsa_df['Congruency1'].append(Congruency1)
                            rsa_df['Congruency2'].append(Congruency2)

#                             print('here0')
                            rsa_df['StimVal1'].append(StimVal1)
                            rsa_df['StimVal2'].append(StimVal2)
#                             print('here1')
                            print(str(StimValdiff))
                            rsa_df['StimValdiff'].append(StimValdiff)
#                             print('here2')
                            rsa_df['StimValdiffabs'].append(StimValdiffabs)
#                             print('here3')
                            rsa_df['order'].append(np.unique(temp_df2['order'])[0])
                            rsa_df['ImgStim1'].append(np.unique(temp_df1['ImgStim'])[0])
#                             print('here2')
                            rsa_df['ImgStim2'].append(np.unique(temp_df2['ImgStim'])[0])
                            rsa_df['condition1'].append(condition1)
#                             print('here3')
                            rsa_df['condition2'].append(condition2)
                            rsa_df['trialcorrect1'].append(trialcorrect1)
                            rsa_df['trialcorrect2'].append(trialcorrect2)
                            rsa_df['valmn1'].append(np.unique(temp_df1['valmn'])[0])
                            rsa_df['valmn2'].append(np.unique(temp_df2['valmn'])[0])
                            rsa_df['aromn1'].append(np.unique(temp_df1['aromn'])[0])
                            rsa_df['aromn2'].append(np.unique(temp_df2['aromn'])[0])
                            rsa_df['RT1'].append(np.unique(temp_df1['RT'])[0])
                            rsa_df['RT2'].append(np.unique(temp_df2['RT'])[0])
#                             print('here0')
                            rsa_df['Treal_precise1'].append(np.unique(temp_df1['Treal_precise'])[0])
                            rsa_df['Treal_precise2'].append(np.unique(temp_df2['Treal_precise'])[0])
                            rsa_df['Testimate_precise1'].append(np.unique(temp_df1['Testimate_precise'])[0])
                            rsa_df['Testimate_precise2'].append(np.unique(temp_df2['Testimate_precise'])[0])
                            rsa_df['Tprecise_biasabs1'].append(np.unique(temp_df1['Tprecise_biasabs'])[0])
                            rsa_df['Tprecise_biasabs2'].append(np.unique(temp_df2['Tprecise_biasabs'])[0])
                            rsa_df['Tprecise_bias1'].append(np.unique(temp_df1['Tprecise_bias'])[0])
                            rsa_df['Tprecise_bias2'].append(np.unique(temp_df2['Tprecise_bias'])[0])
                            rsa_df['Testimate_run1'].append(np.unique(temp_df1['Testimate_run'])[0])
                            rsa_df['Testimate_run2'].append(np.unique(temp_df2['Testimate_run'])[0])
                            rsa_df['Trun_biasabs1'].append(np.unique(temp_df1['Trun_biasabs'])[0])
                            rsa_df['Trun_biasabs2'].append(np.unique(temp_df2['Trun_biasabs'])[0])
                            rsa_df['Trun_bias1'].append(np.unique(temp_df1['Trun_bias'])[0])
                            rsa_df['Trun_bias2'].append(np.unique(temp_df2['Trun_bias'])[0])

#                             print('here1')
                            rsa_df['pval_PerciseChance1'].append(np.unique(temp_df1['pval_PerciseChance'])[0])
#                             print('here2')
                            rsa_df['pval_PerciseChance2'].append(np.unique(temp_df2['pval_PerciseChance'])[0])
#                             print('here3')
                            rsa_df['pval_RunChance1'].append(np.unique(temp_df1['pval_RunChance'])[0])
                            rsa_df['pval_RunChance2'].append(np.unique(temp_df2['pval_RunChance'])[0])
                            rsa_df['PercisepChanceFlag1'].append(PercisepChanceFlag1)
                            rsa_df['PercisepChanceFlag2'].append(PercisepChanceFlag2)
                            rsa_df['PerciseBiasFlag1'].append(PerciseBiasFlag1)
                            rsa_df['PerciseBiasFlag2'].append(PerciseBiasFlag2)
                            rsa_df['RunBias1Flag1'].append(RunBias1Flag1)
                            rsa_df['RunBias1Flag2'].append(RunBias1Flag2)
                            rsa_df['RunBias2Flag1'].append(RunBias2Flag1)
                            rsa_df['RunBias2Flag2'].append(RunBias2Flag2)

#                             print('here1')
                            rsa_df['ReconMem1'].append(np.unique(temp_df1['ReconMem'])[0])
#                             print('here2')
                            rsa_df['ConfReconMem1'].append(np.unique(temp_df1['ConfReconMem'])[0])
                            rsa_df['ConfCoarseMem1'].append(np.unique(temp_df1['ConfCoarseMem'])[0])
                            rsa_df['ReconMem2'].append(np.unique(temp_df2['ReconMem'])[0])
                            rsa_df['ConfReconMem2'].append(np.unique(temp_df2['ConfReconMem'])[0])
                            rsa_df['ConfCoarseMem2'].append(np.unique(temp_df2['ConfCoarseMem'])[0])


                            rsa_df['residTprecise1'].append(np.unique(temp_df1['residTprecise'])[0])
                            rsa_df['residTprecise2'].append(np.unique(temp_df2['residTprecise'])[0])

                            rsa_df['residTpreciseabs1'].append(np.unique(temp_df1['residTpreciseabs'])[0])
                            rsa_df['residTpreciseabs2'].append(np.unique(temp_df2['residTpreciseabs'])[0])

                            rsa_df['PreciseBiaslmFlag1'].append(np.unique(temp_df1['PreciseBiaslmFlag'])[0])
                            rsa_df['PreciseBiaslmFlag2'].append(np.unique(temp_df2['PreciseBiaslmFlag'])[0])
#                             print('here3')
                            # print(rsa_df)
# 								print (rsa_df.info(verbose=False, memory_usage="deep"))

                            #
                            # except:
                            # 	print ("failed at RSA stage " + sub+ " " + str(run1) + str(run2))
# 						del betas_dataframe
# 						gc.collect()

                except:
                    print ("could not open data run" + str(run) + str(maskName)+ "_" + sub + "_"	+ model)
                    # continue


            all_rsas=pd.DataFrame(rsa_df)
            all_rsas = all_rsas.sort_values(by=['sub', 'trial1', 'trial2','mask'])
            all_rsas.to_csv('YourMainFolder/ASAP/AA_fMRI/process/results/RSAbymask/' +  str(maskName) + "_all_rsas_betas_whitened_trialwise_extended.csv", index=False)



