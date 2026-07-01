#!/bin/bash -l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=10G
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
runs="1 2 3 4 5 6 7 8" #todo change to 1-8. 

#define the valid runs
if [ "${sub}" == "002" ];then
echo "Merge for 002"
skip=1
elif [ "${sub}" == "003" ];then
echo "Merge for 003"
skip=2
elif [ "${sub}" == "006" ];then
echo "Merge for 006"
skip=3
elif [ "${sub}" == "009" ];then
echo "Merge for 009"
skip=4
elif [ "${sub}" == "019" ];then
echo "Merge for 019"
skip=5
elif [ "${sub}" == "021" ];then
echo "Merge for 021"
skip=6
elif [ "${sub}" == "022" ];then
echo "Merge for 022"
skip=7
elif [ "${sub}" == "023" ];then
echo "Merge for 023"
skip=8
elif [ "${sub}" == "024" ];then
echo "Merge for 024"
skip=5
elif [ "${sub}" == "026" ];then
echo "Merge for 026"
skip=9
elif [ "${sub}" == "033" ];then
echo "Merge for 033"
skip=10
elif [ "${sub}" == "034" ];then
echo "Merge for 034"
skip=11
else
echo "Merge for ${sub}"
skip=0
fi


# this is only executing for GOOD RUNS based on my code ${skip} which indicates  which good runs each subject has--note the code number is uniquue for the combination of bad runs I encountered throughout the study (e.g. code 13 = runs 1,2,4 are good)
case ${skip} in
		0) runs="1 2 3 4 5 6 7 8";;
		1) runs="3 4 5 6 7 8";;
		2) runs="1 3 4 6 7 8";;
		3) runs="1 2 3 4 5 7 8";;
		4) runs="1 2 3 4 7 8";;
		5) runs="2 3 4 5 6 7 8";;		
		6) runs="1 2 3 6 8";;
		7) runs="1 2 3 4 8";;
		8) runs="1 2 4 7";;
		9) runs="1 2 3 5 7 8";;
		10) runs="1 2 3 4 5 8";;
		11) runs="1 2 3 5 6 7 8";;
esac

echo "Merge for ${sub} with ${runs}"
# This concatenates pes
myMVPAmodels="GLM_noTD_ST" #GLM_noTD  GLM_noTD_MC
models="MVPA_extended_allTrials" # MVPA MVPA_3mm MVPA_RTs_3mm #MVPA_RTs_3mm   byValence_MVPA byValence_MVPA_3mm

for model in ${models}
do
for sub in ${sub}
do
for run in  ${runs}
do 
for myMVPAmodel in ${myMVPAmodels}
do

basedir=YourMainFolder/ASAP/AA_fMRI/process/results/${sub}
funcDir=${basedir}/run${run}/${sub}_run${run}_${myMVPAmodel}_${model}.feat

outDir=${funcDir}/MVPA

cd ${outDir}
#ls ${outDir}
output="$(find  -name "pe*" -type f -exec ls -1rt "{}" + | paste -sd " ")"
fslmerge -t ${outDir}/${sub}_run_${run}_merged.nii.gz $output
echo $output
done
done
done
done

date
hostname
