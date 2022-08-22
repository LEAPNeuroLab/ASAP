#Stimulus Calibration Script for Perceptible shock - round 2
#Jo Stasiak 2022

'''
Script for Perceptible Shock Calibration (2)

In this script, participants will be given one electrical shock, and will then respond if the shock was reliably detectable and if it was at all unpleasant.

If participants say a shock was not reliably detectable, the intensity will increase a little bit.
If participants say a shock was unpleasant, the intensity will decrease a little bit.


This script uses data from the first iteration of the perceptible calibration.

'''

import time, sys, random, os, serial, ctypes, numpy
from psychopy import visual, core, event, sound, gui
import pandas as pd
import numpy as np
from scipy import stats
import ctypes
from math import *

#packages from Universal Library, used to talk to the digital port and send shocks through Biopac
from mcculw import ul
from mcculw.enums import InterfaceType, CounterChannelType, DigitalPortType, DigitalIODirection, ULRange
from mcculw.ul import ULError
from mcculw.device_info import DaqDeviceInfo

from psychopy.hardware import joystick
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
import tkinter as tk
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import re#used to read text files


# Set some initial values
board_num = 0
devices = ul.get_daq_device_inventory(interface_type)
daq_dev_info = DaqDeviceInfo(board_num)#get the first board it recognizes - check with instacal that it is board '0'
ao_range = ULRange.BIP10VOLTS#the range of shocks our board supports (+/-10V)
ul.a_out(board_num,0, ao_range, data_value =2000)# initialize it to 0 volts

expName = 'PerCalibration V2'
userVar = {'Participant':'Enter subject ID'}#Need to make sure this is the same that was used for the first calibration
dlg = gui.DlgFromDict(userVar, title=expName)
subID = str(userVar['Participant'])
while os.path.isfile('data/'+subID+'_calibration.txt'):
    userVar = {'Participant':'Enter subject ID'}
    dlg = gui.DlgFromDict(userVar)
    subID = str(userVar['Participant'])
userVar['expName'] = expName


win1 = visual.Window(size=(1275, 975),pos=(270,85), fullscr=False, screen=1, winType='pyglet', allowGUI=True, allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
win1.setMouseVisible(False)
curIntensity = 0 #.25V
defaultKeyboard = keyboard.Keyboard()
frameTolerance = 0.001
endExpNow = False

#Set up the joystick
nJoys = joystick.getNumJoysticks()
id = 0
joy = joystick.Joystick(id)#get the first joystick it recognizes

#Set up the joystick buttons
button_resp = type('', (), {})()
button_resp.device = None
button_resp.device_number = 0
button_resp.device = joystick.Joystick(0)
button_resp.status = None
button_resp.clock = core.Clock()
button_resp.numButtons = button_resp.device.getNumButtons()
button_resp.oldButtonState = button_resp.device.getAllButtons()[:]
button_resp.keys = []
button_resp.rt = []

#initialize variables
rating = 0
detectText = "Did you reliably detect a shock?"
y = "Yes"
n= "No"
instructionsText = visual.TextStim(win=win1, text='', height=0.06, pos=[0,0], wrapWidth=1.1, color='white')
space = keyboard.Keyboard()
defaultKeyboard = keyboard.Keyboard()

pid=subID
#Read the text file created during the first perceptible calibration and get the shock value
with open("data\\" + str(pid) + "_PerceptibleCalibration_1.txt", 'r') as per:
    lines = per.readlines()
    perShock = lines[-1].split('\t')[-1]
    print(perShock)
perShock=re.sub("[^0-9]", "", perShock)
perShock=int(perShock)

#Function for instructions shown on screen
def instFunc(text):
    win1.setMouseVisible(False)
    continueRoutine = True
    instructionsText.setText(text)
    instructionsText.draw()
    win1.flip()
    if defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    event.waitKeys(keyList="space")
    win1.flip()

detectArray=[]
detectResponse=0
detectVal=2
rating=2
detectq = visual.TextStim(win1, text='', height=0.08, color='white', pos=[0,0.3], wrapWidth=1.1)
yq=visual.TextStim(win1, text=y, height=0.07, color='black', pos=[-0.22, -0.15])
nq = visual.TextStim(win1, text=n, height=0.07, color='black', pos=[0.22, -0.15])
def detect():#Ask participants if they can reliably detect the shock
    continueRoutine = True
    detComponents = [detectq, yq,nq, button_resp]
    for thisComponent in detComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win1.getFutureFlipTime(clock="now")
    detClock = core.Clock()
    detClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        t = detClock.getTime()
        tThisFlip = win1.getFutureFlipTime(clock=detClock)
        tThisFlipGlobal = win1.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        if detectq.status == NOT_STARTED:
            detectq.setText('Was this shock reliably detectable?')
            detectq.setAutoDraw(True)
            yq.setAutoDraw(True)
            nq.setAutoDraw(True)
        waitOnFlip = False
        if button_resp.status == NOT_STARTED:
            button_resp.frameNStart = frameN
            button_resp.status = STARTED
            win1.callOnFlip(button_resp.clock.reset)
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [0,1] if i in button_resp.pressedButtons]#corresponds to the first two buttons on the joystick
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:# If they made a response
                print("these keys = ", theseKeys)
                button_resp.keys = theseKeys[-1]
                button_resp.rt = button_resp.clock.getTime()
                continueRoutine=False#Advance the screen
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in detComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win1.flip()

    for thisComponent in detComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if button_resp.keys == 0:#Participants said 'yes'
        detectVal=1
    if button_resp.keys == 1:#Participants said 'no'
        detectVal=0
    detectArray.append(button_resp.keys)
    detectResponse = detectVal
    return detectVal

#grey screen for waiting, says that the shock is coming up
def waitScreen(waitTime=waitTime, pos=[0,0], text='Shock will be delivered shortly', height=rateTextHeight):
    isiText = visual.TextStim(win1, text=text, height=0.07, color=textColor,pos=[0,0], wrapWidth=1.1)
    isiText.draw()
    win1.flip()
    core.wait(waitTime)

#send a shock
def deliverShock(intensity=curIntensity):
    #Deliver shock
    ul.a_out(board_num,0, ao_range, data_value =intensity)#data_value is the shock value you are sending
    core.wait(0.02)
    #Reset ShockPort
    ul.a_out(board_num,0, ao_range, data_value =2000)#set it back to 0 afterwards

#ratingKeys = keyboard.Keyboard()
ratingArray=[0]
ratingVal = 2
ratingInstr = visual.TextStim(win1, text= 'Was this shock at all unpleasant?', height=0.08, color='white', pos=[0,0.3], wrapWidth=1.1)
yq=visual.TextStim(win1, text='Yes', height=0.07, color='black', pos=[-0.22, -0.15])
nq = visual.TextStim(win1, text='No', height=0.07, color='black', pos=[0.22, -0.15])

def ratingScreen():#Ask if the shock was at all unpleasant
    continueRoutine = True
    ratComponents = [ratingInstr, yq,nq, button_resp]
    for thisComponent in ratComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win1.getFutureFlipTime(clock="now")
    ratClock = core.Clock()
    ratClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        t = ratClock.getTime()
        tThisFlip = win1.getFutureFlipTime(clock=ratClock)
        tThisFlipGlobal = win1.getFutureFlipTime(clock=None)
        frameN = frameN + 1
        win1.setMouseVisible(False)
        ratingInstr.setAutoDraw(True)
        yq.setAutoDraw(True)#Draw all the text on screen
        nq.setAutoDraw(True)
        if button_resp.status == NOT_STARTED:
            button_resp.frameNStart = frameN
            button_resp.status = STARTED
            win1.callOnFlip(button_resp.clock.reset)
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [0,1] if i in button_resp.pressedButtons]#corresponds to first two buttons on the joystick
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:#if they responded
                print("these keys = ", theseKeys)
                button_resp.keys = theseKeys[-1]
                button_resp.rt = button_resp.clock.getTime()
                continueRoutine = False#advance the screen
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        if not continueRoutine:
            break
        continueRoutine = False
        for thisComponent in ratComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break
        if continueRoutine:
            win1.flip()

    for thisComponent in ratComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    if button_resp.keys == 0:#Participants answered 'yes'
        ratingVal=1
    if button_resp.keys == 1:#Participants answered 'no'
        ratingVal=0
    ratingArray.append(button_resp.keys)
    ratResponse = ratingVal
    return ratingVal#return their response

def writeToFile(fileHandle,trial,sync=True):#Writes a trial (array of lists) to a file. File needs to be opened outside the function. Pass in the filehandle as an argument
    line = '\t'.join([str(i) for i in trial]) #TABify
    line += '\n' #add a newline
    fileHandle.write(line)
    if sync:
        fileHandle.flush()
        os.fsync(fileHandle)

########### BEGIN CALIBRATION SCRIPT################################################################
win1.setMouseVisible(False)
instFunc(text='''You will now go through the perceptible calibration again, starting from the perceptible shock you decided on the first time. \n\nYou will answer if you can reliably detect the shock and whether it was at all unpleasant.''')
instFunc(text='''Do you have any questions?''')

fileHandle = open('data/'+subID+'_PerceptibleCalibration_2.txt','w')#Create a new text file for this calibration
curIntensity=perShock#starting intensity of the participant's shock from the first calibration
win1.setMouseVisible(False)
curRating = 0
intensityDelta = 0
perceptibleShock = 0
end=0
contineRoutine=True

while contineRoutine:
    waitScreen()# a shock will be delivered shortly
    deliverShock(intensity=curIntensity)#send a shock
    win1.flip()
    detectVal = detect()#ask the first question and get their response
    win1.flip()
    ratingVal = ratingScreen()#ask the second question and get their response
    win1.flip()

    if detectVal == 1 and ratingVal == 0:
        print("detect yes and unpleasant no")
        #Save this voltage as the perceptible stim
        perceptibleShock = curIntensity
        end = True
    if detectVal == 0:
        print("detect no")
        intensityDelta = 100#unable to detect it, increase the intensity
        end = False
    if detectVal == 1 and ratingVal== 1:
        print("detect yes and unpleasant yes")
        intensityDelta = -100#unpleasant, decrease the intensity
        end = False

    newIntensity = curIntensity + intensityDelta
    if newIntensity < 2000:         # minimum intensity = 0 V
        newIntensity = 2000
    if newIntensity> 4095:         #maxmimum intensity = 10 v
        newIntensity = 4095
    writeToFile(fileHandle,[subID,curTrial,curIntensity,detectVal, ratingVal, perceptibleShock]) # add these variables to a text file
    curIntensity = newIntensity
    if end == True:
        contineRoutine=False
core.wait(1)
instFunc(text='''Thank you, the testing is complete.''')
allData = pd.read_table('data/'+subID+'_PerceptibleCalibration_2.txt', sep='\t', header=None)#save the text files
perShock = perceptibleShock
win1.close()
