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
basedir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}
finalmaskdir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks

#define the valid runs
if [ "${sub}" == "002" ];then
echo "Merge func mask for 002"

funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir3}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir6}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}

elif [ "${sub}" == "003" ];then
echo "Merge func mask for 003"

funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir1}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir6}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "006" ];then
echo "Merge func mask for 006"

funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir1}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "009" ];then
echo "Merge func maske for 009"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir1}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "019" ];then
echo "Merge func mask for 019"

funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir6}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}



elif [ "${sub}" == "021" ];then
echo "Merge func mask for 021"

funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir1}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir6}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "022" ];then
echo "Merge func mask for 022"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "023" ];then
echo "Merge func mask for 023"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}

elif [ "${sub}" == "024" ];then
echo "Merge func mask for 024"

funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir6}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "026" ];then
echo "Merge func mask for 026"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}

elif [ "${sub}" == "033" ];then
echo "Merge func mask for 033"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


elif [ "${sub}" == "034" ];then
echo "Merge func mask for 034"

funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir6}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}


else
echo "Merge func mask for ${sub}"
funcDir1=${basedir}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat
funcDir2=${basedir}/run2/${sub}_run2_${myMVPAmodel}_${model}.feat
funcDir3=${basedir}/run3/${sub}_run3_${myMVPAmodel}_${model}.feat
funcDir4=${basedir}/run4/${sub}_run4_${myMVPAmodel}_${model}.feat
funcDir5=${basedir}/run5/${sub}_run5_${myMVPAmodel}_${model}.feat
funcDir6=${basedir}/run6/${sub}_run6_${myMVPAmodel}_${model}.feat
funcDir7=${basedir}/run7/${sub}_run7_${myMVPAmodel}_${model}.feat
funcDir8=${basedir}/run8/${sub}_run8_${myMVPAmodel}_${model}.feat
regDir=${funcDir2}/reg

#create a func mask for all runs that valid voxels are present in all runs. 
fslmaths ${funcDir1}/mask.nii.gz -mul ${funcDir2}/mask.nii.gz -mul ${funcDir3}/mask.nii.gz -mul ${funcDir4}/mask.nii.gz -mul ${funcDir5}/mask.nii.gz -mul ${funcDir6}/mask.nii.gz -mul ${funcDir7}/mask.nii.gz -mul ${funcDir8}/mask.nii.gz $finalmaskdir/mask_allrunmerged.nii.gz 
#register func mask all run merged to anatomical space and keep in function resolution. 
#register func mask all run merged to anatomical space and keep in function resolution.
flirt -in $finalmaskdir/mask_allrunmerged.nii.gz -out $finalmaskdir/mask_allrunmerged_anat.nii.gz -interp nearestneighbour -ref ${regDir}/highres -applyxfm -init ${regDir}/example_func2highres.mat -applyisoxfm ${voxel}
fi


#loop through masks to create final mask
# masks="harvardoxford_Hippocampus_bin60_2mm L_harvardoxford_Hippocampus_bin60_2mm R_harvardoxford_Hippocampus_bin60_2mm FS_FPl FS_lh.L_FPl FS_rh.R_FPl FS_entorhinal_exvivo.thresh FS_rh.entorhinal_exvivo.thresh FS_lh.entorhinal_exvivo.thresh AMY_BLcx_2mm AMY_BL_2mm AMY_BM_2mm AMY_CE_2mm AMY_La_2mm Amy_50_bin L_AMY_BLcx_2mm L_AMY_BL_2mm L_AMY_BM_2mm L_AMY_CE_2mm L_AMY_La_2mm L_Amy_50_bin R_AMY_BLcx_2mm R_AMY_BL_2mm R_AMY_BM_2mm R_AMY_CE_2mm R_AMY_La_2mm R_Amy_50_bin"
masks="harvardoxford_Hippocampus_bin60_2mm FS_entorhinal_exvivo.thresh" #this is the list of your masks
for mask in $masks
do 
#multiple each mask with func mask to remove the bad voxels that is not in func mask. 
fslmaths $finalmaskdir/${mask}_anat_resampled.nii.gz -mul $finalmaskdir/mask_allrunmerged_anat.nii.gz $finalmaskdir/${mask}_anat_resampled_final.nii.gz

done
done 
done

date
hostname
