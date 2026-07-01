import matplotlib
# matplotlib.use('TkAgg')
import os
# imports
import numpy as np
#np.set_printoptions(precision = 3)
import matplotlib.pyplot as plt

import scipy
#get_ipython().magic('matplotlib inline')
import pandas as pd
#pd.set_option('precision',2)
import scipy.io as io
import json
#sns.set(color_codes=True)
#sns.set_style('white')
import os, subprocess, sys, glob
import nibabel as nib
import nilearn, sklearn
from nilearn import image,  input_data, decoding #plotting,
import sklearn.svm
from sklearn.pipeline import Pipeline
#from sklearn.cross_validation import LeaveOneLabelOut, cross_val_score, permutation_test_score
from sklearn.model_selection import LeaveOneGroupOut, cross_val_score, permutation_test_score
from sklearn.feature_selection import SelectKBest, f_classif
###unable to import the below, cross_validation was depracated a year and a half ago
#from sklearn.cross_validation import LeaveOneLabelOut
#from sklearn.model_selection import LeaveOneLabelOut


subs=["002", "003", "004", "005", "006", "008", "009", "010", "012", "014", "017", "019", "020", "021", "022", "023", "024", "025", "026", "029", "030", "031", "032", "033", "034", "035", "036", "037", "038", "039", "040", "041", "042", "043", "044", "045", "046", "047", "048", "049", "050", "051", "053", "054", "055", "056", "057", "058", "059", "060", "061", "062", "063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "073", "011", "015", "074", "075", "076", "077", "078", "079", "080", "082", "083"]

masks = ["perirhinal_exvivo.thresh", "entorhinal_exvivo.thresh"]
#outPath='/home/despoA/lapate/agng/analysis/MVPA/'
models=['MVPA_3mm']  #todo change
myGLMModels=['noTD_ST']  #todo change

OrigPrewhitten=["perirhinal_exvivo.thresh", "entorhinal_exvivo.thresh", "harvardoxford_Hippocampus_bin60_2mm"]


runs=['1','2','3','4','5','6','7','8']
# runs=['1', '2']
regtypes=['MVPA'] #

for mask in masks:
    # directory = os.path.dirname(os.path.abspath(__file__))#Get the current directory
    if mask in OrigPrewhitten:
        path = "YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/prewhitenedBetas"
    else:
        path = "YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/trialwise_matrix/prewhitenedBetasUni"
    output_dir = path
    extension = "csv"
    fieldnames = ['sub', 'mask', 'run', 'trial', 'voxel', 'ImgStim', 'value', 'value_whiten']
    # output_AA = 'AA_Coarsetemporal.csv'  # Output filename for all the selected column and all the subjects.

    # output_filepath = os.path.join(output_dir, output_AA)  # Output in same directory.
    csvlist = [filename for filename in
               glob.glob(os.path.join(path, f'*{mask}*.{extension}'))]  # Get all the sub TRbyTR results in one big df.
    print(csvlist)

    li = []
    for file in csvlist:
        df = pd.read_csv(file, usecols=fieldnames, delimiter=',', header=0)
        li.append(df)
    dfall = pd.concat(li, axis=0, ignore_index=True)


    #Calculate univariate acitivity for the current mask per sub per trial/ImgStim
    df_mean = dfall_filtered.groupby(['sub', 'mask', 'run', 'trial', 'ImgStim'],as_index=False)[['value', 'value_whiten']].mean()
    #save this df
    fdir = "YourMainFolder/ASAP/AA_fMRI/process/results/MVPA/AMY_uni"
    fname = mask + "_univariate.csv"
    fn = os.path.join(fdir,fname)
    df_mean.to_csv(fn, index = False)  # final
