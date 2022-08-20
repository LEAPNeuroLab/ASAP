#Joy test
# jo stasiak

'''
This is a script for the participant to test out the joystick.

They will press the buttons 1,2,3,4 and will then have 15 seconds to use the thumbstick to move a little triangle around the screen.

Then target circles will appear to the participant can practice moving to a specific part of the screen.
'''

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np
from numpy import (sin, cos, tan, log, log10, pi, average,sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os
import sys
import random
import csv
import pandas as pd
from numpy.random import choice
from psychopy.hardware import keyboard
from psychopy.hardware import joystick
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
import ctypes

from math import *
import tkinter as tk
from pyglet.window import key

keyState=key.KeyStateHandler()
prefs.general['audioLib']=['pyo']
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
psychopyVersion = '2021.1.2'
frameTolerance = 0.001

win = visual.Window(size=(1050, 750),pos=(200,50), fullscr=False, screen=1, winType='pyglet', allowGUI=True, allowStencil=True,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',blendMode='avg', useFBO=True, units='height')
win.setMouseVisible(False)

frameRate = win.getActualFrameRate()
if frameRate!= None:
    frameDur = 1.0 / round(frameRate)
else:
    frameDur = 1.0 / 60.0

defaultKeyboard = keyboard.Keyboard()
endExpNow = False

#Set up the joystick_
nJoys = joystick.getNumJoysticks()#Find how many joysticks are connected
id = 0
joy = joystick.Joystick(id)# we will use the first joystick it identifies

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

detectq = visual.TextStim(win, text='', height=0.09, color='white', pos=[0,0])
fix = visual.Polygon(win=win, edges=3, size=(0.04,0.04), fillColor="blue",lineColor='black',lineWidth=2.26, pos=[0,0])
background = visual.Rect(win=win, width=(1.95, 1.95)[0], height=(1.35, 1.35)[1], ori=0.0, pos=(0, 0),lineWidth=1.0,  colorSpace='rgb',  lineColor='black', fillColor='', opacity=0.99, interpolate=True)
joyPicture = visual.ImageStim(win, image = "joystick.png", size=[0.65, 0.75])
targetPlace = visual.Circle(win=win, radius=0.0735, edges=99, lineWidth=1.8, lineColor="black", fillColor="white", pos=[0,0], size=0.7)

#grey screen between instructions
def waitScreen():
    background.draw()
    win.flip()
    event.waitKeys(keyList='space')

#Show a picture of the joystick on the screen
def joyPic():
    background.draw()
    joyPicture.draw()
    win.flip()
    event.waitKeys(keyList='space')

#Function to tell participants to press a joystick button & detect if they were correct
def detect(txt, keysarray):
    continueRoutine = True
    detComponents = [detectq, button_resp, joy]
    for thisComponent in detComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    detClock = core.Clock()
    detClock.reset(-_timeToFirstFrame)
    frameN = -1
    while continueRoutine:
        if detectq.status == NOT_STARTED:
            detectq.setText(txt)#Text on screen telling them what button to press
            detectq.setAutoDraw(True)
        waitOnFlip = False
        if button_resp.status == NOT_STARTED:
            button_resp.frameNStart = frameN
            button_resp.status = STARTED
            win.callOnFlip(button_resp.clock.reset)
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [keysarray] if i in button_resp.pressedButtons]#look for specific button press
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:#if they pressed the right button
                print("these keys = ", theseKeys)
                button_resp.keys = theseKeys[-1]
                button_resp.rt = button_resp.clock.getTime()
                continueRoutine=False#advance the screen
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
            win.flip()
    for thisComponent in detComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
joyClock=core.Clock()

#Function to let the participant move a cursor around
def xyaxistest():
    continueRoutine=True
    joyClock.reset()
    starty = joy.getY()#get initial xy positions
    startx = joy.getX()
    xCoor=0
    yCoor = 0
    while continueRoutine:
        win.setMouseVisible(False)
        fix.draw()
        if joy.getX()>startx + 0.0002:# if joystick was moved past its initial x position, let it move right
            xCoor += 0.0320 # this is the speed at which it moves, to make it slower, make this number lower
        if joy.getX()<-startx - 0.0002:# if joystick was moved past its initial x position, let it move left
            xCoor -= 0.0320
        if joy.getY() >starty + 0.0002:# if joystick was moved past its initial y position, let it move down
            yCoor -= 0.0320
        if joy.getY() <-starty - 0.0002:# if joystick was moved past its initial y position, let it move up
            yCoor += 0.0320
        if yCoor <= (-0.482):#don't let the cursor run off the screen; if it reaches this coordinate, don't let it go further down
            yCoor=-0.482
        if yCoor >= 0.47:#don't let the cursor run off the screen; if it reaches this coordinate, don't let it go further up
            yCoor=0.47
        if xCoor <= -0.683:#don't let the cursor run off the screen; if it reaches this coordinate, don't let it go further left
            xCoor=-0.683
        if xCoor >=0.683:#don't let the cursor run off the screen; if it reaches this coordinate, don't let it go further right
            xCoor=0.683
        if continueRoutine:
            win.flip()
        fix.setPos((xCoor,yCoor))#update the cursor every frame
        if joyClock.getTime() >= 15.00:#they have 15 seconds to move it around
            continueRoutine=False
            win.flip()
#Function for displaying a target circle and having the participant move the cursor to the circle
def xyaxistestTarget(location):
    continueRoutine=True
    joyClock.reset()
    starty = joy.getY()
    startx = joy.getX()
    xCoor=0
    yCoor = 0
    while continueRoutine:
        win.setMouseVisible(False)
        targetPlace.setPos(location)#set the target circle at a specific location on the screen
        targetPlace.draw()# draw the target circle
        fix.draw()#draw the cursor
        if joy.getX()>startx + 0.0002:
            xCoor += 0.0320
        if joy.getX()<-startx - 0.0002:
            xCoor -= 0.0320
        if joy.getY() >starty + 0.0002:
            yCoor -= 0.0320
        if joy.getY() <-starty - 0.0002:
            yCoor += 0.0320
        if yCoor <= (-0.482):
            yCoor=-0.482
        if yCoor >= 0.47:
            yCoor=0.47
        if xCoor <= -0.683:
            xCoor=-0.683
        if xCoor >=0.683:
            xCoor=0.683
        if continueRoutine:
            win.flip()
        fix.setPos((xCoor,yCoor))#update the cursor every frame
        if joyClock.getTime() >= 8.00:#they have 8 seconds to move to the target circle
            continueRoutine=False
            win.flip()

waitScreen()
joyPic()#show picture of the joystick
textArray=['Please press 1', 'Please press 2', 'Please press 3', 'Please press 4']
keyArray=[0,1,2,3]
for spam, eggs in zip(textArray, keyArray):#have them press all 4 buttons on the joystick
    detect(spam, eggs)# the screen won't advance unless they click the right button
    waitScreen()

xyaxistest()#have them practice moving the cursor around

waitScreen()

t1=((-0.582, 0.43))#top left location
t2=((-0.582, -0.43))#bottom left location
t3=((0.582, 0.43))#top right location
t4=((0.582, -0.43))#bottom right location

xyaxistestTarget(t1)#set circle in top left
xyaxistestTarget(t2) # set circle in bottom left
xyaxistestTarget(t3)# set circle in top right
xyaxistestTarget(t4)# set circle to bottom right

waitScreen()
