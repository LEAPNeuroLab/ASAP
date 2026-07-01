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

fsf_dir="YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/fsffiles"

sub=replacesub
run=replacerun

# # running RS preproc
echo "Running feat model"
feat $fsf_dir/$sub/${sub}_run${run}_1stLevel_GLM_noTD_MVPA_extended.fsf 
done

date
hostname