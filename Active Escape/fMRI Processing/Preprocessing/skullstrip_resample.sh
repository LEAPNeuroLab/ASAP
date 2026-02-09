#!/bin/bash -l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=10G 

cd $SLURM_SUBMIT_DIR

date
hostname
###########################################################################################################################################

#Set up the fsl environmental variables
FSLDIR=/sw/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh 
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

export PATH=$PATH:/sw/afni/bin

#ANTs environment
export ANTSPATH=/sw/ANTs/bin
export PATH=${ANTSPATH}:$PATH
############################################################################################################################################


sub="replacesub"
AntsTemplateDir="/home/stasiak/Ants_templates"
###########################################################################################################################################
echo "Ants skull strip"

antsBrainExtraction.sh -d 3 -a /work/stasiak/asap/processed/${sub}/anat/T1High.nii.gz -e $AntsTemplateDir/T_template0.nii.gz -m $AntsTemplateDir/T_template0_BrainCerebellumProbabilityMask.nii.gz -f $AntsTemplateDir/T_template0_BrainCerebellumRegistrationMask.nii.gz -o /work/stasiak/asap/processed/${sub}/anat/T1_
echo "finished skullstrip T1"

mv /work/stasiak/asap/processed/${sub}/anat/T1_BrainExtractionBrain.nii.gz /work/stasiak/asap/processed/${sub}/anat/T1_brain_tmp.nii.gz
mv /work/stasiak/asap/processed/${sub}/anat/T1_BrainExtractionMask.nii.gz /work/stasiak/asap/processed/${sub}/anat/T1_BrainMask.nii.gz


echo "reorient T1 high"
3dresample -orient RPI -inset /work/stasiak/asap/processed/${sub}/anat/T1_brain_tmp.nii.gz -prefix /work/stasiak/asap/processed/${sub}/anat/T1_brain.nii.gz
rm /work/stasiak/asap/processed/${sub}/anat/T1_brain_tmp.nii.gz

#done

date
hostname
