#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 08, 2022, at 13:54
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'AA_task'  # from the Builder filename that created this script
expInfo = {'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\rcl-labadmin\\Desktop\\Jingyi\\AA_fMRI\\007\\AA_task_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joyButtons import virtualJoyButtons as virtualjoybuttonslib
from psychopy.hardware import joystick as joysticklib  # joystick/gamepad accsss
from psychopy.experiment.components.joystick import virtualJoystick as virtualjoysticklib

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='BIC_monitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='deg')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "WaitParticipant"
WaitParticipantClock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='We will start the instruction and practice shortly',
    font='Open Sans',
    pos=(0, 0), height=1.0, wrapWidth=30.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# function for visual angle calculator 
def visual_angle(x,d):
    a = (2*np.arctan(x/(2*d))/np.pi)*360
    return a
#w=0.7
#h=0.525
w=visual_angle(8, 90)
h=visual_angle(6, 90)
#image.setSize([w,h])
image_size=[w, h]
t_joyMoveonset=0

timer = core.Clock()
#from psychopy import parallel
#port = parallel.ParallelPort(address='0x2FE8')
#port.setData(0)

# For Biopac 
# eeg_port = parallel.ParallelPort(address='0x2FE8') 

# For EEG, using physical port 1
#eeg_port = parallel.ParallelPort(address='0x3FF8')
# Port 1 3FF8 (LPT1)
# Port 2 3FE8 (LPT4)
# Port 3 2FF8 (LPT2)
# Port 4 2FE8 (LPT3)
from psychopy.hardware import joystick
import serial.tools.list_ports
ports = serial.tools.list_ports.comports()
for port, desc, hwid in sorted(ports):
    print("{}: {} [{}]".format(port, desc,hwid))
import serial

from psychopy import core
import pylink
import os
import platform
import random
import time
import sys
from EyeLinkCoreGraphicsPsychoPy import EyeLinkCoreGraphicsPsychoPy
from psychopy import visual, core, event, monitors, gui
from PIL import Image  # for preparing the Host backdrop image
from string import ascii_letters, digits

# Set this variable to True if you use the built-in retina screen as your
# primary display device on macOS. If have an external monitor, set this
# variable True if you choose to "Optimize for Built-in Retina Display"
# in the Displays preference settings.
use_retina = False

# Set this variable to True to run the script in "Dummy Mode"
dummy_mode = False

# Set up EDF data file name and local data folder
#
# The EDF data filename should not exceed 8 alphanumeric characters
# use ONLY number 0-9, letters, & _ (underscore) in the filename
edf_fname = str(int(expInfo['participant'][-1]))

# Set up a folder to store the EDF data files and the associated resources
# e.g., files defining the interest areas used in each trial
results_folder = 'eyelink'
if not os.path.exists(results_folder):
    os.makedirs(results_folder)
    

# Step 1: Connect to the EyeLink Host PC
#
# The Host IP address, by default, is "100.1.1.1".
# the "el_tracker" objected created here can be accessed through the Pylink
# Set the Host PC address to "None" (without quotes) to run the script
# in "Dummy Mode"
if dummy_mode:
    el_tracker = pylink.EyeLink(None)
else:
    try:
        el_tracker = pylink.EyeLink("100.1.1.1")
    except RuntimeError as error:
        print('ERROR:', error)
        core.quit()
        sys.exit()

# Step 3: Configure the tracker
#
# Put the tracker in offline mode before we change tracking parameters
el_tracker.setOfflineMode()

# Get the software version:  1-EyeLink I, 2-EyeLink II, 3/4-EyeLink 1000,
# 5-EyeLink 1000 Plus, 6-Portable DUO
eyelink_ver = 0  # set version to 0, in case running in Dummy mode
if not dummy_mode:
    vstr = el_tracker.getTrackerVersionString()
    eyelink_ver = int(vstr.split()[-1].split('.')[0])
    # print out some version info in the shell
    print('Running experiment on %s, version %d' % (vstr, eyelink_ver))

# File and Link data control
# what eye events to save in the EDF file, include everything by default
file_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT'
# what eye events to make available over the link, include everything by default
link_event_flags = 'LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON,FIXUPDATE,INPUT'
# what sample data to save in the EDF data file and to make available
# over the link, include the 'HTARGET' flag to save head target sticker
# data for supported eye trackers
if eyelink_ver > 3:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,HTARGET,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,HTARGET,STATUS,INPUT'
else:
    file_sample_flags = 'LEFT,RIGHT,GAZE,HREF,RAW,AREA,GAZERES,BUTTON,STATUS,INPUT'
    link_sample_flags = 'LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,INPUT'
el_tracker.sendCommand("file_event_filter = %s" % file_event_flags)
el_tracker.sendCommand("file_sample_data = %s" % file_sample_flags)
el_tracker.sendCommand("link_event_filter = %s" % link_event_flags)
el_tracker.sendCommand("link_sample_data = %s" % link_sample_flags)

# get the native screen resolution used by PsychoPy
scn_width, scn_height = win.size
def clear_screen(win):
    """ clear up the PsychoPy window"""

#    win.fillColor = genv.getBackgroundColor()
    win.flip()
    
def show_msg(win, text, wait_for_keypress=True):
    """ Show task instructions on screen"""

    msg = visual.TextStim(win, text,font='Open Sans',pos=(0, 0), height=1.0, wrapWidth=20, ori=0.0, color='white', colorSpace='rgb', opacity=None, languageStyle='LTR',depth=0.0)
    clear_screen(win)
    msg.draw()
    win.flip()

    # wait indefinitely, terminates upon any key press
    if wait_for_keypress:
        event.waitKeys()
        clear_screen(win)

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_welcome = visual.TextStim(win=win, name='text_welcome',
    text='Welcome to our experiment! \n \nOur experiment contains two parts: a joystick moving experiment followed by decision-making tasks. To begin, you will be presented with instructions for the first task. Please take your time to read the instructions carefully. \n\n \n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_welcome_key = visual.TextStim(win=win, name='text_welcome_key',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
button_resp_2 = type('', (), {})() # Create an object to use as a name space
button_resp_2.device = None
button_resp_2.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_2.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_2.device = joystickCache[0]
    else:
        button_resp_2.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_2.device_number))
except Exception:
    pass
    
if not button_resp_2.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_2.status = None
button_resp_2.clock = core.Clock()
button_resp_2.numButtons = button_resp_2.device.getNumButtons()


# Initialize components for Routine "Instr_1"
Instr_1Clock = core.Clock()
text_Instr_1 = visual.TextStim(win=win, name='text_Instr_1',
    text='In the first task, you will first see a gray screen and then see two different categories of emotional images:\n\nPOSITIVE    NEGATIVE \n\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Instr_1_key = visual.TextStim(win=win, name='text_Instr_1_key',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
button_resp_3 = type('', (), {})() # Create an object to use as a name space
button_resp_3.device = None
button_resp_3.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_3.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_3.device = joystickCache[0]
    else:
        button_resp_3.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_3.device_number))
except Exception:
    pass
    
if not button_resp_3.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_3.status = None
button_resp_3.clock = core.Clock()
button_resp_3.numButtons = button_resp_3.device.getNumButtons()


# Initialize components for Routine "Instr_2"
Instr_2Clock = core.Clock()
text_Instr_2 = visual.TextStim(win=win, name='text_Instr_2',
    text='This task contains several blocks.\n\nIn each block, you will first see an instruction. This instruction indicates the direction of the joystick movement for the following rounds of tasks. \n\nThen you will be presented with several images, one at a time. Your task is to move the joystick towards yourself or away from yourself AS FAST AS YOU CAN whenever you see the image, as instructed.\n\n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Instr_2_key = visual.TextStim(win=win, name='text_Instr_2_key',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
button_resp_4 = type('', (), {})() # Create an object to use as a name space
button_resp_4.device = None
button_resp_4.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_4.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_4.device = joystickCache[0]
    else:
        button_resp_4.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_4.device_number))
except Exception:
    pass
    
if not button_resp_4.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_4.status = None
button_resp_4.clock = core.Clock()
button_resp_4.numButtons = button_resp_4.device.getNumButtons()


# Initialize components for Routine "Instr_3"
Instr_3Clock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='If you move the joystick towards yourself the image on the screen will enlarge. \n\nIf you move the joystick away from yourself the image on the screen will shrink. \n\nAfter the joystick movement, please LET GO of the joystick but still KEEP YOUR HAND ON THE JOYSTICK, so that it goes back to the center. \n\nPlease move your joystick to control the size of the image in the next page. ',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
button_resp_9 = type('', (), {})() # Create an object to use as a name space
button_resp_9.device = None
button_resp_9.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_9.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_9.device = joystickCache[0]
    else:
        button_resp_9.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_9.device_number))
except Exception:
    pass
    
if not button_resp_9.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_9.status = None
button_resp_9.clock = core.Clock()
button_resp_9.numButtons = button_resp_9.device.getNumButtons()


# Initialize components for Routine "Practice_joy"
Practice_joyClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='7021.jpg', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color='white', colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
x, y = [None, None]
joystick_2 = type('', (), {})() # Create an object to use as a name space
joystick_2.device = None
joystick_2.device_number = 0
joystick_2.joystickClock = core.Clock()
joystick_2.xFactor = 1
joystick_2.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_2.device = joystickCache[0]
        if win.units == 'height':
            joystick_2.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_2.yFactor = 0.5
    else:
        joystick_2.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_2.device_number))
except Exception:
    pass
    
if not joystick_2.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_2.status = None
joystick_2.clock = core.Clock()
joystick_2.numButtons = joystick_2.device.getNumButtons()
joystick_2.getNumButtons = joystick_2.device.getNumButtons
joystick_2.getAllButtons = joystick_2.device.getAllButtons
joystick_2.getX = lambda: joystick_2.xFactor * joystick_2.device.getX()
joystick_2.getY = lambda: joystick_2.yFactor * joystick_2.device.getY()

button_resp_8 = type('', (), {})() # Create an object to use as a name space
button_resp_8.device = None
button_resp_8.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_8.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_8.device = joystickCache[0]
    else:
        button_resp_8.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_8.device_number))
except Exception:
    pass
    
if not button_resp_8.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_8.status = None
button_resp_8.clock = core.Clock()
button_resp_8.numButtons = button_resp_8.device.getNumButtons()

text_6 = visual.TextStim(win=win, name='text_6',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-4.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='Please move the joystick.',
    font='Open Sans',
    pos=(0, 6.5), height=0.9, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "Instr_4"
Instr_4Clock = core.Clock()
text_Instr_3 = visual.TextStim(win=win, name='text_Instr_3',
    text='There are two types of instructions:\n\nPlease pull the joystick TOWARDS yourself if you see a NEGATIVE image, or pull the joystick AWAY from you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes.\n\nOR\n\nPlease pull the joystick AWAY from yourself if you see a NEGATIVE image, or pull the joystick TOWARDS you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes.\n',
    font='Open Sans',
    pos=(0, 0), height=0.7, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Instr_3_key = visual.TextStim(win=win, name='text_Instr_3_key',
    text='Press the “middle key" to continue.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
button_resp_5 = type('', (), {})() # Create an object to use as a name space
button_resp_5.device = None
button_resp_5.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_5.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_5.device = joystickCache[0]
    else:
        button_resp_5.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_5.device_number))
except Exception:
    pass
    
if not button_resp_5.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_5.status = None
button_resp_5.clock = core.Clock()
button_resp_5.numButtons = button_resp_5.device.getNumButtons()


# Initialize components for Routine "Instr_5"
Instr_5Clock = core.Clock()
text_Instr_4 = visual.TextStim(win=win, name='text_Instr_4',
    text='Next, you will be able to practice this task with some sample images.\n\nNote that if you failed in 20% of rounds, we will ask you to go through this practice run again.\n\nPlease keep your hand on the joystick at all times. ',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_Instr_4_key = visual.TextStim(win=win, name='text_Instr_4_key',
    text='Press the “middle key" when you are ready to begin the practice.',
    font='Open Sans',
    pos=(0, -6.5), height=0.8, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
if int(expInfo['participant'][-1]) % 2 == 0:
    PracRun_order = "CondPractice_taskcontrol1.csv"
else:
    PracRun_order = "CondPractice_taskcontrol2.csv"
button_resp_6 = type('', (), {})() # Create an object to use as a name space
button_resp_6.device = None
button_resp_6.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp_6.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp_6.device = joystickCache[0]
    else:
        button_resp_6.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp_6.device_number))
except Exception:
    pass
    
if not button_resp_6.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp_6.status = None
button_resp_6.clock = core.Clock()
button_resp_6.numButtons = button_resp_6.device.getNumButtons()


# Initialize components for Routine "GrayScreenPrac"
GrayScreenPracClock = core.Clock()
CrossPrac = visual.TextStim(win=win, name='CrossPrac',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice_Cong_instr"
Practice_Cong_instrClock = core.Clock()
text_Cong_PracInstr = visual.TextStim(win=win, name='text_Cong_PracInstr',
    text='Please pull the joystick AWAY from yourself if you see a NEGATIVE image, or pull the joystick TOWARDS you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes.\n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Practice_Cong_trial"
Practice_Cong_trialClock = core.Clock()
fix_1 = visual.TextStim(win=win, name='fix_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ITI_prac = visual.TextStim(win=win, name='ITI_prac',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
x, y = [None, None]
joystick_prac = type('', (), {})() # Create an object to use as a name space
joystick_prac.device = None
joystick_prac.device_number = 0
joystick_prac.joystickClock = core.Clock()
joystick_prac.xFactor = 1
joystick_prac.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_prac.device = joystickCache[0]
        if win.units == 'height':
            joystick_prac.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_prac.yFactor = 0.5
    else:
        joystick_prac.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_prac.device_number))
except Exception:
    pass
    
if not joystick_prac.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_prac.status = None
joystick_prac.clock = core.Clock()
joystick_prac.numButtons = joystick_prac.device.getNumButtons()
joystick_prac.getNumButtons = joystick_prac.device.getNumButtons
joystick_prac.getAllButtons = joystick_prac.device.getAllButtons
joystick_prac.getX = lambda: joystick_prac.xFactor * joystick_prac.device.getX()
joystick_prac.getY = lambda: joystick_prac.yFactor * joystick_prac.device.getY()

li_correct_prac = []


# Initialize components for Routine "GrayScreenPrac"
GrayScreenPracClock = core.Clock()
CrossPrac = visual.TextStim(win=win, name='CrossPrac',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Practice_Incong_instr"
Practice_Incong_instrClock = core.Clock()
text_Incong_PracInstr = visual.TextStim(win=win, name='text_Incong_PracInstr',
    text='Please pull the joystick TOWARDS yourself if you see a NEGATIVE image, or pull the joystick AWAY from you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes.',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "Practice_Incong_trial_2"
Practice_Incong_trial_2Clock = core.Clock()
fix_2 = visual.TextStim(win=win, name='fix_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ITI_prac_2 = visual.TextStim(win=win, name='ITI_prac_2',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
x, y = [None, None]
joystick_prac_2 = type('', (), {})() # Create an object to use as a name space
joystick_prac_2.device = None
joystick_prac_2.device_number = 0
joystick_prac_2.joystickClock = core.Clock()
joystick_prac_2.xFactor = 1
joystick_prac_2.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick_prac_2.device = joystickCache[0]
        if win.units == 'height':
            joystick_prac_2.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick_prac_2.yFactor = 0.5
    else:
        joystick_prac_2.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick_prac_2.device_number))
except Exception:
    pass
    
if not joystick_prac_2.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick_prac_2.status = None
joystick_prac_2.clock = core.Clock()
joystick_prac_2.numButtons = joystick_prac_2.device.getNumButtons()
joystick_prac_2.getNumButtons = joystick_prac_2.device.getNumButtons
joystick_prac_2.getAllButtons = joystick_prac_2.device.getAllButtons
joystick_prac_2.getX = lambda: joystick_prac_2.xFactor * joystick_prac_2.device.getX()
joystick_prac_2.getY = lambda: joystick_prac_2.yFactor * joystick_prac_2.device.getY()


# Initialize components for Routine "Prac_instr"
Prac_instrClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='You did not reach 80% correct rate. We will run through this practice round again. \n \nPlease keep your hand on the joystick at all times. \n\nPress the “middle key" when you are ready to begin the practice.  \n\n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
button_resp = type('', (), {})() # Create an object to use as a name space
button_resp.device = None
button_resp.device_number = 0

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        button_resp.device = joysticklib.Joystick(0)
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        button_resp.device = joystickCache[0]
    else:
        button_resp.device = virtualjoybuttonslib.VirtualJoyButtons(0)
        logging.warning("joystick_{}: Using keyboard emulation 'ctrl' + 'Alt' + digit.".format(button_resp.device_number))
except Exception:
    pass
    
if not button_resp.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

button_resp.status = None
button_resp.clock = core.Clock()
button_resp.numButtons = button_resp.device.getNumButtons()


# Initialize components for Routine "LastCheckBeforeStart"
LastCheckBeforeStartClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='The experimenter will be with you shortly',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "fixation_1"
fixation_1Clock = core.Clock()
fixation = visual.TextStim(win=win, name='fixation',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "eyelink"
eyelinkClock = core.Clock()

# Initialize components for Routine "fMRItriger"
fMRItrigerClock = core.Clock()

# Initialize components for Routine "GrayScreen20s"
GrayScreen20sClock = core.Clock()
GrayScreent = visual.TextStim(win=win, name='GrayScreent',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BlockInstr"
BlockInstrClock = core.Clock()
Instruction_1 = visual.TextStim(win=win, name='Instruction_1',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "main_trial"
main_trialClock = core.Clock()
fix = visual.TextStim(win=win, name='fix',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
ITI_1 = visual.TextStim(win=win, name='ITI_1',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=2.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
correct = ""
x, y = [None, None]
joystick = type('', (), {})() # Create an object to use as a name space
joystick.device = None
joystick.device_number = 0
joystick.joystickClock = core.Clock()
joystick.xFactor = 1
joystick.yFactor = 1

try:
    numJoysticks = joysticklib.getNumJoysticks()
    if numJoysticks > 0:
        try:
            joystickCache
        except NameError:
            joystickCache={}
        if not 0 in joystickCache:
            joystickCache[0] = joysticklib.Joystick(0)
        joystick.device = joystickCache[0]
        if win.units == 'height':
            joystick.xFactor = 0.5 * win.size[0]/win.size[1]
            joystick.yFactor = 0.5
    else:
        joystick.device = virtualjoysticklib.VirtualJoystick(0)
        logging.warning("joystick_{}: Using keyboard+mouse emulation 'ctrl' + 'Alt' + digit.".format(joystick.device_number))
except Exception:
    pass
    
if not joystick.device:
    logging.error('No joystick/gamepad device found.')
    core.quit()

joystick.status = None
joystick.clock = core.Clock()
joystick.numButtons = joystick.device.getNumButtons()
joystick.getNumButtons = joystick.device.getNumButtons
joystick.getAllButtons = joystick.device.getAllButtons
joystick.getX = lambda: joystick.xFactor * joystick.device.getX()
joystick.getY = lambda: joystick.yFactor * joystick.device.getY()


# Initialize components for Routine "GrayScreen20s"
GrayScreen20sClock = core.Clock()
GrayScreent = visual.TextStim(win=win, name='GrayScreent',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "RCheck"
RCheckClock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='The experimenter will be with you shortly. \n\n',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "EndAA"
EndAAClock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='Thank you for finishing the joystick experiment. The experimenter will be with you shortly. ',
    font='Open Sans',
    pos=(0, 0), height=0.9, wrapWidth=20.0, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WaitParticipant"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
WaitParticipantComponents = [text_22, key_resp_5]
for thisComponent in WaitParticipantComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
WaitParticipantClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "WaitParticipant"-------
while continueRoutine:
    # get current time
    t = WaitParticipantClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=WaitParticipantClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WaitParticipantComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WaitParticipant"-------
for thisComponent in WaitParticipantComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "WaitParticipant" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
win.mouseVisible = False
button_resp_2.oldButtonState = button_resp_2.device.getAllButtons()[:]
button_resp_2.keys = []
button_resp_2.rt = []
# keep track of which components have finished
welcomeComponents = [text_welcome, text_welcome_key, button_resp_2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_welcome* updates
    if text_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome.frameNStart = frameN  # exact frame index
        text_welcome.tStart = t  # local t and not account for scr refresh
        text_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome, 'tStartRefresh')  # time at next scr refresh
        text_welcome.setAutoDraw(True)
    
    # *text_welcome_key* updates
    if text_welcome_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_welcome_key.frameNStart = frameN  # exact frame index
        text_welcome_key.tStart = t  # local t and not account for scr refresh
        text_welcome_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_welcome_key, 'tStartRefresh')  # time at next scr refresh
        text_welcome_key.setAutoDraw(True)
    
    # *button_resp_2* updates
    if button_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_2.frameNStart = frameN  # exact frame index
        button_resp_2.tStart = t  # local t and not account for scr refresh
        button_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_2, 'tStartRefresh')  # time at next scr refresh
        button_resp_2.status = STARTED
        # joyButtons checking is just starting
    if button_resp_2.status == STARTED:
        button_resp_2.newButtonState = button_resp_2.device.getAllButtons()[:]
        button_resp_2.pressedButtons = []
        button_resp_2.releasedButtons = []
        button_resp_2.newPressedButtons = []
        if button_resp_2.newButtonState != button_resp_2.oldButtonState:
            button_resp_2.pressedButtons = [i for i in range(button_resp_2.numButtons) if button_resp_2.newButtonState[i] and not button_resp_2.oldButtonState[i]]
            button_resp_2.releasedButtons = [i for i in range(button_resp_2.numButtons) if not button_resp_2.newButtonState[i] and button_resp_2.oldButtonState[i]]
            button_resp_2.oldButtonState = button_resp_2.newButtonState
            button_resp_2.newPressedButtons = [i for i in [0] if i in button_resp_2.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_2.device_number,i)) for i in button_resp_2.pressedButtons]
        theseKeys = button_resp_2.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_1"-------
continueRoutine = True
# update component parameters for each repeat
button_resp_3.oldButtonState = button_resp_3.device.getAllButtons()[:]
button_resp_3.keys = []
button_resp_3.rt = []
# keep track of which components have finished
Instr_1Components = [text_Instr_1, text_Instr_1_key, button_resp_3]
for thisComponent in Instr_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_1"-------
while continueRoutine:
    # get current time
    t = Instr_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instr_1* updates
    if text_Instr_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_1.frameNStart = frameN  # exact frame index
        text_Instr_1.tStart = t  # local t and not account for scr refresh
        text_Instr_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_1, 'tStartRefresh')  # time at next scr refresh
        text_Instr_1.setAutoDraw(True)
    
    # *text_Instr_1_key* updates
    if text_Instr_1_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_1_key.frameNStart = frameN  # exact frame index
        text_Instr_1_key.tStart = t  # local t and not account for scr refresh
        text_Instr_1_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_1_key, 'tStartRefresh')  # time at next scr refresh
        text_Instr_1_key.setAutoDraw(True)
    
    # *button_resp_3* updates
    if button_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_3.frameNStart = frameN  # exact frame index
        button_resp_3.tStart = t  # local t and not account for scr refresh
        button_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_3, 'tStartRefresh')  # time at next scr refresh
        button_resp_3.status = STARTED
        # joyButtons checking is just starting
    if button_resp_3.status == STARTED:
        button_resp_3.newButtonState = button_resp_3.device.getAllButtons()[:]
        button_resp_3.pressedButtons = []
        button_resp_3.releasedButtons = []
        button_resp_3.newPressedButtons = []
        if button_resp_3.newButtonState != button_resp_3.oldButtonState:
            button_resp_3.pressedButtons = [i for i in range(button_resp_3.numButtons) if button_resp_3.newButtonState[i] and not button_resp_3.oldButtonState[i]]
            button_resp_3.releasedButtons = [i for i in range(button_resp_3.numButtons) if not button_resp_3.newButtonState[i] and button_resp_3.oldButtonState[i]]
            button_resp_3.oldButtonState = button_resp_3.newButtonState
            button_resp_3.newPressedButtons = [i for i in [0] if i in button_resp_3.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_3.device_number,i)) for i in button_resp_3.pressedButtons]
        theseKeys = button_resp_3.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_1"-------
for thisComponent in Instr_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Instr_1_key.started', text_Instr_1_key.tStartRefresh)
thisExp.addData('text_Instr_1_key.stopped', text_Instr_1_key.tStopRefresh)
# the Routine "Instr_1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_2"-------
continueRoutine = True
# update component parameters for each repeat
button_resp_4.oldButtonState = button_resp_4.device.getAllButtons()[:]
button_resp_4.keys = []
button_resp_4.rt = []
# keep track of which components have finished
Instr_2Components = [text_Instr_2, text_Instr_2_key, button_resp_4]
for thisComponent in Instr_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_2"-------
while continueRoutine:
    # get current time
    t = Instr_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instr_2* updates
    if text_Instr_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_2.frameNStart = frameN  # exact frame index
        text_Instr_2.tStart = t  # local t and not account for scr refresh
        text_Instr_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_2, 'tStartRefresh')  # time at next scr refresh
        text_Instr_2.setAutoDraw(True)
    
    # *text_Instr_2_key* updates
    if text_Instr_2_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_2_key.frameNStart = frameN  # exact frame index
        text_Instr_2_key.tStart = t  # local t and not account for scr refresh
        text_Instr_2_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_2_key, 'tStartRefresh')  # time at next scr refresh
        text_Instr_2_key.setAutoDraw(True)
    
    # *button_resp_4* updates
    if button_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_4.frameNStart = frameN  # exact frame index
        button_resp_4.tStart = t  # local t and not account for scr refresh
        button_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_4, 'tStartRefresh')  # time at next scr refresh
        button_resp_4.status = STARTED
        # joyButtons checking is just starting
    if button_resp_4.status == STARTED:
        button_resp_4.newButtonState = button_resp_4.device.getAllButtons()[:]
        button_resp_4.pressedButtons = []
        button_resp_4.releasedButtons = []
        button_resp_4.newPressedButtons = []
        if button_resp_4.newButtonState != button_resp_4.oldButtonState:
            button_resp_4.pressedButtons = [i for i in range(button_resp_4.numButtons) if button_resp_4.newButtonState[i] and not button_resp_4.oldButtonState[i]]
            button_resp_4.releasedButtons = [i for i in range(button_resp_4.numButtons) if not button_resp_4.newButtonState[i] and button_resp_4.oldButtonState[i]]
            button_resp_4.oldButtonState = button_resp_4.newButtonState
            button_resp_4.newPressedButtons = [i for i in [0] if i in button_resp_4.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_4.device_number,i)) for i in button_resp_4.pressedButtons]
        theseKeys = button_resp_4.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_2"-------
for thisComponent in Instr_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Instr_2.started', text_Instr_2.tStartRefresh)
thisExp.addData('text_Instr_2.stopped', text_Instr_2.tStopRefresh)
thisExp.addData('text_Instr_2_key.started', text_Instr_2_key.tStartRefresh)
thisExp.addData('text_Instr_2_key.stopped', text_Instr_2_key.tStopRefresh)
# the Routine "Instr_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_3"-------
continueRoutine = True
# update component parameters for each repeat
button_resp_9.oldButtonState = button_resp_9.device.getAllButtons()[:]
button_resp_9.keys = []
button_resp_9.rt = []
# keep track of which components have finished
Instr_3Components = [text_4, text_5, button_resp_9]
for thisComponent in Instr_3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_3"-------
while continueRoutine:
    # get current time
    t = Instr_3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *button_resp_9* updates
    if button_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_9.frameNStart = frameN  # exact frame index
        button_resp_9.tStart = t  # local t and not account for scr refresh
        button_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_9, 'tStartRefresh')  # time at next scr refresh
        button_resp_9.status = STARTED
        # joyButtons checking is just starting
    if button_resp_9.status == STARTED:
        button_resp_9.newButtonState = button_resp_9.device.getAllButtons()[:]
        button_resp_9.pressedButtons = []
        button_resp_9.releasedButtons = []
        button_resp_9.newPressedButtons = []
        if button_resp_9.newButtonState != button_resp_9.oldButtonState:
            button_resp_9.pressedButtons = [i for i in range(button_resp_9.numButtons) if button_resp_9.newButtonState[i] and not button_resp_9.oldButtonState[i]]
            button_resp_9.releasedButtons = [i for i in range(button_resp_9.numButtons) if not button_resp_9.newButtonState[i] and button_resp_9.oldButtonState[i]]
            button_resp_9.oldButtonState = button_resp_9.newButtonState
            button_resp_9.newPressedButtons = [i for i in [0] if i in button_resp_9.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_9.device_number,i)) for i in button_resp_9.pressedButtons]
        theseKeys = button_resp_9.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_3"-------
for thisComponent in Instr_3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
# the Routine "Instr_3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Practice_joy"-------
continueRoutine = True
# update component parameters for each repeat
joystick_2.oldButtonState = joystick_2.device.getAllButtons()[:]
joystick_2.activeButtons=[i for i in range(joystick_2.numButtons)]
# setup some python lists for storing info about the joystick_2
gotValidClick = False  # until a click is received
button_resp_8.oldButtonState = button_resp_8.device.getAllButtons()[:]
button_resp_8.keys = []
button_resp_8.rt = []
# keep track of which components have finished
Practice_joyComponents = [image_5, joystick_2, button_resp_8, text_6, text_7]
for thisComponent in Practice_joyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Practice_joyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Practice_joy"-------
while continueRoutine:
    # get current time
    t = Practice_joyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Practice_joyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    if image_5.status == STARTED:  # only update if drawing
        image_5.setColor([1,1,1], colorSpace='rgb', log=False)
        image_5.setSize(image_size, log=False)
    joy_reading = joystick_2.getY()
    
    if joy_reading >= -0.2 and joy_reading <= 0.2:
        image_size = [w, h]
    elif joy_reading < -0.2:
        w1=w*0.3
        h1=h*0.3
        image_size = [w1, h1]
    #    image.setSize([w,h])
    elif joy_reading > 0.2:
    #    image_size = (0.64, 0.48)
        w1=w*2
        h1=h*2
        image_size = [w1, h1]
    
    # *button_resp_8* updates
    if button_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_8.frameNStart = frameN  # exact frame index
        button_resp_8.tStart = t  # local t and not account for scr refresh
        button_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_8, 'tStartRefresh')  # time at next scr refresh
        button_resp_8.status = STARTED
        # joyButtons checking is just starting
    if button_resp_8.status == STARTED:
        button_resp_8.newButtonState = button_resp_8.device.getAllButtons()[:]
        button_resp_8.pressedButtons = []
        button_resp_8.releasedButtons = []
        button_resp_8.newPressedButtons = []
        if button_resp_8.newButtonState != button_resp_8.oldButtonState:
            button_resp_8.pressedButtons = [i for i in range(button_resp_8.numButtons) if button_resp_8.newButtonState[i] and not button_resp_8.oldButtonState[i]]
            button_resp_8.releasedButtons = [i for i in range(button_resp_8.numButtons) if not button_resp_8.newButtonState[i] and button_resp_8.oldButtonState[i]]
            button_resp_8.oldButtonState = button_resp_8.newButtonState
            button_resp_8.newPressedButtons = [i for i in [0] if i in button_resp_8.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_8.device_number,i)) for i in button_resp_8.pressedButtons]
        theseKeys = button_resp_8.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Practice_joyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Practice_joy"-------
for thisComponent in Practice_joyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
# store data for thisExp (ExperimentHandler)
thisExp.addData('joystick_2.started', joystick_2.tStart)
thisExp.addData('joystick_2.stopped', joystick_2.tStop)
thisExp.nextEntry()
# the Routine "Practice_joy" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_4"-------
continueRoutine = True
# update component parameters for each repeat
button_resp_5.oldButtonState = button_resp_5.device.getAllButtons()[:]
button_resp_5.keys = []
button_resp_5.rt = []
# keep track of which components have finished
Instr_4Components = [text_Instr_3, text_Instr_3_key, button_resp_5]
for thisComponent in Instr_4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_4"-------
while continueRoutine:
    # get current time
    t = Instr_4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instr_3* updates
    if text_Instr_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_3.frameNStart = frameN  # exact frame index
        text_Instr_3.tStart = t  # local t and not account for scr refresh
        text_Instr_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_3, 'tStartRefresh')  # time at next scr refresh
        text_Instr_3.setAutoDraw(True)
    
    # *text_Instr_3_key* updates
    if text_Instr_3_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_3_key.frameNStart = frameN  # exact frame index
        text_Instr_3_key.tStart = t  # local t and not account for scr refresh
        text_Instr_3_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_3_key, 'tStartRefresh')  # time at next scr refresh
        text_Instr_3_key.setAutoDraw(True)
    
    # *button_resp_5* updates
    if button_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_5.frameNStart = frameN  # exact frame index
        button_resp_5.tStart = t  # local t and not account for scr refresh
        button_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_5, 'tStartRefresh')  # time at next scr refresh
        button_resp_5.status = STARTED
        # joyButtons checking is just starting
    if button_resp_5.status == STARTED:
        button_resp_5.newButtonState = button_resp_5.device.getAllButtons()[:]
        button_resp_5.pressedButtons = []
        button_resp_5.releasedButtons = []
        button_resp_5.newPressedButtons = []
        if button_resp_5.newButtonState != button_resp_5.oldButtonState:
            button_resp_5.pressedButtons = [i for i in range(button_resp_5.numButtons) if button_resp_5.newButtonState[i] and not button_resp_5.oldButtonState[i]]
            button_resp_5.releasedButtons = [i for i in range(button_resp_5.numButtons) if not button_resp_5.newButtonState[i] and button_resp_5.oldButtonState[i]]
            button_resp_5.oldButtonState = button_resp_5.newButtonState
            button_resp_5.newPressedButtons = [i for i in [0] if i in button_resp_5.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_5.device_number,i)) for i in button_resp_5.pressedButtons]
        theseKeys = button_resp_5.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_4"-------
for thisComponent in Instr_4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Instr_3.started', text_Instr_3.tStartRefresh)
thisExp.addData('text_Instr_3.stopped', text_Instr_3.tStopRefresh)
thisExp.addData('text_Instr_3_key.started', text_Instr_3_key.tStartRefresh)
thisExp.addData('text_Instr_3_key.stopped', text_Instr_3_key.tStopRefresh)
# the Routine "Instr_4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instr_5"-------
continueRoutine = True
# update component parameters for each repeat
button_resp_6.oldButtonState = button_resp_6.device.getAllButtons()[:]
button_resp_6.keys = []
button_resp_6.rt = []
# keep track of which components have finished
Instr_5Components = [text_Instr_4, text_Instr_4_key, button_resp_6]
for thisComponent in Instr_5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Instr_5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Instr_5"-------
while continueRoutine:
    # get current time
    t = Instr_5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Instr_5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_Instr_4* updates
    if text_Instr_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_4.frameNStart = frameN  # exact frame index
        text_Instr_4.tStart = t  # local t and not account for scr refresh
        text_Instr_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_4, 'tStartRefresh')  # time at next scr refresh
        text_Instr_4.setAutoDraw(True)
    
    # *text_Instr_4_key* updates
    if text_Instr_4_key.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_Instr_4_key.frameNStart = frameN  # exact frame index
        text_Instr_4_key.tStart = t  # local t and not account for scr refresh
        text_Instr_4_key.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_Instr_4_key, 'tStartRefresh')  # time at next scr refresh
        text_Instr_4_key.setAutoDraw(True)
    
    # *button_resp_6* updates
    if button_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button_resp_6.frameNStart = frameN  # exact frame index
        button_resp_6.tStart = t  # local t and not account for scr refresh
        button_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_resp_6, 'tStartRefresh')  # time at next scr refresh
        button_resp_6.status = STARTED
        # joyButtons checking is just starting
    if button_resp_6.status == STARTED:
        button_resp_6.newButtonState = button_resp_6.device.getAllButtons()[:]
        button_resp_6.pressedButtons = []
        button_resp_6.releasedButtons = []
        button_resp_6.newPressedButtons = []
        if button_resp_6.newButtonState != button_resp_6.oldButtonState:
            button_resp_6.pressedButtons = [i for i in range(button_resp_6.numButtons) if button_resp_6.newButtonState[i] and not button_resp_6.oldButtonState[i]]
            button_resp_6.releasedButtons = [i for i in range(button_resp_6.numButtons) if not button_resp_6.newButtonState[i] and button_resp_6.oldButtonState[i]]
            button_resp_6.oldButtonState = button_resp_6.newButtonState
            button_resp_6.newPressedButtons = [i for i in [0] if i in button_resp_6.pressedButtons]
            [logging.data("joystick_{}_button: {}".format(button_resp_6.device_number,i)) for i in button_resp_6.pressedButtons]
        theseKeys = button_resp_6.newPressedButtons
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instr_5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instr_5"-------
for thisComponent in Instr_5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_Instr_4.started', text_Instr_4.tStartRefresh)
thisExp.addData('text_Instr_4.stopped', text_Instr_4.tStopRefresh)
thisExp.addData('text_Instr_4_key.started', text_Instr_4_key.tStartRefresh)
thisExp.addData('text_Instr_4_key.stopped', text_Instr_4_key.tStopRefresh)
# the Routine "Instr_5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Practice_loop = data.TrialHandler(nReps=999.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(PracRun_order),
    seed=None, name='Practice_loop')
thisExp.addLoop(Practice_loop)  # add the loop to the experiment
thisPractice_loop = Practice_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
if thisPractice_loop != None:
    for paramName in thisPractice_loop:
        exec('{} = thisPractice_loop[paramName]'.format(paramName))

for thisPractice_loop in Practice_loop:
    currentLoop = Practice_loop
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_loop.rgb)
    if thisPractice_loop != None:
        for paramName in thisPractice_loop:
            exec('{} = thisPractice_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "GrayScreenPrac"-------
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GrayScreenPracComponents = [CrossPrac]
    for thisComponent in GrayScreenPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GrayScreenPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GrayScreenPrac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GrayScreenPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GrayScreenPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CrossPrac* updates
        if CrossPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CrossPrac.frameNStart = frameN  # exact frame index
            CrossPrac.tStart = t  # local t and not account for scr refresh
            CrossPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CrossPrac, 'tStartRefresh')  # time at next scr refresh
            CrossPrac.setAutoDraw(True)
        if CrossPrac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CrossPrac.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                CrossPrac.tStop = t  # not accounting for scr refresh
                CrossPrac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CrossPrac, 'tStopRefresh')  # time at next scr refresh
                CrossPrac.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GrayScreenPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GrayScreenPrac"-------
    for thisComponent in GrayScreenPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('CrossPrac.started', CrossPrac.tStartRefresh)
    Practice_loop.addData('CrossPrac.stopped', CrossPrac.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    Practice_Cong_loop = data.TrialHandler(nReps=nReps1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CondPractice_cong.csv'),
        seed=None, name='Practice_Cong_loop')
    thisExp.addLoop(Practice_Cong_loop)  # add the loop to the experiment
    thisPractice_Cong_loop = Practice_Cong_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Cong_loop.rgb)
    if thisPractice_Cong_loop != None:
        for paramName in thisPractice_Cong_loop:
            exec('{} = thisPractice_Cong_loop[paramName]'.format(paramName))
    
    for thisPractice_Cong_loop in Practice_Cong_loop:
        currentLoop = Practice_Cong_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Cong_loop.rgb)
        if thisPractice_Cong_loop != None:
            for paramName in thisPractice_Cong_loop:
                exec('{} = thisPractice_Cong_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Practice_Cong_instr"-------
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        win.flip
        InstrStart=timer.getTime()
        # keep track of which components have finished
        Practice_Cong_instrComponents = [text_Cong_PracInstr]
        for thisComponent in Practice_Cong_instrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice_Cong_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice_Cong_instr"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Practice_Cong_instrClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice_Cong_instrClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if Practice_Cong_loop.thisTrialN == 12 or Practice_Cong_loop.thisTrialN%6 !=0:
                continueRoutine = False
            
            
            # *text_Cong_PracInstr* updates
            if text_Cong_PracInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Cong_PracInstr.frameNStart = frameN  # exact frame index
                text_Cong_PracInstr.tStart = t  # local t and not account for scr refresh
                text_Cong_PracInstr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Cong_PracInstr, 'tStartRefresh')  # time at next scr refresh
                text_Cong_PracInstr.setAutoDraw(True)
            if text_Cong_PracInstr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Cong_PracInstr.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Cong_PracInstr.tStop = t  # not accounting for scr refresh
                    text_Cong_PracInstr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Cong_PracInstr, 'tStopRefresh')  # time at next scr refresh
                    text_Cong_PracInstr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice_Cong_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice_Cong_instr"-------
        for thisComponent in Practice_Cong_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Practice_Cong_loop.addData("InstrStartPracCong", InstrStart)
        Practice_Cong_loop.addData('text_Cong_PracInstr.started', text_Cong_PracInstr.tStartRefresh)
        Practice_Cong_loop.addData('text_Cong_PracInstr.stopped', text_Cong_PracInstr.tStopRefresh)
        
        # ------Prepare to start Routine "Practice_Cong_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_2.setImage(ImgStim_P)
        joystick_prac.oldButtonState = joystick_prac.device.getAllButtons()[:]
        joystick_prac.activeButtons=[i for i in range(joystick_prac.numButtons)]
        # setup some python lists for storing info about the joystick_prac
        gotValidClick = False  # until a click is received
        li=[]
        t_joyMoveonset=0
        trialtime=[]
        joystickX=[]
        joystickY=[]
        win.flip
        image_2start=timer.getTime()
        #win.flip()
        #port.setData(int(EventCode_p))
        #core.wait(.01)
        #port.setData(0)
        # keep track of which components have finished
        Practice_Cong_trialComponents = [fix_1, image_2, ITI_prac, joystick_prac]
        for thisComponent in Practice_Cong_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice_Cong_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice_Cong_trial"-------
        while continueRoutine:
            # get current time
            t = Practice_Cong_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice_Cong_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_1* updates
            if fix_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_1.frameNStart = frameN  # exact frame index
                fix_1.tStart = t  # local t and not account for scr refresh
                fix_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_1, 'tStartRefresh')  # time at next scr refresh
                fix_1.setAutoDraw(True)
            if fix_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_1.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_1.tStop = t  # not accounting for scr refresh
                    fix_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_1, 'tStopRefresh')  # time at next scr refresh
                    fix_1.setAutoDraw(False)
            
            # *image_2* updates
            if image_2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_2.frameNStart = frameN  # exact frame index
                image_2.tStart = t  # local t and not account for scr refresh
                image_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                image_2.setAutoDraw(True)
            if image_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_2.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_2.tStop = t  # not accounting for scr refresh
                    image_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                    image_2.setAutoDraw(False)
            if image_2.status == STARTED:  # only update if drawing
                image_2.setSize(image_size, log=False)
            
            # *ITI_prac* updates
            if ITI_prac.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                ITI_prac.frameNStart = frameN  # exact frame index
                ITI_prac.tStart = t  # local t and not account for scr refresh
                ITI_prac.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_prac, 'tStartRefresh')  # time at next scr refresh
                ITI_prac.setAutoDraw(True)
            if ITI_prac.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_prac.tStartRefresh + ITI_P-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_prac.tStop = t  # not accounting for scr refresh
                    ITI_prac.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ITI_prac, 'tStopRefresh')  # time at next scr refresh
                    ITI_prac.setAutoDraw(False)
            li.append(joystick_prac.getY())
            joy_max=max(li)
            joy_min=min(li)
            trialtime.append(tThisFlipGlobal)
            joystickX.append(joystick_prac.getX())
            joystickY.append(joystick_prac.getY())
            
            #Get the joystick movement onset global time.
            if t_joyMoveonset== 0 and joy_min < -0.2:
                t_joyMoveonset = tThisFlipGlobal
            elif t_joyMoveonset == 0 and joy_max > 0.2:
                t_joyMoveonset = tThisFlipGlobal
            
            if joy_min >= -0.2 and joy_max <= 0.2:
                image_size = [w, h]
            elif joy_min < -0.2:
                w1=w*0.3
                h1=h*0.3
                image_size = [w1, h1]
            #    image.setSize([w,h])
            elif joy_max > 0.2:
            #    image_size = (0.64, 0.48)
                w1=w*2
                h1=h*2
                image_size = [w1, h1]
            
            
            #if joy_min >= -0.02 and joy_max <= 0.03:
            #    idx_joymax = 0 
            #    idx_joymin = 0
            #else: 
            #    # using map() + lambda to find index of 
            #    #first element just greater than 0.03
            #    print("li")
            #    print(li)
            #    print("the first number")
            #    print(list(filter(lambda i: i > 0.03, li))[0])
            #    print("the first number index")
            #    print(li.index(list(filter(lambda i: i > 0.03, li))[0])) 
            #    idx_joymax = li.index(list(filter(lambda i: i > 0.03, li))[0])
            #    #find index of first element just less than -0.02
            #    idx_joymin = li.index(list(filter(lambda i: i < -0.02, li))[0])
            #
            #
            #
            #if idx_joymax==idx_joymin:
            #    image_size = [w, h]
            #else:
            #    if joy_min >= -0.02 and joy_max <= 0.03:
            #        image_size = [w, h]
            #    elif joy_min < -0.02 and idx_joymin > idx_joymax:
            #        w1=w*0.3
            #        h1=h*0.3
            #        image_size = [w1, h1]
            #    #    image.setSize([w,h])
            #    elif joy_max > 0.03 and idx_joymin < idx_joymax:
            #    #    image_size = (0.64, 0.48)
            #        w1=w*1.7
            #        h1=h*1.7
            #        image_size = [w1, h1]
            if ITI_prac.status==FINISHED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice_Cong_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice_Cong_trial"-------
        for thisComponent in Practice_Cong_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Practice_Cong_loop.addData('fix_1.started', fix_1.tStartRefresh)
        Practice_Cong_loop.addData('fix_1.stopped', fix_1.tStopRefresh)
        Practice_Cong_loop.addData('image_2.started', image_2.tStartRefresh)
        Practice_Cong_loop.addData('image_2.stopped', image_2.tStopRefresh)
        Practice_Cong_loop.addData('ITI_prac.started', ITI_prac.tStartRefresh)
        Practice_Cong_loop.addData('ITI_prac.stopped', ITI_prac.tStopRefresh)
        # store data for Practice_Cong_loop (TrialHandler)
        # store data for Practice_Cong_loop (TrialHandler)
        x, y = joystick_prac.getX(), joystick_prac.getY()
        joystick_prac.newButtonState = joystick_prac.getAllButtons()[:]
        joystick_prac.pressedState = [joystick_prac.newButtonState[i] for i in range(joystick_prac.numButtons)]
        joystick_prac.time = joystick_prac.joystickClock.getTime()
        Practice_Cong_loop.addData('joystick_prac.x', x)
        Practice_Cong_loop.addData('joystick_prac.y', y)
        [Practice_Cong_loop.addData('joystick_prac.button_{0}'.format(i), int(joystick_prac.pressedState[i])) for i in joystick_prac.activeButtons]
        Practice_Cong_loop.addData('joystick_prac.time', joystick_prac.time)
        Practice_Cong_loop.addData('joystick_prac.started', joystick_prac.tStart)
        Practice_Cong_loop.addData('joystick_prac.stopped', joystick_prac.tStop)
        #print(ImgStim_P)
        joystick_RT = t_joyMoveonset - image_2.tStartRefresh
        Practice_Cong_loop.addData("joystickMovePrac.started", t_joyMoveonset)
        Practice_Cong_loop.addData("joystickPrac_reaction", joystick_RT)
        Practice_Cong_loop.addData("joystickPrac_timepoint", trialtime)
        Practice_Cong_loop.addData("joystickPrac_X", joystickX)
        Practice_Cong_loop.addData("joystickPrac_Y", joystickY)
        Practice_Cong_loop.addData("ImageStartPracCong", image_2start)
        
        # correct = 1 , incorrect = 0. 
        if StimVal == "neg" and joy_min <= Target_joy:
            tmp_correct = 1
        elif StimVal == "pos" and joy_max >= Target_joy:
            tmp_correct = 1
        #elif StimVal == "neg" and joy_min > Target_joy:
        #    tmp_correct = 0 
        #elif StimVal == "pos" and joy_max < Target_joy:
        #    tmp_correct = 0
        else:
            tmp_correct = 0
        li_correct_prac.append(tmp_correct)
        print("This is li_correct_prac")
        print(li_correct_prac)
        print("this is joy_max and joy_min targe_joy")
        print(joy_max)
        print(joy_min)
        print(Target_joy)
        
        
        if len(li_correct_prac)==12:
            percent_correct = sum(li_correct_prac)/12
            li_correct_prac=[]
            print("This is percent_correct cong")
            print(percent_correct)
        else: 
            percent_correct = 0
        
        if percent_correct >= 0.8:
            Practice_loop.finished=True
            
        
        # the Routine "Practice_Cong_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nReps1 repeats of 'Practice_Cong_loop'
    
    
    # ------Prepare to start Routine "GrayScreenPrac"-------
    continueRoutine = True
    routineTimer.add(8.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GrayScreenPracComponents = [CrossPrac]
    for thisComponent in GrayScreenPracComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GrayScreenPracClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GrayScreenPrac"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GrayScreenPracClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GrayScreenPracClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *CrossPrac* updates
        if CrossPrac.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            CrossPrac.frameNStart = frameN  # exact frame index
            CrossPrac.tStart = t  # local t and not account for scr refresh
            CrossPrac.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(CrossPrac, 'tStartRefresh')  # time at next scr refresh
            CrossPrac.setAutoDraw(True)
        if CrossPrac.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > CrossPrac.tStartRefresh + 8.0-frameTolerance:
                # keep track of stop time/frame for later
                CrossPrac.tStop = t  # not accounting for scr refresh
                CrossPrac.frameNStop = frameN  # exact frame index
                win.timeOnFlip(CrossPrac, 'tStopRefresh')  # time at next scr refresh
                CrossPrac.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GrayScreenPracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GrayScreenPrac"-------
    for thisComponent in GrayScreenPracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('CrossPrac.started', CrossPrac.tStartRefresh)
    Practice_loop.addData('CrossPrac.stopped', CrossPrac.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    Practice_Incong_loop = data.TrialHandler(nReps=nReps2, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('CondPractice_Incong.csv'),
        seed=None, name='Practice_Incong_loop')
    thisExp.addLoop(Practice_Incong_loop)  # add the loop to the experiment
    thisPractice_Incong_loop = Practice_Incong_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice_Incong_loop.rgb)
    if thisPractice_Incong_loop != None:
        for paramName in thisPractice_Incong_loop:
            exec('{} = thisPractice_Incong_loop[paramName]'.format(paramName))
    
    for thisPractice_Incong_loop in Practice_Incong_loop:
        currentLoop = Practice_Incong_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPractice_Incong_loop.rgb)
        if thisPractice_Incong_loop != None:
            for paramName in thisPractice_Incong_loop:
                exec('{} = thisPractice_Incong_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "Practice_Incong_instr"-------
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        win.flip
        InstrStart=timer.getTime()
        # keep track of which components have finished
        Practice_Incong_instrComponents = [text_Incong_PracInstr]
        for thisComponent in Practice_Incong_instrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice_Incong_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice_Incong_instr"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = Practice_Incong_instrClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice_Incong_instrClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if Practice_Incong_loop.thisTrialN == 12 or Practice_Incong_loop.thisTrialN%6 !=0:
                continueRoutine = False
            
            # *text_Incong_PracInstr* updates
            if text_Incong_PracInstr.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_Incong_PracInstr.frameNStart = frameN  # exact frame index
                text_Incong_PracInstr.tStart = t  # local t and not account for scr refresh
                text_Incong_PracInstr.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_Incong_PracInstr, 'tStartRefresh')  # time at next scr refresh
                text_Incong_PracInstr.setAutoDraw(True)
            if text_Incong_PracInstr.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_Incong_PracInstr.tStartRefresh + 7-frameTolerance:
                    # keep track of stop time/frame for later
                    text_Incong_PracInstr.tStop = t  # not accounting for scr refresh
                    text_Incong_PracInstr.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_Incong_PracInstr, 'tStopRefresh')  # time at next scr refresh
                    text_Incong_PracInstr.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice_Incong_instrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice_Incong_instr"-------
        for thisComponent in Practice_Incong_instrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Practice_Incong_loop.addData("InstrStartPracIncong", InstrStart)
        Practice_Incong_loop.addData('text_Incong_PracInstr.started', text_Incong_PracInstr.tStartRefresh)
        Practice_Incong_loop.addData('text_Incong_PracInstr.stopped', text_Incong_PracInstr.tStopRefresh)
        
        # ------Prepare to start Routine "Practice_Incong_trial_2"-------
        continueRoutine = True
        # update component parameters for each repeat
        image_3.setImage(ImgStim_P)
        joystick_prac_2.oldButtonState = joystick_prac_2.device.getAllButtons()[:]
        joystick_prac_2.activeButtons=[i for i in range(joystick_prac_2.numButtons)]
        # setup some python lists for storing info about the joystick_prac_2
        gotValidClick = False  # until a click is received
        li=[]
        #trialtime=[]
        #joystickX=[]
        #joystickY=[]
        win.flip
        image_3start=timer.getTime()
        # keep track of which components have finished
        Practice_Incong_trial_2Components = [fix_2, image_3, ITI_prac_2, joystick_prac_2]
        for thisComponent in Practice_Incong_trial_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        Practice_Incong_trial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "Practice_Incong_trial_2"-------
        while continueRoutine:
            # get current time
            t = Practice_Incong_trial_2Clock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=Practice_Incong_trial_2Clock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix_2* updates
            if fix_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix_2.frameNStart = frameN  # exact frame index
                fix_2.tStart = t  # local t and not account for scr refresh
                fix_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix_2, 'tStartRefresh')  # time at next scr refresh
                fix_2.setAutoDraw(True)
            if fix_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix_2.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix_2.tStop = t  # not accounting for scr refresh
                    fix_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix_2, 'tStopRefresh')  # time at next scr refresh
                    fix_2.setAutoDraw(False)
            
            # *image_3* updates
            if image_3.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image_3.frameNStart = frameN  # exact frame index
                image_3.tStart = t  # local t and not account for scr refresh
                image_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                image_3.setAutoDraw(True)
            if image_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image_3.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    image_3.tStop = t  # not accounting for scr refresh
                    image_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                    image_3.setAutoDraw(False)
            if image_3.status == STARTED:  # only update if drawing
                image_3.setSize(image_size, log=False)
            
            # *ITI_prac_2* updates
            if ITI_prac_2.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                ITI_prac_2.frameNStart = frameN  # exact frame index
                ITI_prac_2.tStart = t  # local t and not account for scr refresh
                ITI_prac_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_prac_2, 'tStartRefresh')  # time at next scr refresh
                ITI_prac_2.setAutoDraw(True)
            if ITI_prac_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_prac_2.tStartRefresh + ITI_P-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_prac_2.tStop = t  # not accounting for scr refresh
                    ITI_prac_2.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ITI_prac_2, 'tStopRefresh')  # time at next scr refresh
                    ITI_prac_2.setAutoDraw(False)
            li.append(joystick_prac_2.getY())
            joy_max=max(li)
            joy_min=min(li)
            
            #trialtime.append(tThisFlipGlobal)
            #joystickX.append(joystick_prac.getX())
            #joystickY.append(joystick_prac.getY())
            
            if joy_min >= -0.2 and joy_max <= 0.2:
                image_size = [w, h]
            elif joy_min < -0.2:
                w1=w*0.3
                h1=h*0.3
                image_size = [w1, h1]
            #    image.setSize([w,h])
            elif joy_max > 0.2:
            #    image_size = (0.64, 0.48)
                w1=w*1.7
                h1=h*1.7
                image_size = [w1, h1]
            
            
            #if joy_min >= -0.02 and joy_max <= 0.03:
            #    idx_joymax = 0 
            #    idx_joymin = 0
            #else: 
            #    # using map() + lambda to find index of 
            #    #first element just greater than 0.03
            #    print("li")
            #    print(li)
            #    print("the first number")
            #    print(list(filter(lambda i: i > 0.03, li))[0])
            #    print("the first number index")
            #    print(li.index(list(filter(lambda i: i > 0.03, li))[0])) 
            #    idx_joymax = li.index(list(filter(lambda i: i > 0.03, li))[0])
            #    #find index of first element just less than -0.02
            #    idx_joymin = li.index(list(filter(lambda i: i < -0.02, li))[0])
            #
            #
            #
            #if idx_joymax==idx_joymin:
            #    image_size = [w, h]
            #else:
            #    if joy_min >= -0.02 and joy_max <= 0.03:
            #        image_size = [w, h]
            #    elif joy_min < -0.02 and idx_joymin > idx_joymax:
            #        w1=w*0.3
            #        h1=h*0.3
            #        image_size = [w1, h1]
            #    #    image.setSize([w,h])
            #    elif joy_max > 0.03 and idx_joymin < idx_joymax:
            #    #    image_size = (0.64, 0.48)
            #        w1=w*1.7
            #        h1=h*1.7
            #        image_size = [w1, h1]
            if ITI_prac_2.status==FINISHED:
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in Practice_Incong_trial_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "Practice_Incong_trial_2"-------
        for thisComponent in Practice_Incong_trial_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        Practice_Incong_loop.addData('fix_2.started', fix_2.tStartRefresh)
        Practice_Incong_loop.addData('fix_2.stopped', fix_2.tStopRefresh)
        Practice_Incong_loop.addData('image_3.started', image_3.tStartRefresh)
        Practice_Incong_loop.addData('image_3.stopped', image_3.tStopRefresh)
        Practice_Incong_loop.addData('ITI_prac_2.started', ITI_prac_2.tStartRefresh)
        Practice_Incong_loop.addData('ITI_prac_2.stopped', ITI_prac_2.tStopRefresh)
        # store data for Practice_Incong_loop (TrialHandler)
        # store data for Practice_Incong_loop (TrialHandler)
        x, y = joystick_prac_2.getX(), joystick_prac_2.getY()
        joystick_prac_2.newButtonState = joystick_prac_2.getAllButtons()[:]
        joystick_prac_2.pressedState = [joystick_prac_2.newButtonState[i] for i in range(joystick_prac_2.numButtons)]
        joystick_prac_2.time = joystick_prac_2.joystickClock.getTime()
        Practice_Incong_loop.addData('joystick_prac_2.x', x)
        Practice_Incong_loop.addData('joystick_prac_2.y', y)
        [Practice_Incong_loop.addData('joystick_prac_2.button_{0}'.format(i), int(joystick_prac_2.pressedState[i])) for i in joystick_prac_2.activeButtons]
        Practice_Incong_loop.addData('joystick_prac_2.time', joystick_prac_2.time)
        #Practice_Incong_loop.addData("joystickPrac_timepoint", trialtime)
        #Practice_Incong_loop.addData("joystickPrac_X", joystickX)
        #Practice_Incong_loop.addData("joystickPrac_Y", joystickY)
        Practice_Incong_loop.addData("ImageStartPracIncong", image_3start)
        # correct = 1 , incorrect = 0. 
        if StimVal == "neg" and joy_max >= Target_joy:
            tmp_correct = 1
        elif StimVal == "pos" and joy_min <= Target_joy:
            tmp_correct = 1
        #elif StimVal == "neg" and joy_min < Target_joy:
        #    tmp_correct = 0 
        #elif StimVal == "pos" and joy_max > Target_joy:
        #    tmp_correct = 0
        else:
            tmp_correct = 0
        li_correct_prac.append(tmp_correct)
        print("This is li_correct_prac")
        print(li_correct_prac)
        
        if len(li_correct_prac)==12:
            percent_correct = sum(li_correct_prac)/12
            li_correct_prac=[]
            print("This is percent_correct Incong")
            print(percent_correct)    
        else: 
            percent_correct = 0
        
        if percent_correct >= 0.8:
            Practice_loop.finished=True
        # the Routine "Practice_Incong_trial_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed nReps2 repeats of 'Practice_Incong_loop'
    
    
    # ------Prepare to start Routine "Prac_instr"-------
    continueRoutine = True
    # update component parameters for each repeat
    button_resp.oldButtonState = button_resp.device.getAllButtons()[:]
    button_resp.keys = []
    button_resp.rt = []
    # keep track of which components have finished
    Prac_instrComponents = [text, button_resp]
    for thisComponent in Prac_instrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Prac_instrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Prac_instr"-------
    while continueRoutine:
        # get current time
        t = Prac_instrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Prac_instrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        #if int(expInfo['participant'][-1]) % 2 == 0:
        #    if percent_correct >= 0.9 or Practice_loop.thisTrialN%2 !=0:
        #        continueRoutine = False
        #else:
        #    if percent_correct >= 0.9 or Practice_loop.thisTrialN%2 !=0:
        #        continueRoutine = False
        if percent_correct >= 0.8 or (Practice_loop.thisTrialN+1)%2 !=0:
            continueRoutine = False
        #    Practice_loop.finished=True
        
        # *button_resp* updates
        if button_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            button_resp.frameNStart = frameN  # exact frame index
            button_resp.tStart = t  # local t and not account for scr refresh
            button_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(button_resp, 'tStartRefresh')  # time at next scr refresh
            button_resp.status = STARTED
            # joyButtons checking is just starting
        if button_resp.status == STARTED:
            button_resp.newButtonState = button_resp.device.getAllButtons()[:]
            button_resp.pressedButtons = []
            button_resp.releasedButtons = []
            button_resp.newPressedButtons = []
            if button_resp.newButtonState != button_resp.oldButtonState:
                button_resp.pressedButtons = [i for i in range(button_resp.numButtons) if button_resp.newButtonState[i] and not button_resp.oldButtonState[i]]
                button_resp.releasedButtons = [i for i in range(button_resp.numButtons) if not button_resp.newButtonState[i] and button_resp.oldButtonState[i]]
                button_resp.oldButtonState = button_resp.newButtonState
                button_resp.newPressedButtons = [i for i in [0] if i in button_resp.pressedButtons]
                [logging.data("joystick_{}_button: {}".format(button_resp.device_number,i)) for i in button_resp.pressedButtons]
            theseKeys = button_resp.newPressedButtons
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Prac_instrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Prac_instr"-------
    for thisComponent in Prac_instrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Practice_loop.addData('text.started', text.tStartRefresh)
    Practice_loop.addData('text.stopped', text.tStopRefresh)
    print("This practice loop count")
    print(Practice_loop.thisTrialN+1)
    # the Routine "Prac_instr" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 999.0 repeats of 'Practice_loop'


# ------Prepare to start Routine "LastCheckBeforeStart"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
LastCheckBeforeStartComponents = [text_10, key_resp_13]
for thisComponent in LastCheckBeforeStartComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LastCheckBeforeStartClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LastCheckBeforeStart"-------
while continueRoutine:
    # get current time
    t = LastCheckBeforeStartClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LastCheckBeforeStartClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LastCheckBeforeStartComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LastCheckBeforeStart"-------
for thisComponent in LastCheckBeforeStartComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
# the Routine "LastCheckBeforeStart" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
run_loop = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('runcond.csv'),
    seed=None, name='run_loop')
thisExp.addLoop(run_loop)  # add the loop to the experiment
thisRun_loop = run_loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun_loop.rgb)
if thisRun_loop != None:
    for paramName in thisRun_loop:
        exec('{} = thisRun_loop[paramName]'.format(paramName))

for thisRun_loop in run_loop:
    currentLoop = run_loop
    # abbreviate parameter names if possible (e.g. rgb = thisRun_loop.rgb)
    if thisRun_loop != None:
        for paramName in thisRun_loop:
            exec('{} = thisRun_loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fixation_1"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixation_1Components = [fixation]
    for thisComponent in fixation_1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixation_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fixation_1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixation_1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixation_1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixation_1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixation_1"-------
    for thisComponent in fixation_1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run_loop.addData('fixation.started', fixation.tStartRefresh)
    run_loop.addData('fixation.stopped', fixation.tStopRefresh)
    
    # ------Prepare to start Routine "eyelink"-------
    continueRoutine = True
    # update component parameters for each repeat
    ## We download EDF data file from the EyeLink Host PC to the local hard
    ## drive at the end of each testing session, here we rename the EDF to
    ## include session start date/time
    #time_str = time.strftime("_%Y_%m_%d_%H_%M", time.localtime())
    #session_identifier = edf_fname + "_prac" + time_str
    #
    ## create a folder for the current testing session in the "results" folder
    #session_folder = os.path.join(results_folder, session_identifier)
    
    # Step 2: Open an EDF data file on the Host PC
    RunNum='_'+str(run_loop.thisN+1)
    edf_file = edf_fname + RunNum + ".EDF"
    try:
        el_tracker.openDataFile(edf_file)
    except RuntimeError as err:
        print('ERROR:', err)
        # close the link if we have one open
        if el_tracker.isConnected():
            el_tracker.close()
        core.quit()
        sys.exit()
        
    # get a reference to the currently active EyeLink connection
    el_tracker = pylink.getEYELINK()
    
    # put the tracker in the offline mode first
    el_tracker.setOfflineMode()
        
        # send a "TRIALID" message to mark the start of a trial, see Data
        # Viewer User Manual, "Protocol for EyeLink Data to Viewer Integration"
    RunNum=run_loop.thisN+1
    el_tracker.sendMessage('RunNum %d' % RunNum)
    
        # record_status_message : show some info on the Host PC
        # here we show how many trial has been tested
    status_msg = 'Run Num %d' % RunNum
    el_tracker.sendCommand("record_status_message '%s'" % status_msg)
        
         # put tracker in idle/offline mode before recording
    el_tracker.setOfflineMode()
    
        # Start recording
        # arguments: sample_to_file, events_to_file, sample_over_link,
        # event_over_link (1-yes, 0-no)
    
    el_tracker.startRecording(1, 1, 1, 1)
    
    # keep track of which components have finished
    eyelinkComponents = []
    for thisComponent in eyelinkComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    eyelinkClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "eyelink"-------
    while continueRoutine:
        # get current time
        t = eyelinkClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=eyelinkClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in eyelinkComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "eyelink"-------
    for thisComponent in eyelinkComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "eyelink" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "fMRItriger"-------
    continueRoutine = True
    # update component parameters for each repeat
    wait_to_stop=True
    triggers=0
    start = tThisFlipGlobal
    #start = timer.getTime()
    ser = serial.Serial('COM4',19200,stopbits=1)
    # keep track of which components have finished
    fMRItrigerComponents = []
    for thisComponent in fMRItrigerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fMRItrigerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fMRItriger"-------
    while continueRoutine:
        # get current time
        t = fMRItrigerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fMRItrigerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        while wait_to_stop:
        #    ser.close()
            s = ser.read()
            if '5' in s.decode("utf-8"):
        #        stop = timer.getTime()
                stop = tThisFlipGlobal
                ser.close()
                triggers=triggers+1
        #        print('trigger '+str(triggers)+' located '+str(stop-start)+' seconds later')
                wait_to_stop=False
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fMRItrigerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fMRItriger"-------
    for thisComponent in fMRItrigerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run_loop.addData("fMRITriggerStart", start)
    run_loop.addData("fMRITriggerEnd", stop)
    # the Routine "fMRItriger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "GrayScreen20s"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GrayScreen20sComponents = [GrayScreent]
    for thisComponent in GrayScreen20sComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GrayScreen20sClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GrayScreen20s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GrayScreen20sClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GrayScreen20sClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GrayScreent* updates
        if GrayScreent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GrayScreent.frameNStart = frameN  # exact frame index
            GrayScreent.tStart = t  # local t and not account for scr refresh
            GrayScreent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GrayScreent, 'tStartRefresh')  # time at next scr refresh
            GrayScreent.setAutoDraw(True)
        if GrayScreent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GrayScreent.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                GrayScreent.tStop = t  # not accounting for scr refresh
                GrayScreent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(GrayScreent, 'tStopRefresh')  # time at next scr refresh
                GrayScreent.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GrayScreen20sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GrayScreen20s"-------
    for thisComponent in GrayScreen20sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run_loop.addData('GrayScreent.started', GrayScreent.tStartRefresh)
    run_loop.addData('GrayScreent.stopped', GrayScreent.tStopRefresh)
    
    # set up handler to look after randomisation of conditions etc
    trial_loop = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(run_file),
        seed=None, name='trial_loop')
    thisExp.addLoop(trial_loop)  # add the loop to the experiment
    thisTrial_loop = trial_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
    if thisTrial_loop != None:
        for paramName in thisTrial_loop:
            exec('{} = thisTrial_loop[paramName]'.format(paramName))
    
    for thisTrial_loop in trial_loop:
        currentLoop = trial_loop
        # abbreviate parameter names if possible (e.g. rgb = thisTrial_loop.rgb)
        if thisTrial_loop != None:
            for paramName in thisTrial_loop:
                exec('{} = thisTrial_loop[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "BlockInstr"-------
        continueRoutine = True
        routineTimer.add(7.000000)
        # update component parameters for each repeat
        if Congruency==0:
            Instr = "Please pull the joystick AWAY from yourself if you see a NEGATIVE image, or pull the joystick TOWARDS you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes."
        else:
            Instr = "Please pull the joystick TOWARDS yourself if you see a NEGATIVE image, or pull the joystick AWAY from you if you see a POSITIVE image AS FAST AS POSSIBLE without making mistakes."
        win.flip
        #InstrStart=timer.getTime()
        InstrStart = tThisFlipGlobal
        Instruction_1.setText(Instr)
        # keep track of which components have finished
        BlockInstrComponents = [Instruction_1]
        for thisComponent in BlockInstrComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        BlockInstrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "BlockInstr"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = BlockInstrClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=BlockInstrClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if trial_loop.thisTrialN == 48 or trial_loop.thisTrialN%12 !=0:
                continueRoutine = False
            
            # *Instruction_1* updates
            if Instruction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Instruction_1.frameNStart = frameN  # exact frame index
                Instruction_1.tStart = t  # local t and not account for scr refresh
                Instruction_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Instruction_1, 'tStartRefresh')  # time at next scr refresh
                Instruction_1.setAutoDraw(True)
            if Instruction_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Instruction_1.tStartRefresh + 7.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Instruction_1.tStop = t  # not accounting for scr refresh
                    Instruction_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(Instruction_1, 'tStopRefresh')  # time at next scr refresh
                    Instruction_1.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in BlockInstrComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "BlockInstr"-------
        for thisComponent in BlockInstrComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_loop.addData("InstrStart", InstrStart)
        trial_loop.addData('Instruction_1.started', Instruction_1.tStartRefresh)
        trial_loop.addData('Instruction_1.stopped', Instruction_1.tStopRefresh)
        
        # ------Prepare to start Routine "main_trial"-------
        continueRoutine = True
        # update component parameters for each repeat
        image.setImage(ImgStim)
        #w=0.7
        #h=0.525
        ##image.setSize([w,h])
        #image_size=[w, h]
        
        li=[]
        t_joyMoveonset=0
        trialtime=[]
        joystickX=[]
        joystickY=[]
        #win.flip
        #imagestart=timer.getTime()+0.5
        #imagestart_2=0
        tmp_correct=0
        joystick.oldButtonState = joystick.device.getAllButtons()[:]
        joystick.activeButtons=[i for i in range(joystick.numButtons)]
        # setup some python lists for storing info about the joystick
        gotValidClick = False  # until a click is received
        img_onset_time=0
        win.flip()
        #port.setData(int(event_code))
        #core.wait(.01)
        #port.setData(0)
        
        el_tracker.sendMessage('image_onset')
        trial_onset_time = tThisFlipGlobal  # record the image onset time
        EC=int(event_code)
        el_tracker.sendMessage('EventCode %d' % EC)
        status_msg = 'Event Code %d' % EC
        el_tracker.sendCommand("record_status_message '%s'" % status_msg)
        
        ##Below code does not raise error, but not functioning yet. 
        ## Use the code commented below to convert the image and send the backdrop
        #im = Image.open(ImgStim)  # read image with PIL
        #im = im.resize((scn_width, scn_height))
        #img_pixels = im.load()  # access the pixel data of the image
        #pixels = [[img_pixels[i, j] for i in range(scn_width)]
        #for j in range(scn_height)]
        #el_tracker.bitmapBackdrop(scn_width, scn_height, pixels,
        #                              0, 0, scn_width, scn_height,
        #                              0, 0, pylink.BX_MAXCONTRAST)
        # keep track of which components have finished
        main_trialComponents = [fix, image, ITI_1, joystick]
        for thisComponent in main_trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        main_trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "main_trial"-------
        while continueRoutine:
            # get current time
            t = main_trialClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=main_trialClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fix* updates
            if fix.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                fix.frameNStart = frameN  # exact frame index
                fix.tStart = t  # local t and not account for scr refresh
                fix.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(fix, 'tStartRefresh')  # time at next scr refresh
                fix.setAutoDraw(True)
            if fix.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > fix.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    fix.tStop = t  # not accounting for scr refresh
                    fix.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(fix, 'tStopRefresh')  # time at next scr refresh
                    fix.setAutoDraw(False)
            
            # *image* updates
            if image.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
                # keep track of start time/frame for later
                image.frameNStart = frameN  # exact frame index
                image.tStart = t  # local t and not account for scr refresh
                image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                image.setAutoDraw(True)
            if image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > image.tStartRefresh + 2.2-frameTolerance:
                    # keep track of stop time/frame for later
                    image.tStop = t  # not accounting for scr refresh
                    image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                    image.setAutoDraw(False)
            if image.status == STARTED:  # only update if drawing
                image.setSize(image_size, log=False)
            
            # *ITI_1* updates
            if ITI_1.status == NOT_STARTED and tThisFlip >= 2.7-frameTolerance:
                # keep track of start time/frame for later
                ITI_1.frameNStart = frameN  # exact frame index
                ITI_1.tStart = t  # local t and not account for scr refresh
                ITI_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(ITI_1, 'tStartRefresh')  # time at next scr refresh
                ITI_1.setAutoDraw(True)
            if ITI_1.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > ITI_1.tStartRefresh + ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    ITI_1.tStop = t  # not accounting for scr refresh
                    ITI_1.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(ITI_1, 'tStopRefresh')  # time at next scr refresh
                    ITI_1.setAutoDraw(False)
            #if image.status == STARTED and imagestart_2==0:
            #    imagestart_2=timer.getTime()
            
            ##This is for joystick control:
            li.append(joystick.getY())
            joy_max=max(li)
            joy_min=min(li)
            
            if image.status == STARTED:
                trialtime.append(tThisFlipGlobal)
                joystickX.append(joystick.getX())
                joystickY.append(joystick.getY())
            
            if t_joyMoveonset== 0 and joy_min < -0.2:
                t_joyMoveonset = tThisFlipGlobal
            elif t_joyMoveonset == 0 and joy_max > 0.2:
                t_joyMoveonset = tThisFlipGlobal
                
            
            if joy_min >= -0.2 and joy_max <= 0.2:
                image_size = [w, h]
            elif joy_min < -0.2:
                w1=w*0.3
                h1=h*0.3
                image_size = [w1, h1]
            #    image.setSize([w,h])
            elif joy_max > 0.2:
            #    image_size = (0.64, 0.48)
                w1=w*2
                h1=h*2
                image_size = [w1, h1]
            
            if ITI_1.status==FINISHED:
                continueRoutine = False
            if image.status == STARTED and img_onset_time==0:
                img_onset_time= tThisFlipGlobal
                el_tracker.sendCommand("record_status_message '%s'" % img_onset_time)
                el_tracker.sendMessage("record_status_message '%s'" % img_onset_time)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in main_trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "main_trial"-------
        for thisComponent in main_trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trial_loop.addData('fix.started', fix.tStartRefresh)
        trial_loop.addData('fix.stopped', fix.tStopRefresh)
        trial_loop.addData('image.started', image.tStartRefresh)
        trial_loop.addData('image.stopped', image.tStopRefresh)
        trial_loop.addData('ITI_1.started', ITI_1.tStartRefresh)
        trial_loop.addData('ITI_1.stopped', ITI_1.tStopRefresh)
        joystick_RT = t_joyMoveonset - image.tStartRefresh
        trial_loop.addData("joystickMove_started", t_joyMoveonset)
        trial_loop.addData("joystick_reaction", joystick_RT)
        trial_loop.addData("joystick_timepoint", trialtime)
        trial_loop.addData("joystick_X", joystickX)
        trial_loop.addData("joystick_Y", joystickY)
        
        
        # correct = 1 , incorrect = 0.
        #print("this is joy_min")
        #print(joy_min)
        #print("this is joy_max")
        #print(joy_max)
        if Congruency == 1:
            if StimVal == "neg" and joy_max >= Target_JoyParameter:
                tmp_correct = 1
            elif StimVal == "pos" and joy_min <= Target_JoyParameter:
                tmp_correct = 1
            #elif StimVal == "neg" and joy_min < Target_joy:
            #    tmp_correct = 0 
            #elif StimVal == "pos" and joy_max > Target_joy:
            #    tmp_correct = 0
            else:
                tmp_correct = 0
        elif Congruency == 0:
            if StimVal == "neg" and joy_min <= Target_JoyParameter:
                tmp_correct = 1
            elif StimVal == "pos" and joy_max >= Target_JoyParameter:
                tmp_correct = 1
            #elif StimVal == "neg" and joy_min > Target_joy:
            #    tmp_correct = 0 
            #elif StimVal == "pos" and joy_max < Target_joy:
            #    tmp_correct = 0
            else:
                tmp_correct = 0
            
        trial_loop.addData("trial_correct", tmp_correct)
        trial_loop.addData("joystick_max", joy_max)
        trial_loop.addData("joystick_min", joy_min)
        
        # store data for trial_loop (TrialHandler)
        trial_loop.addData('joystick.started', joystick.tStart)
        trial_loop.addData('joystick.stopped', joystick.tStop)
        
        #trial_loop.addData("trial_onset", trial_onset_time)
        #trial_loop.addData("image_onset", img_onset_time)
        # the Routine "main_trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1.0 repeats of 'trial_loop'
    
    
    # ------Prepare to start Routine "GrayScreen20s"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    GrayScreen20sComponents = [GrayScreent]
    for thisComponent in GrayScreen20sComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    GrayScreen20sClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "GrayScreen20s"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = GrayScreen20sClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=GrayScreen20sClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *GrayScreent* updates
        if GrayScreent.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            GrayScreent.frameNStart = frameN  # exact frame index
            GrayScreent.tStart = t  # local t and not account for scr refresh
            GrayScreent.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(GrayScreent, 'tStartRefresh')  # time at next scr refresh
            GrayScreent.setAutoDraw(True)
        if GrayScreent.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > GrayScreent.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                GrayScreent.tStop = t  # not accounting for scr refresh
                GrayScreent.frameNStop = frameN  # exact frame index
                win.timeOnFlip(GrayScreent, 'tStopRefresh')  # time at next scr refresh
                GrayScreent.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in GrayScreen20sComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "GrayScreen20s"-------
    for thisComponent in GrayScreen20sComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run_loop.addData('GrayScreent.started', GrayScreent.tStartRefresh)
    run_loop.addData('GrayScreent.stopped', GrayScreent.tStopRefresh)
    
    # ------Prepare to start Routine "RCheck"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # Close the edf data file on the Host
    el_tracker.closeDataFile()
    # put the tracker in the offline mode first
    el_tracker.setOfflineMode()
    
    # Download the EDF data file from the Host PC to a local data folder
    # parameters: source_file_on_the_host, destination_file_on_local_drive
    local_edf = os.path.join(results_folder, edf_file + '.EDF')
    el_tracker.receiveDataFile(edf_file, local_edf)
    # Close the link to the tracker.
    #el_tracker.close()
    el_tracker.setOfflineMode()
    # keep track of which components have finished
    RCheckComponents = [text_23, key_resp_6]
    for thisComponent in RCheckComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    RCheckClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "RCheck"-------
    while continueRoutine:
        # get current time
        t = RCheckClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=RCheckClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        
        # *key_resp_6* updates
        if key_resp_6.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            key_resp_6.clock.reset()  # now t=0
        if key_resp_6.status == STARTED:
            theseKeys = key_resp_6.getKeys(keyList=['s'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RCheckComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "RCheck"-------
    for thisComponent in RCheckComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run_loop.addData('text_23.started', text_23.tStartRefresh)
    run_loop.addData('text_23.stopped', text_23.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    run_loop.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        run_loop.addData('key_resp_6.rt', key_resp_6.rt)
    # the Routine "RCheck" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'run_loop'


# ------Prepare to start Routine "EndAA"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
EndAAComponents = [text_24, key_resp_8]
for thisComponent in EndAAComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndAAClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndAA"-------
while continueRoutine:
    # get current time
    t = EndAAClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndAAClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_24* updates
    if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_24.frameNStart = frameN  # exact frame index
        text_24.tStart = t  # local t and not account for scr refresh
        text_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
        text_24.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['s'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndAAComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndAA"-------
for thisComponent in EndAAComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_24.started', text_24.tStartRefresh)
thisExp.addData('text_24.stopped', text_24.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndAA" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
