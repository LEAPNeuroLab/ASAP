import pandas as pd
import glob
import os
import numpy as np
import itertools
import ast
from itertools import repeat
from ast import literal_eval

# path=os.getcwd() # Path of directory containing data files.
#todo the path and output_dir is subject to change.
directory = os.path.dirname(os.path.abspath(__file__))#Get the current directory
path=os.path.join(directory,'raw_data_posttask')
output_dir=directory
extension = "csv"
fieldnames = ['participant', 'CoarseTemp_slider.response','CoarseTemp_slider.rt','ImgStim', 'mouse_ItemMem.clicked_name', 'mouse.clicked_name', 'mouse_3.clicked_name']
output_AA = 'AA_Coarsetemporal.csv'  # Output filename for all the selected column and all the subjects.

output_filepath = os.path.join(output_dir, output_AA)  # Output in same directory.
csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))
            if filename != output_filepath]  # Avoid reading any existing output file.

li = []
for file in csvlist:
    df = pd.read_csv(file, usecols = fieldnames, delimiter =',', header = 0)
    li.append(df)
dfall = pd.concat(li, axis=0, ignore_index=True)

clean_coarse = dfall.dropna(subset=['CoarseTemp_slider.response','CoarseTemp_slider.rt'], how='all') # removed empty cells.
clean_coarse=clean_coarse.reset_index(drop=True)
clean_coarse.to_csv(output_filepath, sep=',', index=False)

#Get the AA task info and then merge with coarse temporal dataframe by particpant and ImgStim.
# path=os.getcwd() # Path of directory containing data files.
#todo the path and output_dir is subject to change.
directory = os.path.dirname(os.path.abspath(__file__))#Get the current directory
path=os.path.join(directory,'raw_data')
output_dir=directory
extension = "csv"
fieldnames = ['participant', 'GrayScreent.started', 'run', 'StimVal', 'ITI', 'Action','TargetVal','nonTargetVal', 'Congruency', 'trialNum','order','run','ImgStim','valmn','aromn','valsd','arosd','Social', 'Instruction_1.started', 'image.started', 'joystickMove_started','joystick_reaction','trial_correct']

output_filepath = os.path.join(output_dir, output_AA)  # Output in same directory.
csvlist = [filename for filename in glob.glob(os.path.join(path, f'*.{extension}'))]

li = []
for file in csvlist:
    df = pd.read_csv(file, usecols = fieldnames, delimiter =',', header = 0)
    li.append(df)
dfall = pd.concat(li, axis=0, ignore_index=True)

clean_AA = dfall.dropna(subset=['image.started', 'joystickMove_started','joystick_reaction','trial_correct','GrayScreent.started'], how='all') # removed empty cells.
clean_AA=clean_AA.reset_index(drop=True)
#remove the first six rows in each participant
sublist=list(clean_AA.participant.unique())
# clean_AA.reset_index(inplace=True)
#Add the total time for the joystick experiment.
TotalTime=[]
Start=[]
imageonset=[]
ppli=[]
for sub in sublist:
    tmp_df=clean_AA.loc[clean_AA['participant']==sub]
    tmp_df.reset_index(inplace=True)
    Tstart=tmp_df["GrayScreent.started"].dropna().iloc[0]
    Start.append(Tstart)
    Tend=tmp_df["GrayScreent.started"].dropna().iloc[-1]+20 #20s grayscreen
    Ttotal = Tend-Tstart
    TotalTime.append(Ttotal)
    ppli.append(sub)
    if sub==11:
        runli = list(range(1, 8, 1))
    else:
        runli = list(range(1, 9, 1))
    for run in runli:
        tmp_df_2= tmp_df.loc[tmp_df['run'] == run].reset_index()
        starttime = tmp_df_2.at[0, "GrayScreent.started"]  # todo no need to remove TR.
        cols = "GrayScreent.started"
        tmp_df_2.loc[:, cols] = tmp_df_2.loc[:, cols].ffill()
        tmp_df_2["instruction_onset"] = tmp_df_2["Instruction_1.started"] - starttime
        tmp_df_2["image_onset"] = tmp_df_2["image.started"] - starttime
        imageonset = imageonset + list(tmp_df_2["image_onset"])
Timedf = pd.DataFrame({'participant': ppli,'Start': Start,'TotalTime': TotalTime})
# col_TotalTime=list(itertools.chain.from_iterable(itertools.repeat(x,192) for x in TotalTime))
# col_Start=list(itertools.chain.from_iterable(itertools.repeat(x,192) for x in Start))
clean_AA = dfall.dropna(subset=['image.started', 'joystickMove_started','joystick_reaction','trial_correct'], how='all') # removed empty cells.
clean_AA=clean_AA.reset_index(drop=True)
# clean_AA.reset_index(inplace=True)
# clean_AA['TotalTime']=col_TotalTime
# clean_AA['Start']=col_Start
clean_AA['image_onset']=imageonset
#Merge
clean_AA_1 = clean_AA.merge(Timedf, how='left', on=['participant'])

AATemp_merge = clean_AA_1.merge(clean_coarse, how='inner',on=['participant','ImgStim'])
#rename columns
AATemp_merge.rename({'mouse_ItemMem.clicked_name': 'ReconMem'}, axis=1, inplace=True)
AATemp_merge.rename({'mouse.clicked_name': 'ConfReconMem'}, axis=1, inplace=True)
AATemp_merge.rename({'mouse_3.clicked_name': 'ConfCoarseMem'}, axis=1, inplace=True)

AATemp_merge.to_csv(os.path.join(directory, "CoarseMem_sorted" + "." + "csv"), index=False)


