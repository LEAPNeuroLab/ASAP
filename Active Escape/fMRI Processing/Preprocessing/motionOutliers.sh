#!/bin/bash-l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=20G 

cd $SLURM_SUBMIT_DIR

date
hostname
###########################################################################################################################################

#Set up the fsl environmental variables
FSLDIR=/sw/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh

export PATH=$PATH:/sw/afni/bin

#ANTs environment
export ANTSPATH=/sw/ANTs/bin
export PATH=${ANTSPATH}:$PATH

############################################################################################################################################

mot_thresh="0.5"
sub="replacesub"
run="replacerun"

###########################################################################################################################################

echo "enter run loop"

Rundir="/work/stasiak/asap/processed/${sub}/func/run${run}"
echo Rundir
if [[ ! -e $dir ]]; then
    mkdir $Rundir
fi

echo "finished run loop"
cp /work/stasiak/asap/processed/${sub}/func/${sub}_run${run}.nii.gz /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}.nii.gz
cp /work/stasiak/asap/processed/${sub}/func/SliceTime/sliceTimeOrder_run${run} /work/stasiak/asap/processed/${sub}/func/run${run}/sliceTimeOrder_run${run}.txt

echo "running fsl motion outliers" 
cd  ${Rundir}/
fsl_motion_outliers -i  /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}.nii.gz -o /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_confound.txt --fd --thresh=${mot_thresh} --dummy=0  -s /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_fd_series.txt -p /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_plot.png -v > /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_confound.txt

# in case no confounds, copy file full of zeroes
if  [ ! -f "/work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_confound.txt" ]; then
cp /work/stasiak/asap/processed/scripts/preprocess/AE_defaultConfound.txt /work/stasiak/asap/processed/${sub}/func/run${run}/${sub}_run${run}_confound.txt
fi


