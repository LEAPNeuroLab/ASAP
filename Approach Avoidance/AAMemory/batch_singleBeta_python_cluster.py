#!/usr/bin/env python
# coding: utf-8

import os 
import os.path
import time
import random
import sys
from math import *
import csv
import fnmatch
import re
from shutil import copyfile

import numpy
import numpy as np

#function for multiple replacements given a dictionary
# and the text in which you wish replacements to occur
def multiple_replace(dict, text):
    #create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)
# sub=sys.argv[1]
# TMS=sys.argv[2]
# dir=sys.argv[3]
# procDataDir=sys.argv[4]
# myTR=sys.argv[5]
# myVolumes=sys.argv[6]
# run=sys.argv[7]
subjects = ["PutYourSubjectsHere"]
runs = ["1", "2", "3", "4", "5", "6", "7", "8"]
procDataDir="YourMainFolder/ASAP/AA_fMRI/process/TimeFiles" #todo
fsfoutDir="YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/fsffiles/" #todo
sub002run = ["1", "2", "3", "4", "5", "6"]
for sub in subjects:
    for run in runs:
        if sub=="002" and run in sub002run:
            myVolumes = 138
        else:
            myVolumes = 133

        myTR=1.900000
        myHighPassFilter=100

        inDir=procDataDir + "/" + sub + "/singleBetas_full/" #n=24*8 text files since n=192 trials of interest
        print (inDir)

        # count number of files in single_beta folder for that run
        fn=sub+ '_run' + run + '_*.txt'
        TOTALCOUNT = len(fnmatch.filter(os.listdir(inDir), fn))
        # print 'totalcount' + str(TOTALCOUNT)
        # EV count
        totalEVs = TOTALCOUNT + 2 # gray screen and instructions in additional to each trial
        EVsrealNum = TOTALCOUNT + 2
        #GLM output dir
        outputdir="YourMainFolder/ASAP/AA_fMRI/process/results" #todo change

        #template fsf location #todo
        inFileName = "YourMainFolder/ASAP/AA_fMRI/process/scripts/MVPA/1stLevel_GLM_noTD_MVPA_extended.fsf"

        outFiledir = fsfoutDir + sub
        try:
            os.stat(outFiledir)
        except:
            os.mkdir(outFiledir)
        outFileName = os.path.join(outFiledir, sub + "_run" + run + "_1stLevel_GLM_noTD_MVPA_extended.fsf")


        #replacements dictionary as input to multiple_replace()
        replacements = {
            "&&EVSORIG&&" : str(totalEVs),
            "&&EVSREAL&&" : str(EVsrealNum),
            "SUBID" : sub,
            "@" : run,
            "myTR" : str(myTR),
            "myVolumes" : str(myVolumes),
            "myHighPassFilter" : str(myHighPassFilter),
            "outputdirreplace" : outputdir,
            #changed name to extended here
            "MVPA_3mm": "MVPA_extended_allTrials"
        }

        #actually conducting replacements from inFile to outFile
        with open(inFileName, "r") as inFile:
            lines = inFile.readlines()
        with open(outFileName, "w") as outFile:
            for line in lines:
                outFile.write(multiple_replace(replacements, line))
        # appending text for each EV
        for EVIND in range(TOTALCOUNT+2):
            print (EVIND)
            EVINDEX = str(EVIND + 1)
            print(EVINDEX)
            tmpcount=TOTALCOUNT+1
            if int(EVINDEX) < tmpcount:
                f = open(outFileName, "a")
                f.write('\n# EV ' + EVINDEX +' title\n'
                        'set fmri(evtitle' + EVINDEX +') "trial' + str(EVIND+1) + '"' + '\n\n'
                        '# Basic waveform shape (EV ' + EVINDEX + ')\n'
                        '# 0 : Square\n'
                        '# 1 : Sinusoid\n'
                        '# 2 : Custom (1 entry per volume)\n'
                        '# 3 : Custom (3 column format)\n'
                        '# 4 : Interaction\n'
                        '# 10 : Empty (all zeros)\n'
                        'set fmri(shape' + EVINDEX + ') 3\n\n'
                        '# Convolution (EV '+EVINDEX+')\n'
                        '# 0 : None\n'
                        '# 1 : Gaussian\n'
                        '# 2 : Gamma\n'
                        '# 3 : Double-Gamma HRF\n'
                        '# 4 : Gamma basis functions\n'
                        '# 5 : Sine basis functions\n'
                        '# 6 : FIR basis functions\n'
                        'set fmri(convolve'+EVINDEX+') 3\n\n'
                        '# Convolve phase (EV '+EVINDEX + ')\n'
                        'set fmri(convolve_phase'+EVINDEX+') 0\n\n'
                        '# Apply temporal filtering (EV '+EVINDEX+') \n'
                        'set fmri(tempfilt_yn'+ EVINDEX + ') 1\n\n'
                        '# Add temporal derivative (EV '+EVINDEX +') \n'
                        'set fmri(deriv_yn' + EVINDEX + ') 0 \n\n'
                        '# Custom EV file (EV ' + EVINDEX + ')\n'
                        'set fmri(custom'+ EVINDEX + ') "YourMainFolder/ASAP/AA_fMRI/process/TimeFiles/'+ sub + '/singleBetas_full/' + sub + '_run' + run + '_' + str(EVIND+1) + '.txt"\n\n') #todo
                f.close()
                print("hi I closed the file")
                for dec in range(totalEVs + 1):
                    f = open(outFileName, "a")
                    f.write('# Orthogonalise EV ' + EVINDEX + ' wrt EV ' + str(dec) +'\n'
                            'set fmri(ortho' + EVINDEX + '.' + str(dec) + ') 0\n\n')
                    f.close()
            elif int(EVINDEX) == tmpcount:
                f = open(outFileName, "a")
                f.write('\n# EV ' + EVINDEX +' title\n'
                        'set fmri(evtitle' + EVINDEX + ') "GrayScreen' + str(EVIND + 1) + '"' + '\n\n'
                        '# Basic waveform shape (EV ' + EVINDEX + ')\n'
                        '# 0 : Square\n'
                        '# 1 : Sinusoid\n'
                        '# 2 : Custom (1 entry per volume)\n'
                        '# 3 : Custom (3 column format)\n'
                        '# 4 : Interaction\n'
                        '# 10 : Empty (all zeros)\n'
                        'set fmri(shape' + EVINDEX + ') 3\n\n'
                        '# Convolution (EV ' + EVINDEX + ')\n'
                        '# 0 : None\n'
                        '# 1 : Gaussian\n'
                        '# 2 : Gamma\n'
                        '# 3 : Double-Gamma HRF\n'
                        '# 4 : Gamma basis functions\n'
                        '# 5 : Sine basis functions\n'
                        '# 6 : FIR basis functions\n'
                        'set fmri(convolve' + EVINDEX + ') 3\n\n'
                        '# Convolve phase (EV ' + EVINDEX + ')\n'
                        'set fmri(convolve_phase' + EVINDEX + ') 0\n\n'
                        '# Apply temporal filtering (EV ' + EVINDEX + ') \n'
                        'set fmri(tempfilt_yn' + EVINDEX + ') 1\n\n'
                        '# Add temporal derivative (EV ' + EVINDEX + ') \n'
                        'set fmri(deriv_yn' + EVINDEX + ') 0 \n\n'
                        '# Custom EV file (EV ' + EVINDEX + ')\n'
                        'set fmri(custom' + EVINDEX + ') "YourMainFolder/ASAP/AA_fMRI/process/TimeFiles/'+ sub + '/' + 'GrayScreen' + run + '.txt"\n\n')  # todo
                f.close()
                print("hi I closed the file")
                for dec in range(totalEVs + 1):
                    f = open(outFileName, "a")
                    f.write('# Orthogonalise EV ' + EVINDEX + ' wrt EV ' + str(dec) +'\n'
                            'set fmri(ortho' + EVINDEX + '.' + str(dec) + ') 0\n\n')
                    f.close()
            else:
                f = open(outFileName, "a")
                f.write('\n# EV ' + EVINDEX +' title\n'
                        'set fmri(evtitle' + EVINDEX + ') "Instruction' + str(EVIND + 1) + '"' + '\n\n'
                        '# Basic waveform shape (EV ' + EVINDEX + ')\n'
                        '# 0 : Square\n'
                        '# 1 : Sinusoid\n'
                        '# 2 : Custom (1 entry per volume)\n'
                        '# 3 : Custom (3 column format)\n'
                        '# 4 : Interaction\n'
                        '# 10 : Empty (all zeros)\n'
                        'set fmri(shape' + EVINDEX + ') 3\n\n'
                        '# Convolution (EV ' + EVINDEX + ')\n'
                        '# 0 : None\n'
                        '# 1 : Gaussian\n'
                        '# 2 : Gamma\n'
                        '# 3 : Double-Gamma HRF\n'
                        '# 4 : Gamma basis functions\n'
                        '# 5 : Sine basis functions\n'
                        '# 6 : FIR basis functions\n'
                        'set fmri(convolve' + EVINDEX + ') 3\n\n'
                        '# Convolve phase (EV ' + EVINDEX + ')\n'
                        'set fmri(convolve_phase' + EVINDEX + ') 0\n\n'
                        '# Apply temporal filtering (EV ' + EVINDEX + ') \n'
                        'set fmri(tempfilt_yn' + EVINDEX + ') 1\n\n'
                        '# Add temporal derivative (EV ' + EVINDEX + ') \n'
                        'set fmri(deriv_yn' + EVINDEX + ') 0 \n\n'
                        '# Custom EV file (EV ' + EVINDEX + ')\n'
                        'set fmri(custom' + EVINDEX + ') "YourMainFolder/ASAP/AA_fMRI/process/TimeFiles/'+ sub + '/' + 'Instruction' + run + '.txt"\n\n')  # todo
                f.close()
                print ("hi I closed the file")
                for dec in range(totalEVs + 1):
                    f = open(outFileName, "a")
                    f.write('# Orthogonalise EV ' + EVINDEX + ' wrt EV ' + str(dec) +'\n'
                            'set fmri(ortho' + EVINDEX + '.' + str(dec) + ') 0\n\n')
                    f.close()


        # Contrast & F-tests mode
        f = open(outFileName, "a")
        f.write('# Contrast & F-tests mode\n'
            '# real : control real EVs\n'
            '# orig : control original EVs\n'
            'set fmri(con_mode_old) orig\n'
            'set fmri(con_mode) orig\n'
            'set fmri(conpic_real.1) 1\n'
            'set fmri(conname_real.1) "Test"\n'
            'set fmri(con_real1.1) 1\n'
            'set fmri(conpic_orig.1) 1\n'
            'set fmri(conname_orig.1) "Test"\n'
            'set fmri(con_orig1.1) 1\n'
            'set fmri(con_real1.1) 1\n'
            'set fmri(conmask_zerothresh_yn) 0\n'
            'set fmri(conmask1_1) 0)\n')
        f.close()
        for dec in range(2, totalEVs + 1):
            f = open(outFileName, "a")
            f.write('set fmri(con_real1.' + str(dec) + ') 0\n'
                'set fmri(con_orig1.' + str(dec) + ') 0\n')
            f.close()
