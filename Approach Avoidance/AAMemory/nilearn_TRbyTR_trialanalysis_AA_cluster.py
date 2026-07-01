import matplotlib
import os
# imports
import numpy as np
# np.set_printoptions(precision = 3)
import matplotlib.pyplot as plt

import scipy
# get_ipython().magic('matplotlib inline')
import pandas as pd
# pd.set_option('precision',2)
import scipy.io as io
import json
# sns.set(color_codes=True)
# sns.set_style('white')
import os, subprocess, sys, glob
import nibabel as nib
from nilearn.image import math_img, index_img
import nilearn, sklearn
from nilearn import image, input_data, decoding  # plotting,
import sklearn.svm
from sklearn.pipeline import Pipeline
# from sklearn.cross_validation import LeaveOneLabelOut, cross_val_score, permutation_test_score
from sklearn.model_selection import LeaveOneGroupOut, cross_val_score, permutation_test_score
from sklearn.feature_selection import SelectKBest, f_classif

###unable to import the below, cross_validation was depracated a year and a half ago
# from sklearn.cross_validation import LeaveOneLabelOut
# from sklearn.model_selection import LeaveOneLabelOut


# In[3]:

# sub=sys.argv[1]
sub = 'replacesub'

masks = ["perirhinal_exvivo.thresh", "harvardoxford_Hippocampus_bin60_2mm", "harvardoxford_Hippocampus_bin60_2mm_Anterior", "harvardoxford_Hippocampus_bin60_2mm_Mid", "harvardoxford_Hippocampus_bin60_2mm_Posterior", "FS_FPl", "FS_entorhinal_exvivo.thresh", "Amy_50_bin", "9-46", "FP", "PMd", "M1", "32pl", "FPm", "9-46v", "9-46d", 'V1_exvivo.thresh', "BA4a_exvivo.thresh", "BA4p_exvivo.thresh", "BA4_exvivo.thresh", "25"]
# outPath='/home/despoA/lapate/agng/analysis/MVPA/'
models = ['MVPA_3mm']  # todo change
myGLMModels = ['noTD_ST']  # todo change

# choose good runs
if sub=="003":
    runs=['1', '3', '4', '6', '7', '8']
elif sub=="006" or sub == '053' or sub == '071':
    runs = ['1', '2', '3', '4', '5', '7', '8']
elif sub == "009":
    runs = ['1', '2', '3', '4', '7', '8']
elif sub == "019" or sub == '024' or sub == '047' or sub == '059' or sub == '067':
    runs = ['2', '3', '4', '5', '6', '7', '8']
elif sub == "021":
    runs = ['1', '2', '3', '6', '8']
elif sub == "022":
    runs = ['1', '2', '3', '4', '8']
elif sub == "023":
    runs = ['1', '2', '4', '7']
elif sub == "026" or sub == '066':
    runs = ['1', '2', '3', '5', '7', '8']
elif sub == "033":
    runs = ['1','2','3','4','5','8']
elif sub == "034":
    runs = ['1','2','3','5','6','7','8']
elif sub == "035":
    runs = ['1','3','4','5','6','7','8']
elif sub == "037":
    runs = ['1', '2', '3', '4', '5', '6', '8']
elif sub == "040":
    runs = ['1', '2', '3', '4', '7', '8']
elif sub == "049":
    runs = ['1','2','4','5','6','7','8']
elif sub == "061":
    runs = ['1','2','3','4']
elif sub == "068" or sub == "011":
    runs = ['1','2','3','4','5','6','7']
elif sub == "075":
    runs = ['1','2','3','4', '8']
elif sub == "077":
    runs = ['1','4','6','8']
else:
    runs = ['1', '2', '3', '4', '5', '6', '7', '8']
# runs=['1', '2']
regtypes = ['MVPA']  #

# Create a dictionary that contain time series for each mask
TSdict = {}

##for sub in subs:
for myGLMModel in myGLMModels:
    for model in models:
        for regtype in regtypes:
            # for sub in subs:
            betas = {'sub': [], 'mask': [], 'model': [], 'run': [], 'trial': [], 'voxel': [], 'value_TR0': [],
                     'value_TR1': [], 'value_TR2': [], 'value_TR3': [], 'value_TR4': [], 'value_TR5': [],
                     'value_TR6': [], 'value_TR7': [], 'value_TR8': [], 'imgonset': [], 'Congruency': [], 'StimVal': [],
                     'Action': [], 'TargetVal': [], 'NonTargetVal': [], 'trialNum': [], 'order': [], 'ImgStim': [],
                     'condition': [], 'valmn': [], 'aromn': [], 'valsd': [], 'arosd': [], 'trialcorrect': [], 'RT': [],
                     'Treal_precise': [], 'Testimate_precise': [], 'Tprecise_biasabs': [], 'Tprecise_bias': [],
                     'Testimate_run': [], 'Trun_biasabs': [], 'Trun_bias': [], 'pval_PerciseChance': [],
                     'pval_RunChance': [], 'PercisepChanceFlag': [], 'PerciseBiasFlag': [], 'RunBias1Flag': [],
                     'RunBias2Flag': [], 'ConfCoarseMem': [], 'ConfReconMem': [], 'ReconMem': []}
            for maskName in masks:
                try:
#                     print(maskName)
                    maskDataPath = os.path.join(
                        'YourMainFolder/ASAP/AA_fMRI/process/results/' + sub + '/finalmasks')  # REGISTERED MASK NAME! #todo change
                    maskPath = os.path.join(maskDataPath, str(maskName) + '_anat_resampled_final.nii.gz')
#                     print(maskPath)
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
                        mask_thres = mask_temp >= .05 #new FS masks

                    # create a list that contain all the time series for each run
                    RunwiseTS = []
                    AllrunTS = []
                    for run in runs:
                        try:
                            ###GO THROUGH CSV AND ADD TASK/CONDITION INFORMATION
                            csvFile = 'YourMainFolder/ASAP/AA_fMRI/process/AA_beh/Bev_multivariate/AA_bev_' + sub + '_' + run + '.csv'
                            separator = ','
                            trialList = [trial.split(separator) for trial in
                                         open(csvFile, 'r').readlines()]  # CSV each row= 1 trial
                            colNames = trialList[0]
                            trialList = trialList[1:]
                            trialDict = []  # trialDict will be a list of dictionaries for each trial that contains the column name and value
                            for curTrial in trialList:
                                tempDict = {}
                                try:
                                    for colNum, curCol in enumerate(
                                            colNames):  # looping through enumerate object that has a counter to each column name
                                        if curTrial[colNum] == 'NA':
                                            tempDict[json.loads(curCol).rstrip()] = curTrial[colNum].rstrip()
                                        else:
                                            if json.loads(curCol) == str:
                                                tempDict[json.loads(curCol).rstrip()] = json.loads(curTrial[
                                                                                                       colNum])  # tempDict is a dictionary with the column name and value for each trial
                                            elif json.loads(curTrial[colNum]) == str:
                                                tempDict[json.loads(curCol)] = json.loads(curTrial[colNum]).rstrip()
                                            elif json.loads(curCol) == str and json.loads(curTrial[colNum]) == str:
                                                tempDict[json.loads(curCol).rstrip()] = json.loads(
                                                    curTrial[colNum]).rstrip()
                                            else:
                                                tempDict[json.loads(curCol)] = json.loads(curTrial[colNum])
                                except:
                                    print('this is the trouble trial ' + curCol + " " + colNum)
                                trialDict.append(tempDict)
                            # templist stores information for each trial and its information is appended to totallist
                            templist = []
                            index = 0
                            # go through the trials in the csv file
                            imgonsetvect, subvect, maskvect, runvect, Congruencyvect, StimValvect, Actionvect, TargetValvect, NonTargetValvect, trialNumvect, ordervect, ImgStimvect, conditionvect = [], [], [], [], [], [], [], [], [], [], [], [], []
                            # additional initializations
                            valmnvect, aromnvect, valsdvect, arosdvect, trialcorrectvect, RTvect, Treal_precisevect, Testimate_precisevect, Tprecise_biasabsvect, Tprecise_biasvect, Testimate_runvect, Trun_biasabsvect, Trun_biasvect = [], [], [], [], [], [], [], [], [], [], [], [], []
                            pval_PerciseChancevect, pval_RunChancevect, PercisepChanceFlagvect, PerciseBiasFlagvect, RunBias1Flagvect, RunBias2Flagvect, ReconMemvect, ConfCoarseMemvect, ConfReconMemvect = [], [], [], [], [], [], [], [], []
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
                                    valence = 1  # neg
                                elif trial[1]['StimVal'] == 'pos':
                                    valence = 2  # pos

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
                                    NonTarVal = 1  # neg
                                elif trial[1]['nonTargetVal'] == 'pos':
                                    NonTarVal = 2  # pos

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
                                # image onset
                                Imgonset = trial[1]['image_onset']
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
                                imgonsetvect.append(Imgonset)
                                runvect.append(runNum)
                                Congruencyvect.append(Cong)
                                StimValvect.append(valence)
                                Actionvect.append(actiongoal)
                                TargetValvect.append(TarVal)
                                NonTargetValvect.append(NonTarVal)
                                trialNumvect.append(trialNum)
                                ordervect.append(orderNum)
                                ImgStimulitmp_1 = ImgStimuli.replace('stimuli/', '')
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

                            ### LOAD MRI Filtered_func_anat DATA
                            dataPath = "YourMainFolder/ASAP/AA_fMRI/process/results/" + sub + "/run" + run + "/" + sub + "_run" + run + "_GLM_" + myGLMModel + "_" + regtype + "_extended_allTrials.feat/" + regtype
                            fn = 'filtered_func_data_anat.nii.gz'

                            ds_name = os.path.join(dataPath, fn)
#                             print(ds_name)
                            wholebrain_data = nib.load(ds_name).get_fdata().astype(float)

                            data = wholebrain_data[mask_thres]  # indexing the ones greater than threshold

                            # append time series for each run for a certain mask
                            RunwiseTS.append(data)


                            row_means = data.mean(axis=1, keepdims=True)
                            row_stds = data.std(axis=1, keepdims=True)

                            data_z = (data - row_means) / row_stds
								

                            ### LOOP THROUGH MASK VOXELS AND TRIAL NUMBERS
                            #                             print('data shape: ' + str(data.shape))
                            for n, val in enumerate(
                                    data_z):  # looping across EACH VOXEL (i.e., 18 times (mask w 18 vox's))
                                for trial in range(24):  # 24 times, per trial in each run
                                    betas['sub'].append(sub)
                                    betas['mask'].append(str(maskName))
                                    betas['model'].append(model)
                                    # the index number of what it is  #map of the mask
                                    # gets the actual beta value for specific trial and voxel number
                                    betas['run'].append(int(run))
                                    betas['trial'].append(trial)
                                    betas['voxel'].append(n)
                                    # Get the value for each TR after image onset
                                    tronset = int(round(imgonsetvect[trial] / 1.9))
                                    betas['value_TR0'].append(val[tronset])
                                    betas['value_TR1'].append(val[tronset + 1])
                                    betas['value_TR2'].append(val[tronset + 2])
                                    betas['value_TR3'].append(val[tronset + 3])
                                    #                                     print('error here? : value_TR4' )
                                    betas['value_TR4'].append(val[tronset + 4])
                                    #                                     print('error here? : value_TR5' )
                                    betas['value_TR5'].append(val[tronset + 5])
                                    betas['value_TR6'].append(val[tronset + 6])
                                    betas['value_TR7'].append(val[tronset + 7])
                                    betas['value_TR8'].append(val[tronset + 8])
                                    betas['imgonset'].append(imgonsetvect[trial])
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

                        except:
                            print("could not open run " + run)
                    # concatenate run wise time series and put it in the dictionary for each mask.
                    # Note we are concatenate each run wise time series in the column. In this case, each row is each voxel in a certain mask and each column is a time point in the time series.
                    AllrunTS = np.concatenate(RunwiseTS, axis=1)
                    # update time series dictionary for each mask's time series of the experiment
                    TSdict[maskName] = AllrunTS
                except:
                    print("could not open data for mask " + maskName + "_" + sub + "_" + model)

            ## saving betas
            betas_dataframe = pd.DataFrame(betas)

            ### create dataframe that contain each voxels std and whole mask's std for each subject each mask each model
            stdvoxelli = []
            stdROIli = []
            subli = []
            modelli = []
            maskli = []
            voxelli = []
            for mask in masks:
                # Get the std of the whole mask
                # first average across voxels #We don't need to average for each voxel with a mask.
                # tmpROIMean = np.mean(TSdict[mask], axis=0)
                # Then get the std for the whole time series of the experiment for all voxels in a certain mask across runs.
                tmpROIstd = TSdict[mask].std()
                # loop through each voxel and Get the std of the voxel
                for rowindex, row in np.ndenumerate(TSdict[mask][:, 0]):
                    tmpVoxelstd = TSdict[mask][rowindex[0]].std()
                    stdvoxelli.append(tmpVoxelstd)
                    stdROIli.append(tmpROIstd)
                    voxelli.append(rowindex[0])
                    subli.append(sub)
                    maskli.append(mask)
                    modelli.append(model)

            df_voxelstd = pd.DataFrame(
                {"voxel": voxelli, "mask": maskli, "sub": subli, "model": modelli, "stdVoxel": stdvoxelli,
                 "stdROI": stdROIli})
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe, df_voxelstd, how='left',
                                           left_on=['voxel', 'mask', 'sub', 'model'],
                                           right_on=['voxel', 'mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['stdVoxel'] > 4 * betas_dataframe_all['stdROI']),
                (betas_dataframe_all['stdVoxel'] <= 4 * betas_dataframe_all['stdROI'])]
            choices = ["outlier", "good"]
            betas_dataframe_all['voxel_outlier_Flag'] = np.select(outlier_condition, choices, default=np.nan)

            ### trial-wise outlier flag and removal
            # first average each TR value to get a activation value per trial per ROI
            betas_dataframe_all['trialbeta'] = betas_dataframe_all.loc[:,
                                               ['value_TR0', 'value_TR1', 'value_TR2', 'value_TR3', 'value_TR4']].mean(
                axis=1)

            df_trial = betas_dataframe_all.groupby(['trial', 'mask', 'sub', 'model', 'run'], as_index=False)[
                ['value_TR0', 'value_TR1', 'value_TR2', 'value_TR3', 'value_TR4', 'trialbeta']].mean()
            df_trial.rename({'value_TR0': 'trialwise_TR0', 'value_TR1': 'trialwise_TR1', 'value_TR2': 'trialwise_TR2',
                             'value_TR3': 'trialwise_TR3', 'value_TR4': 'trialwise_TR4', 'trialbeta': 'trialwise_mean'},
                            axis=1, inplace=True)

            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_mean']].mean()
            df_trial_mean.rename({'trialwise_mean': 'Alltrialmean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_mean']].std()
            df_trial_std.rename({'trialwise_mean': 'Alltrialstd'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['trial_outlier_upper'] = df_trialoutlier_sum['Alltrialmean'] + 4 * \
                                                         df_trialoutlier_sum['Alltrialstd']
            df_trialoutlier_sum['trial_outlier_lower'] = df_trialoutlier_sum['Alltrialmean'] - 4 * \
                                                         df_trialoutlier_sum['Alltrialstd']

            df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
                                            left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum2, how='right',
                                           left_on=['trial', 'run', 'mask', 'sub', 'model'],
                                           right_on=['trial', 'run', 'mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_mean'] > betas_dataframe_all['trial_outlier_upper']),
                (betas_dataframe_all['trialwise_mean'] < betas_dataframe_all['trial_outlier_lower']),
                (betas_dataframe_all['trialwise_mean'] <= betas_dataframe_all['trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_mean'] > betas_dataframe_all['trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag'] = np.select(outlier_condition, choices, default=np.nan)

            # do it for each TR
            #TR0
            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR0']].mean()
            df_trial_mean.rename({'trialwise_TR0': 'TR0mean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR0']].std()
            df_trial_std.rename({'trialwise_TR0': 'TR0std'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['TR0trial_outlier_upper'] = df_trialoutlier_sum['TR0mean'] + 4 * \
                                                         df_trialoutlier_sum['TR0std']
            df_trialoutlier_sum['TR0trial_outlier_lower'] = df_trialoutlier_sum['TR0mean'] - 4 * \
                                                         df_trialoutlier_sum['TR0std']
            # df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
            #                                 left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum, how='right',
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_TR0'] > betas_dataframe_all['TR0trial_outlier_upper']),
                (betas_dataframe_all['trialwise_TR0'] < betas_dataframe_all['TR0trial_outlier_lower']),
                (betas_dataframe_all['trialwise_TR0'] <= betas_dataframe_all['TR0trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_TR0'] > betas_dataframe_all['TR0trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag0'] = np.select(outlier_condition, choices, default=np.nan)

            # TR1
            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR1']].mean()
            df_trial_mean.rename({'trialwise_TR1': 'TR1mean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR1']].std()
            df_trial_std.rename({'trialwise_TR1': 'TR1std'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['TR1trial_outlier_upper'] = df_trialoutlier_sum['TR1mean'] + 4 * \
                                                            df_trialoutlier_sum['TR1std']
            df_trialoutlier_sum['TR1trial_outlier_lower'] = df_trialoutlier_sum['TR1mean'] - 4 * \
                                                            df_trialoutlier_sum['TR1std']
            # df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
            #                                 left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum, how='right',
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_TR1'] > betas_dataframe_all['TR1trial_outlier_upper']),
                (betas_dataframe_all['trialwise_TR1'] < betas_dataframe_all['TR1trial_outlier_lower']),
                (betas_dataframe_all['trialwise_TR1'] <= betas_dataframe_all['TR1trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_TR1'] > betas_dataframe_all['TR1trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag1'] = np.select(outlier_condition, choices, default=np.nan)

            #TR2
            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR2']].mean()
            df_trial_mean.rename({'trialwise_TR2': 'TR2mean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR2']].std()
            df_trial_std.rename({'trialwise_TR2': 'TR2std'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['TR2trial_outlier_upper'] = df_trialoutlier_sum['TR2mean'] + 4 * \
                                                            df_trialoutlier_sum['TR2std']
            df_trialoutlier_sum['TR2trial_outlier_lower'] = df_trialoutlier_sum['TR2mean'] - 4 * \
                                                            df_trialoutlier_sum['TR2std']
            # df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
            #                                 left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum, how='right',
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_TR2'] > betas_dataframe_all['TR2trial_outlier_upper']),
                (betas_dataframe_all['trialwise_TR2'] < betas_dataframe_all['TR2trial_outlier_lower']),
                (betas_dataframe_all['trialwise_TR2'] <= betas_dataframe_all['TR2trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_TR2'] > betas_dataframe_all['TR2trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag2'] = np.select(outlier_condition, choices, default=np.nan)

            #TR3
            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR3']].mean()
            df_trial_mean.rename({'trialwise_TR3': 'TR3mean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR3']].std()
            df_trial_std.rename({'trialwise_TR3': 'TR3std'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['TR3trial_outlier_upper'] = df_trialoutlier_sum['TR3mean'] + 4 * \
                                                            df_trialoutlier_sum['TR3std']
            df_trialoutlier_sum['TR3trial_outlier_lower'] = df_trialoutlier_sum['TR3mean'] - 4 * \
                                                            df_trialoutlier_sum['TR3std']
            # df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
            #                                 left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum, how='right',
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_TR3'] > betas_dataframe_all['TR3trial_outlier_upper']),
                (betas_dataframe_all['trialwise_TR3'] < betas_dataframe_all['TR3trial_outlier_lower']),
                (betas_dataframe_all['trialwise_TR3'] <= betas_dataframe_all['TR3trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_TR3'] > betas_dataframe_all['TR3trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag3'] = np.select(outlier_condition, choices, default=np.nan)

            #TR4
            # calculate the mean and sd of the activition per mask, per sub
            df_trial_mean = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR4']].mean()
            df_trial_mean.rename({'trialwise_TR4': 'TR4mean'}, axis=1, inplace=True)
            df_trial_std = df_trial.groupby(['mask', 'sub', 'model'], as_index=False)[['trialwise_TR4']].std()
            df_trial_std.rename({'trialwise_TR4': 'TR4std'}, axis=1, inplace=True)

            # Calculate voxel sd across runs that is larger than 4sd of mean sd of that mask and flag it
            # first merge sd and mean dataframe
            df_trialoutlier_sum = pd.merge(df_trial_mean, df_trial_std, how="left",
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])

            df_trialoutlier_sum['TR4trial_outlier_upper'] = df_trialoutlier_sum['TR4mean'] + 4 * \
                                                            df_trialoutlier_sum['TR4std']
            df_trialoutlier_sum['TR4trial_outlier_lower'] = df_trialoutlier_sum['TR4mean'] - 4 * \
                                                            df_trialoutlier_sum['TR4std']
            # df_trialoutlier_sum2 = pd.merge(df_trial, df_trialoutlier_sum, how='right',
            #                                 left_on=['mask', 'sub', 'model'], right_on=['mask', 'sub', 'model'])
            # merge the sum df with the whole dataframe
            betas_dataframe_all = pd.merge(betas_dataframe_all, df_trialoutlier_sum, how='right',
                                           left_on=['mask', 'sub', 'model'],
                                           right_on=['mask', 'sub', 'model'])
            # Flag the voxel that is outlier as "outlier" and otherwise "good"
            outlier_condition = [
                (betas_dataframe_all['trialwise_TR4'] > betas_dataframe_all['TR4trial_outlier_upper']),
                (betas_dataframe_all['trialwise_TR4'] < betas_dataframe_all['TR4trial_outlier_lower']),
                (betas_dataframe_all['trialwise_TR4'] <= betas_dataframe_all['TR4trial_outlier_upper']) & (
                        betas_dataframe_all['trialwise_TR4'] > betas_dataframe_all['TR4trial_outlier_lower'])]
            choices = ["outlier", "outlier", "good"]

            betas_dataframe_all['trial_outlier_Flag4'] = np.select(outlier_condition, choices, default=np.nan)


            # save the df for flagged voxel/trial
            betas_dataframe_bad = betas_dataframe_all.loc[(betas_dataframe_all['voxel_outlier_Flag'] == 'outlier')]
            if len(betas_dataframe_bad) != 0:
#                 badmask = betas_dataframe_bad.mask.unique()
                # print(badmask)
                betas_dataframe_bad.to_csv('YourMainFolder/ASAP/AA_fMRI/process/results/TRbyTR/trialwise_matrix_New/' + sub + "_TRbyTR_trialwise_bad.csv", index=False)



            betas_dataframe_all['value_TR0_z'] = betas_dataframe_all['value_TR0']
            betas_dataframe_all['value_TR1_z'] = betas_dataframe_all['value_TR1']
            betas_dataframe_all['value_TR2_z'] = betas_dataframe_all['value_TR2']
            betas_dataframe_all['value_TR3_z'] = betas_dataframe_all['value_TR3']
            betas_dataframe_all['value_TR4_z'] = betas_dataframe_all['value_TR4']
            betas_dataframe_all['value_TR5_z'] = betas_dataframe_all['value_TR5']

            betas_dataframe_all['value_trialbeta_z'] = betas_dataframe_all['trialbeta']

            betas_dataframe_all.to_csv('YourMainFolder/ASAP/AA_fMRI/process/results/TRbyTR/trialwise_matrix/' +
                                       sub + "_TRbyTR_trialwise.csv", index=False)  # final
