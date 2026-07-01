import pandas as pd
import glob
import os
import numpy as np
import itertools
import math
import json
from scipy import signal
import ast
from itertools import repeat

# path=os.getcwd() # Path of directory containing data files.
#todo the path and output_dir is subject to change.
directory = os.path.dirname(os.path.abspath(__file__))#Get the current directory
path=os.path.join(directory,'raw_data')
output_dir=directory
extension = "csv"
fieldnames = ['participant', 'run', 'StimVal', 'ITI', 'Action','TargetVal','nonTargetVal', 'Congruency', 'trialNum','order','run','Target_JoyParameter','joystick_max','joystick_min','ImgStim','valmn','aromn','valsd','arosd','Social', 'Instruction_1.started', 'image.started', 'joystickMove_started','joystick_reaction','trial_correct','joystick_timepoint','joystick_X','joystick_Y']
output_AA = 'AA_allaa.csv'  # Output filename for all the selected column and all the subjects.


output_filepath = os.path.join(output_dir, output_AA)  # Output in same directory.
csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))
            if filename != output_filepath]  # Avoid reading any existing output file.

li = []
for file in csvlist:
    df = pd.read_csv(file, usecols = fieldnames, delimiter =',', header = 0)
    li.append(df)
dfall = pd.concat(li, axis=0, ignore_index=True)
clean_AA = dfall.dropna(subset=['image.started', 'joystickMove_started','joystick_reaction','trial_correct','joystick_timepoint','joystick_X','joystick_Y'], how='all') # removed empty cells.
#Add column for velocity adn acceleration
#First add start column and reach column
starty=[]
reachxy=[]
d = []
v = []
max_v = []
a = []
max_a = []
init = []
watch = []
max_v_time = []
max_a_time = []
#store the range of x, y and xy
max_X = []
min_X = []
max_Y = []
min_Y = []
max_xy = []
min_xy = []

for index, row in clean_AA.iterrows():
    peakA_index=""
    peakV_index=""
    # print(row['participant'])
    #Get starty
    lenA=len(json.loads(row['joystick_Y']))
    tmp_starty = np.array(list(itertools.repeat(json.loads(row['joystick_Y'])[0], lenA)))
    starty.append(tmp_starty)
    #Get reachxy
    tmp_reachxy = np.sqrt(np.array(json.loads(row['joystick_X']))**2 + np.array(json.loads(row['joystick_Y']))**2)
    reachxy.append(tmp_reachxy)
    max_X.append(max(json.loads(row['joystick_X'])))
    min_X.append(min(json.loads(row['joystick_X'])))
    max_Y.append(max(json.loads(row['joystick_Y'])))
    min_Y.append(min(json.loads(row['joystick_Y'])))
    max_xy.append(max(tmp_reachxy))
    min_xy.append(min(tmp_reachxy))
    # Get the initial movement timepoint, radius as 0.008
    tmp = abs(np.array(json.loads(row['joystick_Y'])) - tmp_starty)
    watch.append(tmp)
    # If participant did not release joystick for the trial
    if json.loads(row['joystick_Y'])[0] < -0.2 or json.loads(row['joystick_Y'])[
        0] > 0.2:  # In this case, the picture size is not original
        init.append(np.nan)
        max_v.append(np.nan)
        max_v_time.append(np.nan)
        max_a.append(np.nan)
        max_a_time.append(np.nan)
    else:
        try:
            start = [idx for idx, i in enumerate(tmp) if i > 0.008][0]
            tmp_init = np.array(json.loads(row['joystick_timepoint']))[start] - np.array(json.loads(row['joystick_timepoint']))[0]
            #remove reaction time calculated as < 0.2s, normal human reaction >0.25s.
            if tmp_init < 0.2:
                tmp_init=np.nan
        except IndexError:
            tmp_init = np.nan
        init.append(tmp_init)
        # 0th derivative, displacement of reach
        # tmp_d = np.sqrt(np.diff(np.array(json.loads(row['joystick_X'])))**2 + np.diff(np.array(json.loads(row['joystick_Y'])))**2)
        tmp_d = np.abs(np.diff(np.array(json.loads(row['joystick_Y']))))
        d.append(tmp_d)

        tmp_t = np.diff(np.array(json.loads(row['joystick_timepoint'])))
        #velocity of displacement
        tmp_v = tmp_d/tmp_t
        v.append(tmp_v)
        sig_peaksV, _ = signal.find_peaks(tmp_v, distance=6)
        #Find the max v with time large than start time and first occurance of two largest peaks
        try:
            sig_peaksV_filtered = [i for i in sig_peaksV if i>=start-1]
            tmp_v_peaks = [tmp_v[i] for i in sig_peaksV_filtered]
            tmp_v_peaks.sort(reverse=True)
            peak1V_time = tmp_v.tolist().index(tmp_v_peaks[0])
            peak2V_time = tmp_v.tolist().index(tmp_v_peaks[1])
            if peak1V_time>peak2V_time:
                peakV_index = peak2V_time
            else:
                peakV_index = peak1V_time
            max_v.append(tmp_v[peakV_index])
        except IndexError:
            max_v.append(np.nan)
        #Find the timepoint reach max_v
        try:
            sig_peaksV_filtered = [i for i in sig_peaksV if i>=start-1]
            tmp_maxVt=json.loads(row['joystick_timepoint'])[peakV_index + 1]-json.loads(row['joystick_timepoint'])[0]
            max_v_time.append(tmp_maxVt)
        except IndexError:
            max_v_time.append(np.nan)
        except TypeError:
            max_v_time.append(np.nan)
        # 2nd derivative, acceleration of displacement
        tmp_a = np.diff(tmp_v)
        a.append(tmp_a)
        sig_peaksA, _ = signal.find_peaks(tmp_a, distance=6)
        # Find the max a with time large than start time and first occurance of peak
        try:
            sig_peaksA_filtered = [i for i in sig_peaksA if i >= start - 2]
            tmp_a_peaks = [tmp_a[i] for i in sig_peaksA_filtered]
            tmp_a_peaks.sort(reverse=True)
            peak1A_time = tmp_a.tolist().index(tmp_a_peaks[0])
            peak2A_time = tmp_a.tolist().index(tmp_a_peaks[1])
            if peak1A_time > peak2A_time:
                peakA_index = peak2A_time
            else:
                peakA_index = peak1A_time
            max_a.append(tmp_a[peakA_index])
        except IndexError:
            max_a.append(np.nan)
        # Find the timepoint reach max_a
        try:
            sig_peaksA_filtered = [i for i in sig_peaksA if i >= start - 2]
            tmp_maxAt = json.loads(row['joystick_timepoint'])[peakA_index + 2] - \
                        json.loads(row['joystick_timepoint'])[0]
            max_a_time.append(tmp_maxAt)
        except IndexError:
            max_a_time.append(np.nan)
        except TypeError:
            max_a_time.append(np.nan)

clean_AA['max_V']=max_v
clean_AA['max_V_time']=max_v_time
clean_AA['max_a']=max_a
clean_AA['max_a_time'] = max_a_time
clean_AA['joystick_RTcal']=init
reptime = int(len(clean_AA)/24)
clean_AA['trialNum2'] = list(range(24))*reptime

# Filter incorrect trials
# Create trial_correct_RTmod column indicate both trial_correct RTcal_demean values.
mask1 = ((clean_AA['trial_correct'] == 0) | (np.isnan(clean_AA['joystick_RTcal'])))
clean_AA.loc[mask1,'trial_correct_RTcal'] = 0
clean_AA.loc[~mask1,'trial_correct_RTcal'] = 1

clean_AA.to_csv(output_filepath, sep=',', index=False)
