import matplotlib
# matplotlib.use('TkAgg')
import os
# imports
import numpy as np
#np.set_printoptions(precision = 3)
import matplotlib.pyplot as plt

import scipy
#get_ipython().magic('matplotlib inline')
import pandas as pd
#pd.set_option('precision',2)
import scipy.io as io
import json
#sns.set(color_codes=True)
#sns.set_style('white')
import os, subprocess, sys, glob
import nibabel as nib
import nilearn, sklearn
from nilearn import image,  input_data, decoding #plotting,
import sklearn.svm
from sklearn.pipeline import Pipeline
#from sklearn.cross_validation import LeaveOneLabelOut, cross_val_score, permutation_test_score
from sklearn.model_selection import LeaveOneGroupOut, cross_val_score, permutation_test_score
from sklearn.feature_selection import SelectKBest, f_classif
###unable to import the below, cross_validation was depracated a year and a half ago
#from sklearn.cross_validation import LeaveOneLabelOut
#from sklearn.model_selection import LeaveOneLabelOut


# In[3]:

# sub=sys.argv[1]
sub = 'replacesub'

# masks = ["harvardoxford_Hippocampus_bin60_2mm", "L_harvardoxford_Hippocampus_bin60_2mm", "R_harvardoxford_Hippocampus_bin60_2mm", "FS_FPl", "FS_lh.L_FPl", "FS_rh.R_FPl", "FS_entorhinal_exvivo.thresh", "FS_rh.entorhinal_exvivo.thresh", "FS_lh.entorhinal_exvivo.thresh", "AMY_BLcx_2mm", "AMY_BL_2mm", "AMY_BM_2mm", "AMY_CE_2mm", "AMY_La_2mm", "Amy_50_bin", "L_AMY_BLcx_2mm", "L_AMY_BL_2mm", "L_AMY_BM_2mm", "L_AMY_CE_2mm", "L_AMY_La_2mm", "L_Amy_50_bin", "R_AMY_BLcx_2mm", "R_AMY_BL_2mm", "R_AMY_BM_2mm", "R_AMY_CE_2mm", "R_AMY_La_2mm", "R_Amy_50_bin"]
# masks = ["harvardoxford_Hippocampus_bin60_2mm_Anterior", "L_harvardoxford_Hippocampus_bin60_2mm_Anterior", "R_harvardoxford_Hippocampus_bin60_2mm_Anterior", "harvardoxford_Hippocampus_bin60_2mm_Mid", "L_harvardoxford_Hippocampus_bin60_2mm_Mid", "R_harvardoxford_Hippocampus_bin60_2mm_Mid","harvardoxford_Hippocampus_bin60_2mm_Posterior", "L_harvardoxford_Hippocampus_bin60_2mm_Posterior", "R_harvardoxford_Hippocampus_bin60_2mm_Posterior", "harvardoxford_Hippocampus_bin60_2mm", "L_harvardoxford_Hippocampus_bin60_2mm", "R_harvardoxford_Hippocampus_bin60_2mm", "FS_FPl", "FS_lh.L_FPl", "FS_rh.R_FPl", "FS_entorhinal_exvivo.thresh", "FS_rh.entorhinal_exvivo.thresh", "FS_lh.entorhinal_exvivo.thresh", "AMY_BLcx_2mm", "AMY_BL_2mm", "AMY_BM_2mm", "AMY_CE_2mm", "AMY_La_2mm", "Amy_50_bin", "L_AMY_BLcx_2mm", "L_AMY_BL_2mm", "L_AMY_BM_2mm", "L_AMY_CE_2mm", "L_AMY_La_2mm", "L_Amy_50_bin", "R_AMY_BLcx_2mm", "R_AMY_BL_2mm", "R_AMY_BM_2mm", "R_AMY_CE_2mm", "R_AMY_La_2mm", "R_Amy_50_bin"]
masks = ["perirhinal_exvivo.thresh", "harvardoxford_Hippocampus_bin60_2mm_Anterior", "L_harvardoxford_Hippocampus_bin60_2mm_Anterior", "R_harvardoxford_Hippocampus_bin60_2mm_Anterior", "harvardoxford_Hippocampus_bin60_2mm_Mid", "L_harvardoxford_Hippocampus_bin60_2mm_Mid", "R_harvardoxford_Hippocampus_bin60_2mm_Mid","harvardoxford_Hippocampus_bin60_2mm_Posterior", "L_harvardoxford_Hippocampus_bin60_2mm_Posterior", "R_harvardoxford_Hippocampus_bin60_2mm_Posterior", "harvardoxford_Hippocampus_bin60_2mm", "L_harvardoxford_Hippocampus_bin60_2mm", "R_harvardoxford_Hippocampus_bin60_2mm", "FS_FPl", "FS_lh.L_FPl", "FS_rh.R_FPl", "FS_entorhinal_exvivo.thresh", "FS_rh.entorhinal_exvivo.thresh", "FS_lh.entorhinal_exvivo.thresh", "AMY_BM_2mm", "AMY_CE_2mm", "Amy_50_bin", "9-46", "FP", "PMd", "M1", "32pl", "FPm", "9-46v", "9-46d", 'V1_exvivo.thresh', "BA4a_exvivo.thresh", "BA4p_exvivo.thresh", "BA4_exvivo.thresh", "25"]
#outPath='/home/despoA/lapate/agng/analysis/MVPA/'
models=['MVPA_3mm']  #todo change
myGLMModels=['noTD_ST']  #todo change

runs=['1','2','3','4','5','6','7','8']
# runs=['1', '2']
regtypes=['MVPA'] #

#Load the bad voxel/trial from TRbyTR analysis

fieldnames = ['sub','run','trial','mask','voxel']
file = "YourMainFolder/ASAP/AA_fMRI/process/results/TRbyTR/trialwise_matrix/" + sub + "_TRbyTR_trialwise_bad.csv"
if os.path.exists(file):
    badvox = pd.read_csv(file, usecols = fieldnames, delimiter =',', header = 0)
    badvox['badvox_Flag'] = "outlier"
    badvox['sub'] = badvox['sub'].apply(lambda x: str(x).zfill(3))
    badvoxcheck="bad"
else:
    badvoxcheck="nobad"
    print("no bad voxel/trial for participant: " + sub)

# print(badvox)

##for sub in subs:
for myGLMModel in myGLMModels:
    for model in models:
        for regtype in regtypes:
            #for sub in subs:
            betas = {'ReconMem':[], 'ConfReconMem':[], 'ConfCoarseMem': [],'sub':[],'mask':[],'model':[],'run':[],'trial':[], 'voxel':[], 'value':[], 'Congruency':[], 'StimVal':[],'Action':[], 'TargetVal':[],'NonTargetVal':[],'trialNum':[], 'order':[], 'ImgStim':[], 'condition': [], 'valmn':[], 'aromn':[], 'valsd':[], 'arosd': [], 'trialcorrect': [], 'RT': [],'Treal_precise': [], 'Testimate_precise': [], 'Tprecise_biasabs':[], 'Tprecise_bias':[], 'Testimate_run':[], 'Trun_biasabs':[], 'Trun_bias':[], 'pval_PerciseChance':[], 'pval_RunChance':[], 'PercisepChanceFlag':[], 'PerciseBiasFlag':[], 'RunBias1Flag':[], 'RunBias2Flag':[], 'residTprecise':[], 'residTpreciseabs':[], 'PreciseBiaslmFlag':[]}
            for maskName in masks:
                try:
                    print(maskName)
                    maskDataPath = os.path.join(
                        'YourMainFolder/ASAP/AA_fMRI/process/results/' + sub + '/finalmasks')  # REGISTERED MASK NAME! #todo change

                    maskPath = os.path.join(maskDataPath, str(maskName) + '_anat_resampled_final.nii.gz')
                    print(maskPath)
                    # orig!! no thresh
                    #                         mask = nib.load(maskPath).get_data().astype(bool)
                    ## thresh according to the mask
                    mask_temp = nib.load(maskPath).get_fdata()
                    if "FS" in maskName:
                        mask_thres = mask_temp >= .05  # relevant for Free Surfer PFC probabilistic maps
                    elif "AMY" in maskName:
                        mask_thres = mask_temp >= 0.25  # relevant for Tyzka AMY subnuclei probabilistic maps
                    elif "Amy" in maskName or 'harvardoxford' in maskName:
                        mask_thres = mask_temp >= 0.7  # relevant for harvard-oxford probabilistic maps
                    else:
                        mask_thres = mask_temp >= .05  # new FS masks
                    for run in runs:
                        try:
                            ###GO THROUGH CSV AND ADD TASK/CONDITION INFORMATION
                            csvFile = 'YourMainFolder/ASAP/AA_fMRI/process/AA_beh/Bev_multivariate/AA_bev_' + sub + '_' + run + '.csv'  # todo change
                            separator = ','
                            trialList = [trial.split(separator) for trial in
                                         open(csvFile, 'r').readlines()]  # CSV each row= 1 trial
                            colNames = trialList[0]
                            trialList = trialList[1:]
                            trialDict = []  # trialDict will be a list of dictionaries for each trial that contains the column name and value
                            for curTrial in trialList:
                                tempDict = {}
                                try:
                                    for colNum, curCol in enumerate(colNames):  # looping through enumerate object that has a counter to each column name
                                        if curTrial[colNum]=='NA':
                                            tempDict[json.loads(curCol).rstrip()] = curTrial[colNum].rstrip()
                                        else:
                                            if json.loads(curCol)==str:
                                                tempDict[json.loads(curCol).rstrip()] = json.loads(curTrial[colNum])  # tempDict is a dictionary with the column name and value for each trial
                                            elif json.loads(curTrial[colNum])==str:
                                                tempDict[json.loads(curCol)] = json.loads(curTrial[colNum]).rstrip()
                                            elif json.loads(curCol)==str and json.loads(curTrial[colNum])==str:
                                                tempDict[json.loads(curCol).rstrip()] = json.loads(curTrial[colNum]).rstrip()
                                            else:
                                                tempDict[json.loads(curCol)] = json.loads(curTrial[colNum])
                                except:
                                    print('this is the trouble trial ' + curCol + " " + colNum)
                                trialDict.append(tempDict)
                            # templist stores information for each trial and its information is appended to totallist
                            templist = []
                            index = 0
                            # go through the trials in the csv file
                            subvect, maskvect, runvect, Congruencyvect, StimValvect, Actionvect, TargetValvect, NonTargetValvect, trialNumvect, ordervect, ImgStimvect, conditionvect = [], [], [], [], [], [], [], [], [], [], [], []
                            # additional initializations
                            valmnvect, aromnvect, valsdvect, arosdvect, trialcorrectvect, RTvect, Treal_precisevect, Testimate_precisevect, Tprecise_biasabsvect, Tprecise_biasvect, Testimate_runvect, Trun_biasabsvect, Trun_biasvect = [], [], [], [], [], [], [], [], [], [], [], [], []
                            pval_PerciseChancevect, pval_RunChancevect, PercisepChanceFlagvect, PerciseBiasFlagvect, RunBias1Flagvect, RunBias2Flagvect, ReconMemvect, ConfCoarseMemvect, ConfReconMemvect, residTprecisevect, residTpreciseabsvect, PreciseBiaslmFlagvect = [], [], [], [], [], [], [], [], [], [], [], []
                            for trial in enumerate(trialDict):
                                # Recognition memory
                                if trial[1]['ReconMem'] == 'YES':
                                    ReconMem = 1
                                elif trial[1]['ReconMem'] == 'NO':
                                    ReconMem = 2

                                # confidence rating of Recognition memory
                                if trial[1]['ConfReconMem'] == 'NotConfAtALL_1':
                                    ConfReconMem = 1
                                elif trial[1]['ConfReconMem'] == 'SConf_1':
                                    ConfReconMem = 2
                                elif trial[1]['ConfReconMem'] == 'ModConf_1':
                                    ConfReconMem = 3
                                elif trial[1]['ConfReconMem'] == 'VeryConf_1':
                                    ConfReconMem = 4

                                # confidence rating of Recognition memory
                                if trial[1]['ConfCoarseMem'] == 'NotConfAtALL_2':
                                    ConfCoarseMem = 1
                                elif trial[1]['ConfCoarseMem'] == 'SConf_2':
                                    ConfCoarseMem = 2
                                elif trial[1]['ConfCoarseMem'] == 'ModConf_2':
                                    ConfCoarseMem = 3
                                elif trial[1]['ConfCoarseMem'] == 'VeryConf_2':
                                    ConfCoarseMem = 4

                                # Congruency labels
                                if trial[1]['Congruency'] == 'Incon':
                                    Cong = 1  # Incongruent
                                elif trial[1]['Congruency'] == 'Con':
                                    Cong = 2  # Congruenct

                                # stimuli valence labels
                                if trial[1]['StimVal'] == 'neg':
                                    valence = 1 #neg
                                elif trial[1]['StimVal'] == 'pos':
                                    valence = 2 #pos

                                # Action goal label
                                if trial[1]['Action'] == 'go':
                                    actiongoal = 1  # go/approach
                                elif trial[1]['Action'] == 'nogo':
                                    actiongoal = 2  # nogo/avoid

                                # Target valence label
                                if trial[1]['TargetVal'] == 'neg':
                                    TarVal = 1  # neg
                                elif trial[1]['TargetVal'] == 'pos':
                                    TarVal = 2  # pos

                                # Nontarget valence label
                                if trial[1]['nonTargetVal'] == 'neg':
                                    NonTarVal = 1  #neg
                                elif trial[1]['nonTargetVal'] == 'pos':
                                    NonTarVal = 2  #pos

                                # Memory flag for precise p metrics
                                if trial[1]['PercisepChanceFlag'] == 'MemSuccess':
                                    MemFlag_pchance = 1
                                elif trial[1]['PercisepChanceFlag'] == 'MemFail':
                                    MemFlag_pchance = 2
                                elif trial[1]['PercisepChanceFlag'] == 'MemBetween':
                                    MemFlag_pchance = 3

                                # Memory flag for precise estimate bias metrics
                                if trial[1]['PerciseBiasFlag'] == 'MemSuccess':
                                    MemFlag_PerciseBias = 1
                                elif trial[1]['PerciseBiasFlag'] == 'MemFail':
                                    MemFlag_PerciseBias = 2
                                elif trial[1]['PerciseBiasFlag'] == 'MemBetween':
                                    MemFlag_PerciseBias = 3

                                # Memory flag for run estimate bias 1 metrics
                                if trial[1]['RunBias1Flag'] == 'MemSuccess':
                                    MemFlag_RunBias1 = 1
                                elif trial[1]['RunBias1Flag'] == 'MemFail':
                                    MemFlag_RunBias1 = 2
                                elif trial[1]['RunBias1Flag'] == 'MemBetween':
                                    MemFlag_RunBias1 = 3

                                # Memory flag for run estimate bias 2 metrics
                                if trial[1]['RunBias2Flag'] == 'MemSuccess':
                                    MemFlag_RunBias2 = 1
                                elif trial[1]['RunBias2Flag'] == 'MemFail':
                                    MemFlag_RunBias2 = 2
                                elif trial[1]['RunBias2Flag'] == 'MemBetween':
                                    MemFlag_RunBias2 = 3

                                # conditionLabels
                                if (trial[1]['StimVal'] == "neg") and (trial[1]['Action'] == "go"):
                                    # print("neg_go")
                                    condition = 1  # neg_go
                                elif (trial[1]['StimVal'] == "pos") and (trial[1]['Action'] == "go"):
                                    # print("pos_go")
                                    condition = 2  # pos_go
                                elif (trial[1]['StimVal'] == "neg") and (trial[1]['Action'] == "nogo"):
                                    condition = 3  # neg_noGo
                                elif (trial[1]['StimVal'] == "pos") and (trial[1]['Action'] == "nogo"):
                                    condition = 4  # pos_noGo


                                # participant ID
                                participant = trial[1]['participant']
                                # run number
                                runNum = trial[1]['run']
                                # trial number: 1-12
                                trialNum = trial[1]['trialNum']
                                # order num: just a control, since my fMRI has two orders balanced across participants
                                orderNum = trial[1]['order']
                                # image stimuli
                                ImgStimuli = trial[1]['ImgStim']
                                # normalized image valence
                                Imgvalmn_norm = trial[1]['valmn']
                                # normalized image valence sd
                                Imgvalsd_norm = trial[1]['valsd']
                                # normalized image arousal
                                Imgaromn_norm = trial[1]['aromn']
                                # normalized image arousal sd
                                Imgarosd_norm = trial[1]['arosd']

                                # joystick experiment correct
                                joycorrect = trial[1]['trial_correct_RTcal']
                                # joystick experiment RT
                                joyRT = trial[1]['joystick_RTcal']
                                # precise display time for the stimuli
                                Treal_precise = trial[1]['Treal_precise']
                                # estimated display time for the stimuli
                                Testimate_precise = trial[1]['Testimate_precise']
                                # absolute bias of estimated display time
                                Tprecise_biasabs = trial[1]['Tprecise_biasabs']
                                # bias of estimated display time
                                Tprecise_bias = trial[1]['Tprecise_bias']
                                # estimated run
                                Testimate_run = trial[1]['Testimate_run']

                                #Get the lm residual measures (Jenkin's)
                                PreciseBiaslmFlag = trial[1]['PreciseBiaslmFlag']
                                residTprecise = trial[1]['residTprecise']
                                residTpreciseabs = trial[1]['residTpreciseabs']

                                # absolute estimated run bias
                                Trun_biasabs = trial[1]['Trun_biasabs']
                                # estimated run bias
                                Trun_bias = trial[1]['Trun_bias']
                                # parametric change p for each precise estimates of stimuli display
                                pval_PerciseChance = trial[1]['pval_PerciseChance']
                                # parametric change p for each run estimates of stimuli display
                                pval_RunChance = trial[1]['pval_RunChance']

                                # FILL IN LISTS
                                subvect.append(participant)
                                runvect.append(runNum)
                                Congruencyvect.append(Cong)
                                StimValvect.append(valence)
                                Actionvect.append(actiongoal)
                                TargetValvect.append(TarVal)
                                NonTargetValvect.append(NonTarVal)
                                trialNumvect.append(trialNum)
                                ordervect.append(orderNum)
                                ImgStimulitmp_1  = ImgStimuli.replace('stimuli/','')
                                ImgStimulitmp_2 = ImgStimulitmp_1.replace('.jpg', '')
                                ImgStimvect.append(ImgStimulitmp_2)
                                conditionvect.append(condition)

                                valmnvect.append(Imgvalmn_norm)
                                aromnvect.append(Imgaromn_norm)
                                valsdvect.append(Imgvalsd_norm)
                                arosdvect.append(Imgarosd_norm)
                                trialcorrectvect.append(joycorrect)
                                RTvect.append(joyRT)
                                Treal_precisevect.append(Treal_precise)
                                Testimate_precisevect.append(Testimate_precise)
                                Tprecise_biasabsvect.append(Tprecise_biasabs)
                                Tprecise_biasvect.append(Tprecise_bias)
                                Testimate_runvect.append(Testimate_run)
                                Trun_biasabsvect.append(Trun_biasabs)
                                Trun_biasvect.append(Trun_bias)
                                pval_PerciseChancevect.append(pval_PerciseChance)
                                pval_RunChancevect.append(pval_RunChance)
                                PercisepChanceFlagvect.append(MemFlag_pchance)
                                PerciseBiasFlagvect.append(MemFlag_PerciseBias)
                                RunBias1Flagvect.append(MemFlag_RunBias1)
                                RunBias2Flagvect.append(MemFlag_RunBias2)
                                ReconMemvect.append(ReconMem)
                                ConfReconMemvect.append(ConfReconMem)
                                ConfCoarseMemvect.append(ConfCoarseMem)

                                PreciseBiaslmFlagvect.append(PreciseBiaslmFlag)
                                residTprecisevect.append(residTprecise)
                                residTpreciseabsvect.append(residTpreciseabs)

                            ### LOAD MRI BETAS DATA
                            # dataPath = os.path.join(
                            #    '/home/despoA/lapate/agng/data/mri/processed/' + sub + '/func/' + cond + '/run' + run + '/' + cond + '_run' + run + '_GLM_noTD_ST_MVPA_3mm_allTrials.feat/' + regtype + '/')  # LOAD REGISTER3D AND MERGED BETAS FOR THAT RUN!!!
                            dataPath = "YourMainFolder/ASAP/AA_fMRI/process/results/" + sub + "/run" + run + "/" + sub + "_run" + run + "_GLM_" + myGLMModel+ "_" + regtype + "_extended_allTrials.feat/" + regtype
#                             print("This is PEmerge path:" + dataPath)
                            fn = sub + '_run_' + run + '_merged.nii.gz'

                            ds_name = os.path.join(dataPath, fn)
#                             print(ds_name)
                            wholebrain_data = nib.load(ds_name).get_fdata().astype(float)
#                             print('wholebrain_data shape: ' + str(wholebrain_data.shape))
#                             print('mask shape:' + str(mask_thres.shape))
                            # thresh at 25
                            data = wholebrain_data[mask_thres]  # indexing the ones greater than threshold
                            ### LOOP THROUGH MASK VOXELS AND TRIAL NUMBERS
#                             print('data shape: ' + str(data.shape))
                            for n, val in enumerate(data):  # looping across EACH VOXEL (i.e., 18 times (mask w 18 vox's))
                                for trial in range(data.shape[1]):  # 24 times, per trial in each run
                                    betas['sub'].append(sub)
                                    betas['mask'].append(str(maskName))
                                    betas['model'].append(model)
                                    # the index number of what it is  #map of the mask
                                    # gets the actual beta value for specific trial and voxel number
                                    betas['run'].append(int(run))
                                    betas['trial'].append(trial)
                                    betas['voxel'].append(n)
                                    betas['value'].append(val[trial])
                                    betas['Congruency'].append(Congruencyvect[trial])
                                    betas['StimVal'].append(StimValvect[trial])
                                    betas['Action'].append(Actionvect[trial])
                                    betas['TargetVal'].append(TargetValvect[trial])
                                    betas['NonTargetVal'].append(NonTargetValvect[trial])
                                    betas['trialNum'].append(trialNumvect[trial])
                                    betas['order'].append(ordervect[trial])
                                    betas['ImgStim'].append(ImgStimvect[trial])
                                    betas['condition'].append(conditionvect[trial])
                                    betas['valmn'].append(valmnvect[trial])
                                    betas['aromn'].append(aromnvect[trial])
                                    betas['valsd'].append(valsdvect[trial])
                                    betas['arosd'].append(arosdvect[trial])
                                    betas['trialcorrect'].append(trialcorrectvect[trial])
                                    betas['RT'].append(RTvect[trial])
                                    betas['Treal_precise'].append(Treal_precisevect[trial])
                                    betas['Testimate_precise'].append(Testimate_precisevect[trial])
                                    betas['Tprecise_biasabs'].append(Tprecise_biasabsvect[trial])
                                    betas['Tprecise_bias'].append(Tprecise_biasvect[trial])
                                    betas['Testimate_run'].append(Testimate_runvect[trial])
                                    betas['Trun_biasabs'].append(Trun_biasabsvect[trial])
                                    betas['Trun_bias'].append(Trun_biasvect[trial])
                                    betas['pval_PerciseChance'].append(pval_PerciseChancevect[trial])
                                    betas['pval_RunChance'].append(pval_RunChancevect[trial])
                                    betas['PercisepChanceFlag'].append(PercisepChanceFlagvect[trial])
                                    betas['PerciseBiasFlag'].append(PerciseBiasFlagvect[trial])
                                    betas['RunBias1Flag'].append(RunBias1Flagvect[trial])
                                    betas['RunBias2Flag'].append(RunBias2Flagvect[trial])
                                    betas['ConfCoarseMem'].append(ConfCoarseMemvect[trial])
                                    betas['ConfReconMem'].append(ConfReconMemvect[trial])
                                    betas['ReconMem'].append(ReconMemvect[trial])

                                    betas['residTprecise'].append(residTprecisevect[trial])
                                    betas['residTpreciseabs'].append(residTpreciseabsvect[trial])
                                    betas['PreciseBiaslmFlag'].append(PreciseBiaslmFlagvect[trial])

                        except:
                            print("could not open run " + run)
                except:
                    print("could not open data for mask " + maskName + "_" + sub + "_" + model)

                # ## saving betas
                # betas_dataframe = pd.DataFrame(betas)
                # print(betas_dataframe)
                # betas_dataframe.to_csv('/home/despoA/lapate/agng/data/mri/processed/RSA/' + str(
                #     sub) + "_" + cond + "_allbetas_25_trialwise.csv")  # final

            ## saving betas
            betas_dataframe = pd.DataFrame(betas)

            #remove bad voxel/trial use the flag from TRbyTR analysis
#             print(betas_dataframe)
#             print(badvox)
            badvoxcheck="nobad"
            if badvoxcheck=="nobad":
                betas_dataframe['badvox_Flag'] = "good"
            else:
                betas_dataframe = pd.merge(betas_dataframe, badvox, how='left',
                                           left_on=['sub','run','trial','mask','voxel'],
                                           right_on=['sub','run','trial','mask','voxel'])
                betas_dataframe['badvox_Flag'] = betas_dataframe['badvox_Flag'].fillna('good')

            #print the row with bad voxels
#             print(betas_dataframe[betas_dataframe['badvox_Flag'] == 'outlier'])

            #Filter bad rows
                betas_dataframe = betas_dataframe[betas_dataframe['badvox_Flag'] == 'good']

            # print(betas_dataframe)
            #calculate z score (Voxelwise activity estimates were z-scored per voxel, mask, run, and participant)
            #Create summarize dataframe for mean and sd per voxel, mask, run, and *participant
            df_mean = betas_dataframe.groupby(['voxel','run','mask','sub','model'],as_index=False)['value'].mean()
            df_mean.rename({'value': 'value_mean'}, axis=1, inplace=True)
            df_sd = betas_dataframe.groupby(['voxel','run','mask','sub','model'],as_index=False)['value'].std()
            df_sd.rename({'value': 'value_sd'}, axis=1, inplace=True)
            #merge sd and mean
            df_sum = pd.merge(df_mean, df_sd, how='inner', left_on=['voxel','run','mask','sub','model'], right_on=['voxel','run','mask','sub','model'])
            #merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe, df_sum, how='left', left_on=['voxel','run','mask','sub','model'], right_on=['voxel','run','mask','sub','model'])
            betas_dataframe_all['value_z'] = (betas_dataframe_all['value']-betas_dataframe_all['value_mean'])/betas_dataframe_all['value_sd']
            betas_dataframe_all.to_csv('YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/' +
                sub + "_allbetas_trialwise.csv")  # final
