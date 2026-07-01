#!/bin/bash -l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=10G
#####################################################################################################################################
sub=replacesub
SUBJECTS_DIR=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/FS
if [ -d  $SUBJECTS_DIR ]; then
rm -r ${SUBJECTS_DIR}
fi

if [ ! -e  $SUBJECTS_DIR ]; then
mkdir ${SUBJECTS_DIR}
fi

export FREESURFER_HOME=/sw/freesurfer_7
source $FREESURFER_HOME/SetUpFreeSurfer.sh
echo $FREESURFER_HOME
export SUBJECTS_DIR=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/FS

FSLDIR=/sw/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

export PATH=$PATH:/sw/afni/bin



StrucDir="YourMainFolder/ASAP/AA_fMRI/process/sortedraw/${sub}" #contains average and denoised T1 scans. 
# refdir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/${sub}_run1_GLM_noTD_ST_MVPA_extended_allTrials.feat/reg"
refdir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1/L1.feat/reg"

#First, we need to register orignal T1 to skull striped T1, since Ants skull strip change the qform.
if [ -e $StrucDir/T1High_RPI.nii.gz ]; then
rm $StrucDir/T1High_RPI.nii.gz
rm $StrucDir/orig2highres.nii.gz
fi 
3dresample -orient RPI -inset $StrucDir/T1High.nii.gz -prefix  $StrucDir/T1High_RPI.nii.gz
flirt -in $StrucDir/T1High_RPI.nii.gz -ref $refdir/highres.nii.gz -out $StrucDir/orig2highres.nii.gz -applyxfm -usesqform

#Recon-all transfer volumetric files to surface files. This can run couple hours. 
#cd $Output
recon-all -i $StrucDir/orig2highres.nii.gz -s ${sub}_FS -all



#first step is putting the PFC atlas annot file (lh.sur_PFC_Oxford.annot) in the ./fsaverage/label/
# No need to copy, just make sure it is in the ./fsaverage/label directory. It is a projected directory from freesurfer directory.

cd $SUBJECTS_DIR
# LEFT HEMI
mri_surf2surf --srcsubject fsaverage --trgsubject ${sub}_FS --hemi lh --sval-annot ./fsaverage/label/lh.sur_PFC_Oxford.annot --tval ./${sub}_FS/label/lh.sur_PFC_Oxford_native.annot
# then getting left labels
mri_annotation2label --subject ${sub}_FS --hemi lh --annotation ./${sub}_FS/label/lh.sur_PFC_Oxford_native.annot --outdir ./${sub}_FS/label/

# RIght HEMI
mri_surf2surf --srcsubject fsaverage --trgsubject ${sub}_FS --hemi rh --sval-annot ./fsaverage/label/rh.sur_PFC_Oxford.annot --tval ./${sub}_FS/label/rh.sur_PFC_Oxford_native.annot
# then getting right labels
mri_annotation2label --subject ${sub}_FS --hemi rh --annotation ./${sub}_FS/label/rh.sur_PFC_Oxford_native.annot --outdir ./${sub}_FS/label/
# done

cd $SUBJECTS_DIR/${sub}_FS/label
#change the names make them correct for right HEMI
filenames="9 11 13 25 45 46 11m 14m 23ab 24ab 32d 44d 44v 47-12m 47-12o 6r 6v 8A 8B 8m 9-46d 9-46v CCZ FOp FPl FPm IFJ IFS M1 32pl PMd preSMA RCZa RCZp SMA"
for filename in ${filenames}
do 
mv rh.L_${filename}.label rh.R_${filename}.label
done

#####################################################################################################################################

#####################################################################################################################################

# 	THIS ONE IS FOR PFC left HEMI

# (2) getting from native surface space back to T1/nifti + NN interp + fill thresh
# subjects="002 003 004 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 035 037 038 040 041 042"
template_labels="L_9 L_11 L_13 L_25 L_45 L_46 L_11m L_14m L_23ab L_24ab L_32d L_44d L_44v L_47-12m L_47-12o L_6r L_6v L_8A L_8B L_8m L_9-46d L_9-46v L_CCZ L_FOp L_FPl L_FPm L_IFJ L_IFS L_M1 L_32pl L_PMd L_preSMA L_RCZa L_RCZp L_SMA"
#template_labels="R_9 R_11 R_13 R_25 R_45 R_46 R_11m R_14m R_23ab R_24ab R_32d R_44d R_44v R_47-12m R_47-12o R_6r R_6v R_8A R_8B R_8m R_9-46d R_9-46v R_CCZ R_FOp R_FPl R_FPm R_IFJ R_IFS R_M1 R_32pl R_PMd R_preSMA R_RCZa R_RCZp R_SMA"

# subject-specific folder with your anat-space but functional resolution masks (for that subject)!
outEPIdir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks"
if [ ! -e  $outEPIdir ]; then
mkdir $outEPIdir
fi 

#Use run1 as ref
basedir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1"

# --proj  frac .5 .5 0 looks by far the best (followed by linear interpolation to EPI). (frac 0 1 .1 is Ok when projected back to EPI w/ NN)

fsmask_dir="${SUBJECTS_DIR}/${sub}_FS/mri/masks"
if [ ! -e  $fsmask_dir ]; then
mkdir $fsmask_dir
fi 

## using identity
# cd ${SUBJECTS_DIR}
# for subj in ${subjects}
# do
for label in ${template_labels}
do
HEMI="lh"

mri_label2vol --subject ${sub}_FS --temp ${SUBJECTS_DIR}/${sub}_FS/mri/orig.mgz --label ${SUBJECTS_DIR}/${sub}_FS/label/${HEMI}.${label}.label --fillthresh .5 --identity   --hemi ${HEMI} --proj frac  .5 .5 0 --o ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}.nii.gz  

echo "resample!"
3dresample -orient RPI -inset ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}.nii.gz -prefix  ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI
cd ${SUBJECTS_DIR}/${sub}_FS/mri/masks
#3dAFNItoNIFTI  $resting+orig.BRIK  -prefix $rest_dir/$resting.nii
3dAFNItoNIFTI ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI+orig.BRIK  -prefix ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii
 
# remove AFNI format files we don't need (since we will work with nifti for a while)
rm -f *+orig.*
#rm -f $resting+*
gzip ${SUBJECTS_DIR}/${sub}_FS/mri/masks/*.nii # compress from .nii to .nii.gz

cp ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii.gz ${outEPIdir}/volume_${HEMI}.${label}_RPI.nii.gz
mv ${outEPIdir}/volume_${HEMI}.${label}_RPI.nii.gz ${outEPIdir}/FS_${HEMI}.${label}_anat.nii.gz


#for MVPA
# 3dresample  -master $basedir/${sub}_run1_GLM_noTD_ST_MVPA_extended_allTrials.feat/MVPA/pe1_anat.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled.nii.gz -input ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii.gz 
# fslmaths ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled_thres.nii.gz 

#for Featquery
3dresample  -master ${refdir}/highres.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${HEMI}.${label}_anat_highres.nii.gz -input ${outEPIdir}/FS_${HEMI}.${label}_anat.nii.gz
# binarize
fslmaths ${outEPIdir}/FS_${HEMI}.${label}_anat_highres.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${HEMI}.${label}_anat_highres_thres.nii.gz
done
# done

#####################################################################################################################################

# 	THIS ONE IS FOR PFC right HEMI
# (2) getting from native surface space back to T1/nifti + NN interp + fill thresh
# subjects="002 003 004 006 007 008 009 010 011 012 013 014 015 016 017 018 019 020 021 022 023 024 025 026 027 028 029 030 031 032 033 035 037 038 040 041 042"
# template_labels="L_9 L_11 L_13 L_25 L_45 L_46 L_11m L_14m L_23ab L_24ab L_32d L_44d L_44v L_47-12m L_47-12o L_6r L_6v L_8A L_8B L_8m L_9-46d L_9-46v L_CCZ L_FOp L_FPl L_FPm L_IFJ L_IFS L_M1 L_32pl L_PMd L_preSMA L_RCZa L_RCZp L_SMA"
template_labels="R_9 R_11 R_13 R_25 R_45 R_46 R_11m R_14m R_23ab R_24ab R_32d R_44d R_44v R_47-12m R_47-12o R_6r R_6v R_8A R_8B R_8m R_9-46d R_9-46v R_CCZ R_FOp R_FPl R_FPm R_IFJ R_IFS R_M1 R_32pl R_PMd R_preSMA R_RCZa R_RCZp R_SMA"

# subject-specific folder with your anat-space but functional resolution masks (for that subject)!
outEPIdir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks"
basedir="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/run1"

# --proj  frac .5 .5 0 looks by far the best (followed by linear interpolation to EPI). (frac 0 1 .1 is Ok when projected back to EPI w/ NN)

fsmask_dir="${SUBJECTS_DIR}/${sub}_FS/mri/masks"
if [ ! -e  $fsmask_dir ]; then
mkdir $fsmask_dir
fi 

## using identity
# cd ${SUBJECTS_DIR}
# for subj in ${subjects}
# do
for label in ${template_labels}
do

HEMI="rh"

mri_label2vol --subject ${sub}_FS --temp ${SUBJECTS_DIR}/${sub}_FS/mri/orig.mgz --label ${SUBJECTS_DIR}/${sub}_FS/label/${HEMI}.${label}.label --fillthresh .5 --identity   --hemi ${HEMI} --proj frac  .5 .5 0 --o ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}.nii.gz  

echo "resample!"
3dresample -orient RPI -inset ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}.nii.gz -prefix  ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI
cd ${SUBJECTS_DIR}/${sub}_FS/mri/masks
#3dAFNItoNIFTI  $resting+orig.BRIK  -prefix $rest_dir/$resting.nii
3dAFNItoNIFTI ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI+orig.BRIK  -prefix ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii
 
# remove AFNI format files we don't need (since we will work with nifti for a while)
rm -f *+orig.*
#rm -f $resting+*
gzip ${SUBJECTS_DIR}/${sub}_FS/mri/masks/*.nii # compress from .nii to .nii.gz

cp ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii.gz ${outEPIdir}/volume_${HEMI}.${label}_RPI.nii.gz
mv ${outEPIdir}/volume_${HEMI}.${label}_RPI.nii.gz ${outEPIdir}/FS_${HEMI}.${label}_anat.nii.gz

#for MVPA
# 3dresample  -master $basedir/${sub}_run1_GLM_noTD_ST_MVPA_extended_allTrials.feat/MVPA/pe1_anat.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled.nii.gz -input ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${HEMI}.${label}_RPI.nii.gz 
# fslmaths ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${HEMI}.${label}_anat_resampled_thres.nii.gz 

#for Featquery
3dresample  -master ${refdir}/highres.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${HEMI}.${label}_anat_highres.nii.gz -input ${outEPIdir}/FS_${HEMI}.${label}_anat.nii.gz
# binarize
fslmaths ${outEPIdir}/FS_${HEMI}.${label}_anat_highres.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${HEMI}.${label}_anat_highres_thres.nii.gz
done
# done
#####################################################################################################################################

# 	THIS ONE IS FOR left EC 
# (3) getting from native surface space back to T1/nifti + NN interp + fill thresh
template_labels="lh.entorhinal_exvivo lh.entorhinal_exvivo.thresh lh.perirhinal_exvivo lh.perirhinal_exvivo.thresh lh.V1_exvivo lh.V1_exvivo.thresh lh.BA4a_exvivo lh.BA4a_exvivo.thresh lh.BA4p_exvivo lh.BA4p_exvivo.thresh"
# template_labels="rh.entorhinal_exvivo.label rh.entorhinal_exvivo.thresh.label rh.perirhinal_exvivo.label rh.perirhinal_exvivo.thresh.label"
# --proj  frac .5 .5 0 looks by far the best (followed by linear interpolation to EPI). (frac 0 1 .1 is Ok when projected back to EPI w/ NN) 

# using identity
# cd ${SUBJECTS_DIR}
# for subj in ${subjects}
# do
for label in ${template_labels}
do

mri_label2vol --subject ${sub}_FS --temp ${SUBJECTS_DIR}/${sub}_FS/mri/orig.mgz --label ${SUBJECTS_DIR}/${sub}_FS/label/${label}.label --fillthresh .5 --identity   --hemi lh --proj frac  .5 .5 0 --o ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}.nii.gz  
# PFX Ox naming
echo "resample!"
3dresample -orient RPI -inset ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}.nii.gz -prefix  ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI
cd ${SUBJECTS_DIR}/${sub}_FS/mri/masks
#3dAFNItoNIFTI  $resting+orig.BRIK  -prefix $rest_dir/$resting.nii
3dAFNItoNIFTI ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI+orig.BRIK  -prefix ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii
 
# remove AFNI format files we don't need (since we will work with nifti for a while)
rm -f *+orig.*
#rm -f $resting+*
gzip ${SUBJECTS_DIR}/${sub}_FS/mri/masks/*.nii # compress from .nii to .nii.gz

cp ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii.gz ${outEPIdir}/volume_${label}_RPI.nii.gz
mv ${outEPIdir}/volume_${label}_RPI.nii.gz ${outEPIdir}/FS_${label}_anat.nii.gz

#for MVPA
# 3dresample  -master $basedir/${sub}_run1_GLM_noTD_ST_MVPA_extended_allTrials.feat/MVPA/pe1_anat.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${label}_anat_resampled.nii.gz -input ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii.gz    
# fslmaths ${outEPIdir}/FS_${label}_anat_resampled.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${label}_anat_resampled_thres.nii.gz

#for Featquery
3dresample  -master ${refdir}/highres.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${label}_anat_highres.nii.gz -input ${outEPIdir}/FS_${label}_anat.nii.gz
# binarize
fslmaths ${outEPIdir}/FS_${label}_anat_highres.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${label}_anat_highres_thres.nii.gz
done

#####################################################################################################################################

# 	THIS ONE IS FOR right EC 
# (3) getting from native surface space back to T1/nifti + NN interp + fill thresh
template_labels="rh.entorhinal_exvivo rh.entorhinal_exvivo.thresh rh.perirhinal_exvivo rh.perirhinal_exvivo.thresh rh.V1_exvivo rh.V1_exvivo.thresh rh.BA4a_exvivo rh.BA4a_exvivo.thresh rh.BA4p_exvivo rh.BA4p_exvivo.thresh"
# template_labels="rh.entorhinal_exvivo.label rh.entorhinal_exvivo.thresh.label rh.perirhinal_exvivo.label rh.perirhinal_exvivo.thresh.label"
# --proj  frac .5 .5 0 looks by far the best (followed by linear interpolation to EPI). (frac 0 1 .1 is Ok when projected back to EPI w/ NN) 

# using identity
# cd ${SUBJECTS_DIR}
# for subj in ${subjects}
# do
for label in ${template_labels}
do

mri_label2vol --subject ${sub}_FS --temp ${SUBJECTS_DIR}/${sub}_FS/mri/orig.mgz --label ${SUBJECTS_DIR}/${sub}_FS/label/${label}.label --fillthresh .5 --identity   --hemi rh --proj frac  .5 .5 0 --o ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}.nii.gz  
# PFX Ox naming
echo "resample!"
3dresample -orient RPI -inset ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}.nii.gz -prefix  ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI
cd ${SUBJECTS_DIR}/${sub}_FS/mri/masks
#3dAFNItoNIFTI  $resting+orig.BRIK  -prefix $rest_dir/$resting.nii
3dAFNItoNIFTI ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI+orig.BRIK  -prefix ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii
 
# remove AFNI format files we don't need (since we will work with nifti for a while)
rm -f *+orig.*
#rm -f $resting+*
gzip ${SUBJECTS_DIR}/${sub}_FS/mri/masks/*.nii # compress from .nii to .nii.gz

cp ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii.gz ${outEPIdir}/volume_${label}_RPI.nii.gz
mv ${outEPIdir}/volume_${label}_RPI.nii.gz ${outEPIdir}/FS_${label}_anat.nii.gz

#For MVPA
# 3dresample  -master $basedir/${sub}_run1_GLM_noTD_ST_MVPA_extended_allTrials.feat/MVPA/pe1_anat.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${label}_anat_resampled.nii.gz -input ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}_RPI.nii.gz    
# # flirt -in ${SUBJECTS_DIR}/${sub}_FS/mri/masks/volume_${label}.nii.gz -applyxfm -init ident.mat -out ${outEPIdir}/FS_${label}_anat_resampled.nii.gz -paddingsize 0.0 -interp nearestneighbour -ref  $basedir/${sub}_01_mask_total_fsl.nii.gz
# fslmaths ${outEPIdir}/FS_${label}_anat_resampled.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${label}_anat_resampled_thres.nii.gz

#for Featquery
3dresample  -master ${refdir}/highres.nii.gz  -rmode Li -prefix ${outEPIdir}/FS_${label}_anat_highres.nii.gz -input ${outEPIdir}/FS_${label}_anat.nii.gz
# binarize
fslmaths ${outEPIdir}/FS_${label}_anat_highres.nii.gz -thr 0.0 -bin ${outEPIdir}/FS_${label}_anat_highres_thres.nii.gz
done
date