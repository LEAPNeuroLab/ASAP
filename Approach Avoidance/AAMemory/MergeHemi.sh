#!/bin/bash -l
#SBATCH --nodes=1 --ntasks-per-node=1
#SBATCH --mem=10G
cd $SLURM_SUBMIT_DIR

date
hostname

export PATH=$PATH:/sw/afni/bin

FSLDIR=/sw/fsl
. ${FSLDIR}/etc/fslconf/fsl.sh
PATH=${FSLDIR}/bin:${PATH}
export FSLDIR PATH

subjects="002 003 004 005 006 007 008 009 010 012 013 014 017 019 020 021 022 023 024 025 026 027 029 030 031 032 033 034 035 036 037 038 039 040 041 042 043 044 045 046 047 048 049 050 051 053 054 055 056 057 058 059 060 061 062 063 064 065 066 069 072 073 068 067 070 071"
masks3="perirhinal_exvivo perirhinal_exvivo.thresh" #This is the list of your masks
# masks1="AMY_AAA_2mm AMY_ATA_2mm AMY_ATA_ASTA_2mm AMY_BL_BLV_2mm AMY_BLN_BL_BLD+BLI_2mm AMY_BLN_BM_2mm AMY_BLN_La_2mm AMY_CEN_2mm AMY_CMN_2mm"
# masks2="9 11 13 25 45 46 11m 14m 23ab 24ab 32d 44d 44v 47-12m 47-12o 6r 6v 8A 8B 8m 9-46d 9-46v CCZ FOp FPl FPm IFJ IFS M1 32pl PMd preSMA RCZa RCZp SMA"
# masks3="entorhinal_exvivo entorhinal_exvivo.thresh perirhinal_exvivo perirhinal_exvivo.thresh V1_exvivo V1_exvivo.thresh BA4a_exvivo BA4a_exvivo.thresh BA4p_exvivo BA4p_exvivo.thresh"
# masks4="CA1 CA2+3 DG ERC PHC PRC SUB HPC aHPC pHPC"
namefix="anat_highres_thres.nii.gz"

for sub in $subjects
do
final="YourMainFolder/ASAP/AA_fMRI/process/results/${sub}/finalmasks"


for FSmaskMTL in $masks3
do
fslmaths ${final}/FS_lh.${FSmaskMTL}_${namefix} -add ${final}/FS_rh.${FSmaskMTL}_${namefix} ${final}/tmp_FS_${FSmaskMTL}_${namefix}
fslmaths ${final}/tmp_FS_${FSmaskMTL}_${namefix} -thr 0.0 -bin ${final}/FS_${FSmaskMTL}_${namefix}
rm ${final}/tmp_FS_${FSmaskMTL}_${namefix}
done

done

date
hostname