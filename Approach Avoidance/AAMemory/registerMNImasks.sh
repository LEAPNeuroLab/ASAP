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
#now let's apply our NONLINEAR MNI--> T1 matrix transgorm to mask image
#Use run1 as ref
MaskregDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat/reg
peDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/${sub}_run1_${myMVPAmodel}_${model}.feat/MVPA
finalmaskDir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks
# create processed directory if it doesn't exist
if [ ! -e  $finalmaskDir ]; then
mkdir ${finalmaskDir}
fi
#remove processed files
#Use with caution!!!!
rm ${finalmaskDir}/*_anat.nii.gz
rm ${finalmaskDir}/*_anat_resampled.nii.gz
#### compute invert warp; only needs to be done once per subject
echo "invwarp"
invwarp --ref=${MaskregDir}/highres.nii.gz  --warp=${MaskregDir}/highres2standard_warp.nii.gz --out=${MaskregDir}/standard2highres_warp.nii.gz 

masks="Amy_50_bin harvardoxford_Hippocampus_bin60_2mm"


for mask in  ${masks}  
do
echo ${mask}
applywarp --ref=${MaskregDir}/highres.nii.gz --in=${MNImaskDir}/${mask}.nii.gz --warp=${MaskregDir}/standard2highres_warp.nii.gz  --out=${finalmaskDir}/${mask}_anat.nii.gz --interp=nn # using nonlinear, need to inwarp first, above (comp. intensive)
# getting it to the same resolution as your func.
# flirt -in ${finalmaskDir}/${mask}_anat.nii.gz -applyxfm -init /home/jingyi/essentialfiles/ident.mat -out ${finalmaskDir}/${mask}_anat_resampled.nii.gz -paddingsize 0.0 -interp nearestneighbour -ref  ${MaskregDir}/example_func.nii.gz #Get it with the func resolution
3dresample  -master ${peDir}/pe1_anat.nii.gz  -rmode Li -prefix ${finalmaskDir}/${mask}_anat_resampled.nii.gz -input ${finalmaskDir}/${mask}_anat.nii.gz 
fslmaths ${finalmaskDir}/${mask}_anat_resampled.nii.gz -thr 0.9 -bin ${finalmaskDir}/${mask}_anat_resampled_thres.nii.gz
done # mask level
done
done

