#!/bin/bash -l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=20G
cd $SLURM_SUBMIT_DIR

date
hostname
###########################################################################################################################################

#Set up the environmental variables
FSLDIR=/sw/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

export PATH=$PATH:/sw/afni/bin

export ANTSPATH=/sw/ANTs/bin
export PATH=${ANTSPATH}:$PATH
############################################################################################################################################
sub=replacesub
voxel=2.5 #change to your scan resolution
models="MVPA_extended_allTrials" #MVPA_3mm MVPA_3mm_tstat "MVPA  MVPA_RTs_3mm  MVPA_3mm_allTrials MVPA_3mm_allTrials_FIR
MNImaskDir=/home/jingyi/MNI_atlases

for model in ${models}
do
myMVPAmodels="GLM_noTD_ST" 

for myMVPAmodel in ${myMVPAmodels}
do

for run in 1 2 3 4 5 6 7 8
do 

basedir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run${run}
funcDir=${basedir}/${sub}_run${run}_${myMVPAmodel}_${model}.feat
standard="/sw/fsl/data/standard/MNI152_T1_2mm_brain"

regDir=${funcDir}/reg
statsDir=${funcDir}/stats
outDir=${funcDir}/MVPA

# create processed directory if it doesn't exist
if [ ! -e  $outDir ]; then
mkdir ${outDir}
fi

# FIRST, let's register the single beta files to structural
###  how many YOU CARE ABOUT!!!!! 
TOTALCOUNT=24 # This is your EV of interest 
echo ${statsDir}
cd ${statsDir}/
echo hello1
for((peNum=1;peNum<=${TOTALCOUNT};peNum=peNum+1)) do
   echo hello2
   echo $peNum
	# # applying examplefun2highres matrix but forcing the resampling to be a particular voxel size that is our functional native resolution (eg 2.5 mm). 
	flirt -in ${statsDir}/pe${peNum}.nii.gz -out ${outDir}/tmp_pe${peNum}_anat.nii.gz -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel} 
done

# this one is for a spatial pre-whitening step
flirt -in ${statsDir}/res4d.nii.gz -out ${outDir}/res4d_anat.nii.gz -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel} 

# if you want to create a 'wholebrain' functional mask
flirt -in ${regDir}/example_func2highres.nii.gz -applyxfm -init /home/jingyi/essentialfiles/ident.mat -out ${outDir}/wholebrain_func_anat_resampled -paddingsize 0.0 -interp trilinear -ref ${outDir}/pe1_anat.nii.gz
 
done # run level
#############################################################################################################################################
#now let's apply our NONLINEAR MNI--> T1 matrix transgorm to mask image
#Use run1 as ref
MaskregDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat/reg
finalmaskDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks
peDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat/MVPA
# create processed directory if it doesn't exist
if [ ! -e  $finalmaskDir ]; then
mkdir ${finalmaskDir}
fi
#### compute invert warp; only needs to be done once per subject
echo "invwarp"
invwarp --ref=${MaskregDir}/highres.nii.gz  --warp=${MaskregDir}/highres2standard_warp.nii.gz --out=${MaskregDir}/standard2highres_warp.nii.gz 

#masks="conj_BA46_946D_25_L MFG_25_bin  LAmy_50_bin RAmy_50_bin Amy_50_bin LPFC_eimemri  AMY_CE AMY_BL L_11m L_11 L_13 L_14m L_23ab L_24ab L_25 L_32d L_32pl L_44d L_44v L_45 L_46 L_47-12m L_47-12o L_47-12s L_6r L_6v L_8A L_8B L_8m L_9-46d L_9-46v L_9 L_CCZ L_FPl L_FPm L_IFJ L_IFS L_M1 L_PMd L_preSMA L_RCZa L_RCZp L_SMA R_11m R_11 R_13 R_14m R_23ab R_24ab R_25 R_32d R_32pl R_44d R_44v R_45 R_46 R_47-12m R_47-12o R_47-12s R_6r R_6v R_8A R_8B R_8m R_9-46d R_9-46v R_9 R_CCZ R_FPl R_FPm R_IFJ R_IFS R_M1 R_PMd R_preSMA R_RCZa R_RCZp R_SMA 11m 11 13 14m 23ab 24ab 25 32d 32pl 44d 44v 45 46 47-12m 47-12o 47-12s 6r 6v 8A 8B 8m 9-46d 9-46v 9 CCZ FPl FPm IFJ IFS M1 PMd preSMA RCZa RCZp SMA L_RCZ R_RCZ L_32 R_32 32 RCZ"
masks="Amy_50_bin AMY_BL_2mm AMY_BLcx_2mm AMY_BM_2mm AMY_CE_2mm AMY_La_2mm harvardoxford_Hippocampus_bin60_2mm"


for mask in  ${masks} # 32 11m 11 13 14m 23ab 24ab 25 32d 32pl 44d 44v 45 46 47-12m 47-12o 47-12s 6r 6v 8A 8B 8m 9-46d 9-46v 9 CCZ FPl FPm IFJ IFS M1 PMd preSMA RCZa RCZp SMA badre_FPC_CL2_6mm badre_MidDLPFC_CL4_6mm badre_PMd_CL9_6mm badre_PrePMd_CL6_6mm huettel_DL_1_CL9_6mm huettel_DL_2_CL8_6mm huettel_DL_3_CL7_6mm huettel_DL_4_CL5_6mm huettel_DL_5_CL2_6mm huettel_DL_6_CL1_6mm L_11m L_11 L_13 L_14m L_23ab L_24ab L_25 L_32d L_32pl L_44d L_44v L_45 L_46 L_47-12m L_47-12o L_47-12s L_6r L_6v L_8A L_8B L_8m L_9-46d L_9-46v L_9 L_CCZ L_FPl L_FPm L_IFJ L_IFS L_M1 L_PMd L_preSMA L_RCZa L_RCZp L_SMA R_11m R_11 R_13 R_14m R_23ab R_24ab R_25 R_32d R_32pl R_44d R_44v R_45 R_46 R_47-12m R_47-12o R_47-12s R_6r R_6v R_8A R_8B R_8m R_9-46d R_9-46v R_9 R_CCZ R_FPl R_FPm R_IFJ R_IFS R_M1 R_PMd R_preSMA R_RCZa R_RCZp R_SMA R_RCZ L_RCZ RCZ L_32 R_32     #Oxford_PFC_unthresh_2mm_4D  #badre_FPC_CL2_6mm badre_MidDLPFC_CL4_6mm badre_PMd_CL9_6mm badre_PrePMd_CL6_6mm huettel_DL_1_CL9_6mm huettel_DL_2_CL8_6mm huettel_DL_3_CL7_6mm huettel_DL_4_CL5_6mm huettel_DL_5_CL2_6mm huettel_DL_6_CL1_6mm  #.nii.gz #fat_sallet #sallet_2mm_4D neubert_ventral_2mm_4D #neubert_cinguloOFC_2mm_4D Yeo_400_2mm_4D #conj_BA46_946D_25_L r_ifs l_aifs l_pifs BA32 IFS_25_R IFS_25_L IC_25_R IC_25_L FPl_R FPl_L BA9_46V_25_R BA9_46V_25_L BA46_25_R BA46_25_L BA9_46D_25_R BA9_46D_25_L BA25 BA24 FM_25_bin FPm_25_bin FPl_25_bin BA9_25    BA9_46V_25    BA9_46D_25  BA9_46D_25 IC_50_bin CG_50_bin STGp_50_bin STGa_50_bin FP_50_bin R_Tha_50_bin L_Tha_50_bin L_IFG R_IFG Amy_50_bin Mask_Ce_2mmDilated_Right LAmy_50_bin RAmy_50_bin LO_50 IFS_25  LPFC_eimemri dmPFC_eimemri TO_50_bin   BA10_25 MFG_25_bin MFG_25_bin_L  MFG_25_bin_R ##MNI_frontalLobe_Insula 
do
echo ${mask}
applywarp --ref=${MaskregDir}/highres.nii.gz --in=${MNImaskDir}/${mask}.nii.gz --warp=${MaskregDir}/standard2highres_warp.nii.gz  --out=${finalmaskDir}/${mask}_anat.nii.gz --interp=nn # using nonlinear, need to inwarp first, above (comp. intensive)
# getting it to the same resolution as your func.
# flirt -in ${finalmaskDir}/${mask}_anat.nii.gz -applyxfm -init /home/jingyi/essentialfiles/ident.mat -out ${finalmaskDir}/${mask}_anat_resampled.nii.gz -paddingsize 0.0 -interp nearestneighbour -ref  ${MaskregDir}/example_func.nii.gz #Get it with the func resolution
3dresample  -master ${peDir}/pe1_anat.nii.gz  -rmode Li -prefix ${finalmaskDir}/${mask}_anat_resampled.nii.gz -input ${finalmaskDir}/${mask}_anat.nii.gz 
fslmaths ${finalmaskDir}/${mask}_anat_resampled.nii.gz -thr 0.9 -bin ${finalmaskDir}/${mask}_anat_resampled_thres.nii.gz
done # mask level

done # myMVPAmodel level
done # model
