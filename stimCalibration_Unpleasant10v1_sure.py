#Stimulus Calibration Script for Benign and Unpleasant shocks
#Jo Stasiak 2022

import time, sys, random, os, serial, ctypes, numpy
from psychopy import visual, core, event, sound, gui
import pandas as pd
import numpy as np
from scipy import stats
import ctypes
from math import *

from mcculw import ul
from mcculw.enums import InterfaceType, CounterChannelType, DigitalPortType, DigitalIODirection, ULRange
from mcculw.ul import ULError
from mcculw.device_info import DaqDeviceInfo

from psychopy.hardware import joystick
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
import tkinter as tk
from psychopy.hardware import keyboard
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)


# Set some initial values
board_num = 0
devices = ul.get_daq_device_inventory(interface_type)
daq_dev_info = DaqDeviceInfo(board_num)#get the first board it recognizes - check with instacal that it is board '0'
ao_range = ULRange.BIP10VOLTS#the range of shocks our board supports (+/-10V)

ul.a_out(board_num,0, ao_range, data_value =2000)# initialize it to 0 volts

expName='UnpCalibration V1'
userVar = {'Participant':'Enter subject ID'}
dlg = gui.DlgFromDict(userVar, title=expName)
subID = str(userVar['Participant'])
#hand = str(userVar['handedness'])
while os.path.isfile('data/'+subID+'_calibration.txt'):
#    popupError('File exists, enter new subject ID')
    userVar = {'Participant':'Enter subject ID'}
    dlg = gui.DlgFromDict(userVar)
    subID = str(userVar['Participant'])
userVar['expName']=expName
win1 = visual.Window(size=(1275, 975),pos=(270,85), fullscr=False, screen=1, winType='pyglet', allowGUI=True, allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
win1.setMouseVisible(False)
curIntensity = 0 #.25V
defaultKeyboard = keyboard.Keyboard()

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

frameTolerance = 0.001
endExpNow = False

#initialize variables
rating = 0
detectText = "Did you reliably detect a shock?"
ynKey = keyboard.Keyboard()
ratKey = keyboard.Keyboard()
y = "Yes"
n= "No"
sureKey = keyboard.Keyboard()
instructionsText = visual.TextStim(win=win1, text='', height=0.06, pos=[0,0], wrapWidth=1.1, color='white')
space=keyboard.Keyboard()
defaultKeyboard = keyboard.Keyboard()
keyPress=''
#Function to show instructions on screen
def instFunc(text):
    keyPress=''
    win1.setMouseVisible(False)
    continueRoutine = True
    instructionsText.setText(text)
    instructionsText.draw()
    win1.flip()
    if defaultKeyboard.getKeys(keyList=["escape"]):# if we press escape, quit the script
        core.quit()
    event.waitKeys(keyList="space")
    win1.flip()
    if sureKey.getKeys(keyList=['n']):
        keyPress = 1
    if sureKey.getKeys(keyList=['y']):
        keyPress = 2
    return keyPress
rating=2

# grey screen for waiting
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

ratingInstr = visual.TextStim(win1, text= 'Was this shock as unpleasant as you are willing to tolerate?', height=0.08, color='white', pos=[0,0.3], wrapWidth=1.1)
yq=visual.TextStim(win1, text=y, height=0.07, color='black', pos=[-0.25, -0.15])
nq = visual.TextStim(win1, text=n, height=0.07, color='black', pos=[0.25, -0.15])
ratingArray=[0]
ratingVal = 2
#function to ask if the shock was as unpleasant as they are willing to tolerate
def ratingScreen():
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
        ratingInstr.setAutoDraw(True)#draw the text on screen
        yq.setAutoDraw(True)
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
                button_resp.newPressedButtons = [i for i in [0,1] if i in button_resp.pressedButtons]#corresponds to the first 2 joystick buttons
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
    ratingArray.append(button_resp.keys)
    return ratingVal #return their response

def writeToFile(fileHandle,trial,sync=True):#Writes a trial (array of lists) to a file. File needs to be opened outside the function. Pass in the filehandle as an argument
    line = '\t'.join([str(i) for i in trial]) #TABify
    line += '\n'
    fileHandle.write(line)
    if sync:
        fileHandle.flush()
        os.fsync(fileHandle)

########### BEGIN CALIBRATION SCRIPT################################################################
win1.setMouseVisible(False)
instFunc(text='''You will now go through testing to identify an unpleasant level of electrical stimulation that will be used during the task.''')
instFunc(text='''A number of electric shocks will be delivered to your wrist. You will answer if the shock is as unpleasant as you are willing to tolerate.''')
instFunc(text='''We will start with low levels of stimulation and the intensity will gradually increase based on your responses.''')
instFunc(text='''Yes - end calibration\n\nNo - increase intensity''')
instFunc(text='''This shock is intended to be an aversive stimuli that you will want to avoid in the task.''')

instFunc(text='''Do you have any questions?''')

fileHandle = open('data/'+subID+'_UnpleasantCalibration_1.txt','w')#Create a new text file for this calibration
curIntensity=2525#starting intensity of 2.5 volts
win1.setMouseVisible(False)
curRating = 0
intensityDelta = 0
unpleasantShock = 0
end=0
contineRoutine=True

while contineRoutine:
    waitScreen()
    deliverShock(intensity=curIntensity)# give the shock
    win1.flip()
    ratingVal = ratingScreen()# ask the unpleasantness question
    win1.flip()
    if ratingVal == 1: # participants said yes
        print("max unpleasant")
        unpleasantShock = curIntensity
        end = True # end the calibration there
    if ratingVal == 0: # participants said no
        print("not too unpleasant")
        intensityDelta = 50 # increase the shock by 0.25
        end = False # and keep going
    newIntensity = curIntensity + intensityDelta

    if newIntensity> 4095:                           #maximumIntensity =10v
        newIntensity = 4095
        end = True # if they reached the max intensity, end the calibration
    writeToFile(fileHandle,[subID,curTrial,curIntensity,ratingVal, unpleasantShock])# add these variables to a text file
    curIntensity = newIntensity
    if end == True:
        keyPress = instFunc("Are you sure?")
        if keyPress == 1:#Participants said no, not sure
            contineRoutine = True#continue the calibration
        if keyPress == 2:#participants said yes, I am sure
            contineRoutine=False#stop the calibration
core.wait(1)
instFunc(text='''Thank you, the testing is complete.''')

allData = pd.read_table('data/'+subID+'_UnpleasantCalibration_1.txt', sep='\t', header=None)# save the text file
win1.close()
