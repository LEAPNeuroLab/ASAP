import itertools
import random
import os
import numpy as np
import pandas as pd
import glob
import itertools
import scipy
from scipy import stats
from psychopy import visual, core, event, gui

#Get participants ID
ID = {"subject":"",}
dialogue = gui.DlgFromDict(ID)
#ID = input("Please enter the 3 digits participant's ID:\n")

#Get the two orders for the run.
directory = os.path.dirname(os.path.abspath(__file__))#Get the current directory
order1_dir = os.path.join(directory, "AA_order1" + "." + "csv")
order2_dir = os.path.join(directory, "AA_order2" + "." + "csv")
order1 = pd.read_csv(order1_dir, delimiter =',', header = 0)
order2 = pd.read_csv(order2_dir, delimiter =',', header = 0)

#Get the final order for the run.
#IF the last digit of the ID is 0-4, order 1, otherwise, order2.
li_1=[0, 1, 2, 3, 4]
li_2=[5, 6, 7, 8, 9]

if int(ID['subject'][-1]) in li_1:
    tmp_order=order1
else:
    tmp_order=order2
#IF ID is odd Incong first, ID is even Cong first.
tmp_cong = tmp_order[tmp_order['Congruency'] == 0]
tmp_incong = tmp_order[tmp_order['Congruency'] == 1]
if int(ID['subject'][-1]) % 2 == 0:
    run_order = pd.concat([tmp_cong, tmp_incong],ignore_index=True)
else:
    run_order = pd.concat([tmp_incong, tmp_cong],ignore_index=True)

## Add the "ImgStim" column.
# Add a long dataframe for all the runs.
All_run = pd.concat([run_order]*8, ignore_index=True)
# Add run number
li_runnumber = list(itertools.repeat(1, 24)) + list(itertools.repeat(2, 24)) + list(itertools.repeat(3, 24)) + list(itertools.repeat(4, 24)) + list(itertools.repeat(5, 24)) + list(itertools.repeat(6, 24)) + list(itertools.repeat(7, 24)) + list(itertools.repeat(8, 24))
All_run["run"] = li_runnumber

neg_dir = os.path.join(directory, "Attack_list" + "." + "csv")
pos_dir = os.path.join(directory, "Positive_list" + "." + "csv")
df_neg = pd.read_csv(neg_dir, delimiter =',', header = 0)
df_pos = pd.read_csv(pos_dir, delimiter =',', header = 0)

#Add Target_joy_parameter #todo add this to psychopy file.
go_list = list(itertools.repeat(0.2,96))
mask_joy_go = All_run['Action'].apply(lambda x: 1 if x == "go" else 0).astype('bool')
All_run.loc[mask_joy_go,'Target_JoyParameter'] = go_list

nogo_list = list(itertools.repeat(-0.2, 96))
mask_joy_nogo = All_run['Action'].apply(lambda x: 1 if x == "nogo" else 0).astype('bool')
All_run.loc[mask_joy_nogo,'Target_JoyParameter'] = nogo_list

# Function to check any value in the list smaller than the val, return ture.
def CheckForLess(li, val):
    return(any(x < val for x in li))
p_list=list(itertools.repeat(0.01, 8))
n=0
while CheckForLess(p_list,0.1):
    n=n+1
    df_neg = df_neg.sample(frac=1).reset_index(drop=True)
    df_pos = df_pos.sample(frac=1).reset_index(drop=True)

    mask_neg = All_run['StimVal'].apply(lambda x: 1 if x == "neg" else 0).astype('bool')
    All_run.loc[mask_neg,'ImgStim'] = df_neg["IAPS"].tolist()
    All_run.loc[mask_neg,'valmn'] = df_neg["valmn"].tolist()
    All_run.loc[mask_neg,'aromn'] = df_neg["aromn"].tolist()
    All_run.loc[mask_neg,'valsd'] = df_neg["valsd"].tolist()
    All_run.loc[mask_neg,'arosd'] = df_neg["arosd"].tolist()
    All_run.loc[mask_neg,'Social'] = df_neg["Social"].tolist()

    mask_pos = All_run['StimVal'].apply(lambda x: 1 if x == "pos" else 0).astype('bool')
    All_run.loc[mask_pos,'ImgStim'] = df_pos["IAPS"].tolist()
    All_run.loc[mask_pos,'valmn'] = df_pos["valmn"].tolist()
    All_run.loc[mask_pos,'aromn'] = df_pos["aromn"].tolist()
    All_run.loc[mask_pos,'valsd'] = df_pos["valsd"].tolist()
    All_run.loc[mask_pos,'arosd'] = df_pos["arosd"].tolist()
    All_run.loc[mask_pos,'Social'] = df_pos["Social"].tolist()

    # Check the stimuli valence of positive and go trials vs positive nogo trials are comparable.
    PosGo = All_run.loc[(All_run['StimVal']=="pos") & (All_run["Action"]=="go")]
    PosGo_list_val = PosGo['valmn']
    PosNogo = All_run.loc[(All_run['StimVal']=="pos") & (All_run["Action"]=="nogo")]
    PosNogo_list_val = PosNogo['valmn']
    test1 = stats.ttest_ind(PosGo_list_val,PosNogo_list_val)
    p1 = test1.pvalue
    
    # Check the stimuli arousal of positive and go trials vs positive nogo trials are comparable.
    PosGo_list_aro = PosGo['aromn']
    PosNogo_list_aro = PosNogo['aromn']
    test2 = stats.ttest_ind(PosGo_list_aro,PosNogo_list_aro)
    p2 = test2.pvalue
    # Check the stimuli valence of negative and go trials vs negative nogo trials are comparable.
    NegGo = All_run.loc[(All_run['StimVal']=="neg") & (All_run["Action"]=="go")]
    NegGo_list_val = NegGo['valmn']
    NegNogo = All_run.loc[(All_run['StimVal']=="neg") & (All_run["Action"]=="nogo")]
    NegNogo_list_val = NegNogo['valmn']
    test3 = stats.ttest_ind(NegGo_list_val,NegNogo_list_val)
    p3=test3.pvalue
    # Check the stimuli arousal of negative and go trials vs negative nogo trials are comparable.
    NegGo_list_aro = NegGo['aromn']
    NegNogo_list_aro = NegNogo['aromn']
    test4 = stats.ttest_ind(NegGo_list_aro,NegNogo_list_aro)
    p4=test4.pvalue
    # Check the valence of selected positive stimuli for all runs are comparable.
    pos_run1 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==1)]
    pos_run1_list_val = pos_run1['valmn']
    pos_run2 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==2)]
    pos_run2_list_val = pos_run2['valmn']
    pos_run3 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==3)]
    pos_run3_list_val = pos_run3['valmn']
    pos_run4 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==4)]
    pos_run4_list_val = pos_run4['valmn']
    pos_run5 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==5)]
    pos_run5_list_val = pos_run5['valmn']
    pos_run6 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==6)]
    pos_run6_list_val = pos_run6['valmn']
    pos_run7 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==7)]
    pos_run7_list_val = pos_run7['valmn']
    pos_run8 = All_run.loc[(All_run['StimVal']=="pos") & (All_run['run']==8)]
    pos_run8_list_val = pos_run8['valmn']
    test5 = stats.f_oneway(pos_run1_list_val, pos_run2_list_val, pos_run3_list_val, pos_run4_list_val, pos_run5_list_val, pos_run6_list_val, pos_run7_list_val, pos_run8_list_val)
    p5=test5.pvalue
    # Check the arousal of selected positive stimuli for all runs are comparable.
    pos_run1_list_aro = pos_run1['aromn']
    pos_run2_list_aro = pos_run2['aromn']
    pos_run3_list_aro = pos_run3['aromn']
    pos_run4_list_aro = pos_run4['aromn']
    pos_run5_list_aro = pos_run5['aromn']
    pos_run6_list_aro = pos_run6['aromn']
    pos_run7_list_aro = pos_run7['aromn']
    pos_run8_list_aro = pos_run8['aromn']
    test6 = stats.f_oneway(pos_run1_list_aro, pos_run2_list_aro, pos_run3_list_aro, pos_run4_list_aro, pos_run5_list_aro, pos_run6_list_aro, pos_run7_list_aro, pos_run8_list_aro)
    p6=test6.pvalue
    # Check the valence of selected negative stimuli for all runs are comparable.
    neg_run1 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==1)]
    neg_run1_list_val = neg_run1['valmn']
    neg_run2 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==2)]
    neg_run2_list_val = neg_run2['valmn']
    neg_run3 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==3)]
    neg_run3_list_val = neg_run3['valmn']
    neg_run4 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==4)]
    neg_run4_list_val = neg_run4['valmn']
    neg_run5 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==5)]
    neg_run5_list_val = neg_run5['valmn']
    neg_run6 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==6)]
    neg_run6_list_val = neg_run6['valmn']
    neg_run7 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==7)]
    neg_run7_list_val = neg_run7['valmn']
    neg_run8 = All_run.loc[(All_run['StimVal']=="neg") & (All_run['run']==8)]
    neg_run8_list_val = neg_run8['valmn']
    test7 = stats.f_oneway(neg_run1_list_val, neg_run2_list_val, neg_run3_list_val, neg_run4_list_val, neg_run5_list_val, neg_run6_list_val, neg_run7_list_val, neg_run8_list_val)
    p7=test7.pvalue
    # Check the arousal of selected negative stimuli for all runs are comparable.
    neg_run1_list_aro = neg_run1['aromn']
    neg_run2_list_aro = neg_run2['aromn']
    neg_run3_list_aro = neg_run3['aromn']
    neg_run4_list_aro = neg_run4['aromn']
    neg_run5_list_aro = neg_run5['aromn']
    neg_run6_list_aro = neg_run6['aromn']
    neg_run7_list_aro = neg_run7['aromn']
    neg_run8_list_aro = neg_run8['aromn']
    test8 = stats.f_oneway(neg_run1_list_aro, neg_run2_list_aro, neg_run3_list_aro, neg_run4_list_aro, neg_run5_list_aro, neg_run6_list_aro, neg_run7_list_aro, neg_run8_list_aro)
    p8=test8.pvalue
    p_list=[p1, p2, p3, p4, p5, p6, p7, p8]

#add .jpg to the "ImgStim" rows
All_run["ImgStim"] = All_run["ImgStim"].apply(lambda x: "{}{}".format(x,'.jpg'))
All_run["ImgStim"] = 'stimuli/' + All_run["ImgStim"].astype(str)
# divide into each run and save the file in the same folder.
AA_con_run1 = All_run.loc[All_run['run']==1]
AA_con_run2 = All_run.loc[All_run['run']==2]
AA_con_run3 = All_run.loc[All_run['run']==3]
AA_con_run4 = All_run.loc[All_run['run']==4]
AA_con_run5 = All_run.loc[All_run['run']==5]
AA_con_run6 = All_run.loc[All_run['run']==6]
AA_con_run7 = All_run.loc[All_run['run']==7]
AA_con_run8 = All_run.loc[All_run['run']==8]

directory = os.path.dirname(os.path.abspath(__file__))
AA_con_run1.to_csv(os.path.join(directory, "AA_con_run1" + "." + "csv"), index=False)
AA_con_run2.to_csv(os.path.join(directory, "AA_con_run2" + "." + "csv"), index=False)
AA_con_run3.to_csv(os.path.join(directory, "AA_con_run3" + "." + "csv"), index=False)
AA_con_run4.to_csv(os.path.join(directory, "AA_con_run4" + "." + "csv"), index=False)
AA_con_run5.to_csv(os.path.join(directory, "AA_con_run5" + "." + "csv"), index=False)
AA_con_run6.to_csv(os.path.join(directory, "AA_con_run6" + "." + "csv"), index=False)
AA_con_run7.to_csv(os.path.join(directory, "AA_con_run7" + "." + "csv"), index=False)
AA_con_run8.to_csv(os.path.join(directory, "AA_con_run8" + "." + "csv"), index=False)

for i in range(4):
    locals()['betweenlong' + str(i + 1)] = []
    locals()['betweenshort' + str(i + 1)] = []
    locals()['within_1_' + str(i + 1)] = []
    locals()['within_2_' + str(i + 1)] = []
    locals()['within_3_' + str(i + 1)] = []
    locals()['within_4_' + str(i + 1)] = []
    for j in range(48):
        rowN=i*48+j
        # block_n = int(rowN//8)+1 #block count; block_n=1 represents first block
        a = int(i*48)
        idx_betweenlong = [0, 1, 2, 3, 44, 45, 46, 47]
        idx_betweenlong_current = [x+a for x in idx_betweenlong]
        idx_betweenshort = [20, 21, 22, 23, 24, 25, 26, 27]
        idx_betweenshort_current = [x+a for x in idx_betweenshort]
        idx_within_1 = [*range(4, 12)]
        idx_within_1_current = [x+a for x in idx_within_1]
        idx_within_2 = [*range(12, 20)]
        idx_within_2_current = [x+a for x in idx_within_2]
        idx_within_3 = [*range(28, 36)]
        idx_within_3_current = [x+a for x in idx_within_3]
        idx_within_4 = [*range(36, 44)]
        idx_within_4_current = [x+a for x in idx_within_4]
        if rowN in idx_betweenlong_current:
            locals()['betweenlong' + str(i + 1)].append(rowN)
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['betweenlong' + str(i + 1)].append('betweeen')
            locals()['betweenlong' + str(i + 1)].append('long')
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['betweenlong' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
        elif rowN in idx_betweenshort_current:
            locals()['betweenshort' + str(i + 1)].append(rowN)
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['betweenshort' + str(i + 1)].append('betweeen')
            locals()['betweenshort' + str(i + 1)].append('short')
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['betweenshort' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
        elif rowN in idx_within_1_current:
            locals()['within_1_' + str(i + 1)].append(rowN)
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['within_1_' + str(i + 1)].append('within')
            locals()['within_1_' + str(i + 1)].append('later')
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['within_1_' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
        elif rowN in idx_within_2_current:
            locals()['within_2_' + str(i + 1)].append(rowN)
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['within_2_' + str(i + 1)].append('within')
            locals()['within_2_' + str(i + 1)].append('first')
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['within_2_' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
        elif rowN in idx_within_3_current:
            locals()['within_3_' + str(i + 1)].append(rowN)
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['within_3_' + str(i + 1)].append('within')
            locals()['within_3_' + str(i + 1)].append('later')
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['within_3_' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
        elif rowN in idx_within_4_current:
            locals()['within_4_' + str(i + 1)].append(rowN)
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["ImgStim"])
            locals()['within_4_' + str(i + 1)].append('within')
            locals()['within_4_' + str(i + 1)].append('first')
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["run"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["StimVal"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["Action"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["Congruency"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["valmn"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["aromn"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["valsd"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["arosd"])
            locals()['within_4_' + str(i + 1)].append(All_run.iloc[rowN]["Social"])
# create a dictionary with the key for each row.
TestDic = {}
for k in range(4):
    for l in range(6):
        row_idx = l + k*6
        if l==0:
            TestDic[row_idx]=locals()['betweenlong' + str(k + 1)]
        elif l == 1:
            TestDic[row_idx] = locals()['betweenshort' + str(k + 1)]
        elif l == 2:
            TestDic[row_idx] = locals()['within_1_' + str(k + 1)]
        elif l == 3:
            TestDic[row_idx] = locals()['within_2_' + str(k + 1)]
        elif l == 4:
            TestDic[row_idx] = locals()['within_3_' + str(k + 1)]
        elif l == 5:
            TestDic[row_idx] = locals()['within_4_' + str(k + 1)]
#create list for column names
i=0
name_list = []
for i in range(8):
    pos1="image"+str(i+1)+"_orig_idx"
    pos2="image"+str(i+1)+"Stim"
    pos3="image"+str(i+1)+"_typebetween"
    pos4="image"+str(i+1)+"_typelong"
    pos5 = "image" + str(i + 1) + "_run"
    pos6="image"+str(i+1)+"_StimVal"
    pos7 = "image" + str(i + 1) + "_Action"
    pos8 = "image" + str(i + 1) + "_Congruency"
    pos9 = "image" + str(i + 1) + "_valmn"
    pos10 = "image" + str(i + 1) + "_aromn"
    pos11 = "image" + str(i + 1) + "_valsd"
    pos12 = "image" + str(i + 1) + "_arosd"
    pos13 = "image" + str(i + 1) + "_Social"
    name_list.extend([pos1, pos2, pos3, pos4, pos5, pos6,pos7,pos8,pos9,pos10,pos11,pos12,pos13])
# form a dataframe of the temporal order test condition file from the TestDict
OrderTest = pd.DataFrame.from_dict(TestDic, orient='index', columns=name_list)
#rearrange the column order:
# shift column 'Name' to first position
tmp_first = OrderTest.pop('image8Stim')
# insert column using insert(position,column_name,first_column) function
OrderTest.insert(0, 'image8Stim', tmp_first)
#do the same thing for the rest of the 8 stimuli columns:
tmp_first = OrderTest.pop('image7Stim')
OrderTest.insert(0, 'image7Stim', tmp_first)
tmp_first = OrderTest.pop('image6Stim')
OrderTest.insert(0, 'image6Stim', tmp_first)
tmp_first = OrderTest.pop('image5Stim')
OrderTest.insert(0, 'image5Stim', tmp_first)
tmp_first = OrderTest.pop('image4Stim')
OrderTest.insert(0, 'image4Stim', tmp_first)
tmp_first = OrderTest.pop('image3Stim')
OrderTest.insert(0, 'image3Stim', tmp_first)
tmp_first = OrderTest.pop('image2Stim')
OrderTest.insert(0, 'image2Stim', tmp_first)
tmp_first = OrderTest.pop('image1Stim')
OrderTest.insert(0, 'image1Stim', tmp_first)
# Save the temporal order sorting condition file
OrderTest.to_csv(os.path.join(directory, "TemporalOrderTest" + "." + "csv"), index=False)


#Generate condition file for the coarse temporal test:
orig_idx = [*range(0, 192)]
All_run["orig_idx"]=orig_idx
CoarseTemporal = All_run.sample(frac=1).reset_index(drop=True)
tmp_first = CoarseTemporal.pop('orig_idx')
CoarseTemporal.insert(0, 'orig_idx', tmp_first)
tmp_first = CoarseTemporal.pop('ImgStim')
CoarseTemporal.insert(0, 'ImgStim', tmp_first)
CoarseTemporal.to_csv(os.path.join(directory, "CoarseTemporal" + "." + "csv"), index=False)

## Generate condition file for the valence and arousal test:
# ValAro = CoarseTemporal.sample(frac=1).reset_index(drop=True)
# ValAro.to_csv(os.path.join(directory, "ValenceArousal" + "." + "csv"), index=False)
