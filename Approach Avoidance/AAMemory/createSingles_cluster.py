#!/usr/bin/env python
# coding: utf-8
# prepare text files for fmri analysis

import time
import random
import os
# import serial, ctypes, numpy
import numpy
import sys
from math import *
import csv
from shutil import copyfile
import numpy as np


# creates folder containing individual timing files for a specific subject, TMS condition, and run
def createSingles(dataLoc, outDirLoc, subject, run, file):
    # Reads in a CSV datafile; text files. Expects the first row to be the column names
    csvFile = dataLoc + subject + "_run" + run + "_" + file
    separator = ','
    # open csv file, individual lines are read as a trial
    # individual lines are split using the given separator
    # trialList is a list of these lines
    trialList = [trial.split(separator) for trial in open(csvFile, 'r').readlines()]
    # header
    colNames = trialList[0]
    # list of trials
    trialList = trialList[1:]
    # timeToSubtract = 8  # note: NOT NEEDED AT UCSB DEPENDING ON HOW YOU'RE MODELING YOUR DATA
    # trialDict will be a list of dictionaries for each trial that contains the column name and value
    trialDict = []
    for curTrial in trialList:
        tempDict = {}
        # looping through enumerate object that has a counter to each column name
        for colNum, curCol in enumerate(colNames):
            # tempDict is a dictionary with the column name and value for each trial
            tempDict[curCol.rstrip()] = curTrial[colNum].rstrip()
        trialDict.append(tempDict)
    # example of what trialDict looks like:
    # [{"condition":"d", ... "stimOnset":"20.56098367"...}, {..."stimOnset":"28.2048323"...}, ...]

    stimTimingFilesSeparator = '\t'  # FSL's preferred "1d files" separator

    # run=run
    i = 0
    # timing text file created for every trial
    for trial in enumerate(trialDict):
        # fn is a file object that will contain single timing trial info
        # w denotes open for writing
        fn = open(outDirLoc + subject + '_run' + str(run) + '_' + str(int(trial[0]) + 1) + '.txt', 'w')
        # matrix=stimTimingFilesSeparator.join(map(str,[trial[1]['stimOnset'],.5,trial[1]['RT']]))  #if weighted by RT
        # Note: removing 4 seconds from all timing because will remove 4 dummy scans #NOTE: LIKELY NOT NEEDED AT UCSB
        matrix = stimTimingFilesSeparator.join(map(str, [str((float(trial[1]['image_onset']))), 2.2, 1]))
        # matrix is the information that will be written into the text file
        # takes the stimOnset value from the trial, subtracts timeToSubtract to get the time we want in the file
        # joins together the .5 and 1 value by the tab separation denoted by stimTimingFilesSeparator
        fn.write(matrix + '\n')
        os.fsync(fn)
        fn.flush()
        fn.close()
    # file writes and closes


##############################################################################################################
##############################################################################################################


# subject=sys.argv[1]
subjects = ["Put your subjects here"] #todo change
runs = ['1', '2', '3', '4', '5', '6', '7', '8']

# outDirName='/home/despoB/agng/raw-data/timing/'
# BevDir = '/Users/jingyiwang/Desktop/AA_fMRIAnalyses/BevAnalysis/AAbevsorted/'
# TimeFileDir = "/Users/jingyiwang/Desktop/AA_fMRIAnalyses/BevAnalysis/TimeseriesGeneretor/"
BevDir = 'YourMainFolder/ASAP/AA_fMRI/process/AAbevsorted/'
TimeFileDir = "YourMainFolder/ASAP/AA_fMRI/process/TimeFiles/"
# runs=['1']
file = 'AA.csv'  # (n=24 rows= 24 trials)

for subject in subjects:
    outDirLoc = TimeFileDir + subject + "/singleBetas_full/"
    print(subject)
    #If the outDirLoc not exist make a folder.
    try:
        os.stat(outDirLoc)
    except:
        os.mkdir(outDirLoc)
    for run in runs:
        dataLoc = BevDir + subject + '/'

        try:
            createSingles(dataLoc, outDirLoc, subject, run, file)
        except:
            print("file does not exist" + subject + " " + run)
