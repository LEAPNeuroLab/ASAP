**Author:** Jingyi Wang, PhD (wangjingyimayer@gmail.com)

This pipeline calculates three neural metrics (between-trial pattern correlation, within-trial pattern correlation, and trial-wise univariate activity) and computes the relationship between these three neural metrics with amygdala activation and temporal memory accuracy. The "masks" folder contains all the MNI masks and Freesurfer labels used in the current study. The "ImgStimlist.txt" contains the list of image names included in the current study, from the IAPS and OASIS datasets. Detailed descriptions of each processing script, as well as the steps for properly using each script, can be found below:

## Sort behavioral data

**Step 1:** Run the "SortBevData_aa.py" script in Python. This script sorts each participant's raw Psychopy data from the fMRI task into csv files.

**Step 2:** Run the "SortBevData_CoraseTemp.py" script in Python. This script sorts each participant's raw Psychopy data from the post-task into csv files.

## Preprocessing neural data

**Step 1:** Run the "createSingles_cluster.py" script in Python. This script takes the sorted behavioral data and produces the time files (i.e., three column txt files) for later FSL processing.

**Step 2:** Run the "batch_singleBeta_python_cluster.py" script in Python. This script creates FSL FEAT processing .fsf files for single-trial GLM analyses, based on the template file "1stLevel_GLM_noTD_MVPA_extended.fsf".

**Step 3:** Run the "batch_singleBeta_python_cluster_run.sh" script as a Bash command. This script performs the FEAT processing using the .fsf files created in Step 2.

**Step 4:** Run the "registerSingleBeta_FSL_allTrials.sh" script as a Bash command. This script registers the trial-wise beta from functional space to subject space.

**Step 5:** Run the "mergePEs.sh" script as a Bash command. This script merges each parameter estimate (PE) in the subject space from each trial (from Step 4) into one 4D NIfTI file.

## Create masks in functional resolution anatomical space

**Cortical masks:**

**Step 1:** Run the "Freesurfer_atlasAA.sh" script as a Bash command. This script transfers surface masks in the FreeSurfer atlas into each subject's volumetric space.

**Step 2:** Run the "MergeHemi.sh" script as a Bash command. This script merges masks from the left and right hemispheres into one bilateral mask.

**Subcortical masks:**

**Step 1:** Run the "registerMNImasks.sh" script as a Bash command. This script registers MNI masks from the Harvard-Oxford subcortical structural atlas into functional-resolution anatomical space masks.

After both cortical and subcortical volumetric masks are ready, run the "createfinalmasks.sh" script as a Bash command. This script ensures that all the final masks contain only valid voxels in the functional scans.

## Between-trial pattern correlation

**Step 1:** Run the "nilearn_extractBetas_trialanalysis_AA_cluster.py" script in Python. This script extracts voxel-wise and trial-wise beta values from each participant within given ROIs. To run this script, one needs to make sure all the masks were registered to subject space and functional resolution.

**Step 2:** Run the "inv_covariance_AA_cluster.py" script in Python. This script applies multivariate noise normalization to the PE in order to reduce nuisance correlations between voxels caused by physiological and instrumental noise.

**Step 3:** Run the "nilearn_doRSA_whitened_trialwise_byMask_AA_cluster.py" script in Python. This script calculates the pattern correlation within a given ROI between adjacent trials.

## Within-trial pattern correlation

**Step 1:** Run the "nilearn_TRbyTR_trialanalysis_AA_cluster.py" script in Python. This script extracts trial-wise and voxel-wise activity at each TR within each a-priori ROI, which were then z-scored per voxel, run, and participant.

**Step 2:** Run the "nilearn_doRSA_TRbyTR_trialwise_byMask_AA_cluster.py" script in Python. This script calculates the pattern correlation within a given ROI between adjacent TR within a trial.

## Trial-wise univariate activity

**Step 1:** Run the "Get_trialwise_AA_cluster.py" script in Python. This script estimates univariate activation by averaging the trial-wise and voxel-wise PE within each trial and each ROI (i.e., results from between-trial pattern correlation in Step 2).

## Neural behavioral analyzing scripts

The scripts below are all written for R:

- The "AAfMRI_CoarseMem_overall_upload.Rmd" script calculates overall temporal memory accuracy using permutation tests.
- The "AAfMRI_Bev_uniPRC_Within-trialPC_upload.Rmd" script computes the relationship between temporal memory accuracy and univariate activations within each ROI.
- The "AAfMRI_Between-trialPC_upload.Rmd" script computes the temporal memory accuracy and between-trial correlation within each ROI.
- The "AAfMRI_Mediation_upload.Rmd" script conducts the mediation tests.
