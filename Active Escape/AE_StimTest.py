#Joanne Stasiak 2022

'''
Test of the shock machine for participants to get used to feeling a shock for the first time

'''

import time, sys, random, os, serial, ctypes, numpy
from psychopy import visual, core, event, sound, gui
import pandas as pd
import numpy as np
from scipy import stats
import ctypes
from math import *

#Import MCC Universal Library to use with the digital port, which talks to the stimulus computer and sends shocks to the shock machine (Biopac STM100C)
from mcculw import ul
from mcculw.enums import InterfaceType
from mcculw.enums import CounterChannelType, DigitalPortType, DigitalIODirection
from mcculw.ul import ULError
from mcculw.device_info import DaqDeviceInfo
import tkinter as tk
from mcculw.enums import ULRange

#Set up the digital port
board_num = 0#we will use the first digital port
devices = ul.get_daq_device_inventory(interface_type)#find any and all ports connected
daq_dev_info = DaqDeviceInfo(board_num)#but again just use the first one -  check in insta cal the board is '0'
ao_range = ULRange.BIP10VOLTS#Our range of shocks the board can send (+/-10V)
ul.a_out(board_num,0, ao_range, data_value =2000) #initialize the board to 0 volts so it is not sitting at a negative/positive voltage to begin

#First send one shock
sendTrig = ul.a_out(board_num,0, ao_range, data_value =2520)# This is 2.57V --  50 =  -9.75V; 200 = -9V; 500=-7.5; 1000= -5V; 2000=0V #
sendTrig
core.wait(0.2)
ul.a_out(board_num, 0, ao_range, data_value = 2000)#bring it back to 0 volts

#Then check on the participant to see how they are doing
#And press space to continue
event.waitKeys(keyList='space')

#Then send a sequence of 3 more pulses of the same intensity
rg = [1,2,3]
core.wait(3.000)
for i in rg:
    try:
        # The last argument is the byte value that you want to write to the port
        sendTrig = ul.a_out(board_num,0, ao_range, data_value =2520)
        sendTrig
        print('sendTrig')
        core.wait(0.2)
        ul.a_out(board_num, 0, ao_range, data_value = 2000)
        core.wait(1)# 1 sec duration between shocks
        print("revert to 0")
    except ULError as e:
        codeMsg = 'Write Error: ' + str(e.errorcode) + ' (' + e.message + ')'
