#Fixation Screen
# jo stasiak

#This is just a single screen that is used to display for participants during the localizer, T1, and gre scans

from __future__ import absolute_import, division
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import os
import sys
import csv
from psychopy.hardware import keyboard
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

fix = visual.TextStim(win=win, text='+', height=0.08,pos=[0,0], color='white')
background = visual.Rect(win=win, width=(1.95, 1.95)[0], height=(1.35, 1.35)[1], ori=0.0, pos=(0, 0),lineWidth=1.0,  colorSpace='rgb',  lineColor='black', fillColor='', opacity=0.99, interpolate=True)

def fixScreen():
    background.draw()
    fix.draw()
    win.flip()
    event.waitKeys(keyList='space')

fixScreen()
