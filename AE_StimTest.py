import time, sys, random, os, serial, ctypes, numpy
from psychopy import visual, core, event, sound, gui
import pandas as pd
import numpy as np
from scipy import stats
import ctypes
from mcculw import ul
from mcculw.enums import InterfaceType
from math import *
from mcculw.enums import CounterChannelType, DigitalPortType, DigitalIODirection
from mcculw.ul import ULError
from mcculw.device_info import DaqDeviceInfo
import tkinter as tk#from builtins import *  # @UnusedWildImport

from mcculw import ul
from mcculw.enums import ULRange

from mcculw.enums import DigitalIODirection
from mcculw.device_info import DaqDeviceInfo
from mcculw.enums import DigitalPortType, DigitalIODirection
board_num = 0

PORTVAR = ul.d_config_port(board_num, DigitalPortType.AUXPORT, DigitalIODirection.OUT)
print("Port var:", PORTVAR)
interface_type = InterfaceType.ANY
output_channel = 0

devices = ul.get_daq_device_inventory(interface_type)
daq_dev_info = DaqDeviceInfo(board_num)
print('\nActive DAQ device: ', daq_dev_info.product_name, ' (',daq_dev_info.unique_id, ')\n', sep='')
ao_info = daq_dev_info.get_ao_info()
core.wait(1)
num_chans = min(ao_info.num_chans, 4)
num_points = num_chans
ao_range = ULRange.BIP10VOLTS
ul.a_out(board_num,0, ao_range, data_value =2000)

rg = [1,2,3]
core.wait(3.000)
#event.waitKeys(keyList='space')
for i in rg:
    try:
        # The last argument is the byte value that you want to write to the port
        sendTrig = ul.a_out(board_num,0, ao_range, data_value =2520) #50 =  -9.75V; 200 = -9V; 500=-7.5; 1000= -5V; 2000=0V #
        sendTrig
        print('sendTrig')
        core.wait(0.2)
        ul.a_out(board_num, 0, ao_range, data_value = 2000)
        core.wait(1)
        print("revert to 0")
    except ULError as e:
        codeMsg = 'Write Error: ' + str(e.errorcode) + ' (' + e.message + ')'