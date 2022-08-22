# ASAP Active Escape Task
fMRI task used to explore emotion-motor interactions

### In this task, participants will view a countdown on the screen before making a quick motor response using a joystick. Depending on participants' performance, as well as the type of trial they completed, they may or may not receive a shock.

This is a 2( Controllability:Controllable/Uncontrollable) x2 (Shock Intensity:Perceptible/Unpleasant) design, such that there are four trial types in total:

  - Controllable, Perceptible:
      - participants can try to make a *successful* motor response to avoid a **perceptible** shock
      
  - Controllable, Unpleasant:
      - participants can try to make a *successful* motor response to avoid an **unpleasant** shock
      
  - Uncontrollable, Perceptible:
      - participants can try to make a motor response, but will receive a **perceptible** shock *regardless* of their performance

  - Uncontrollable, Unpleasant:
      - participants can try to make a motor response, but will receive an **unpleasant** shock *regardless* of their performance


The motor response involves the use of a joystick to move a center cursor, a small triangle, to a target circle which will be randomly placed in one of the four corners of the screen. Participants have 940ms to complete this motor response. A successful response is defined as any overlap of the cursor with the target circle. 

Following the motor response, participants will be responding to two questions about their emotional experience.

![Active Escape task design!](https://github.com/LEAPNeuroLab/ASAP/blob/main/Active%20Escape/TaskDesign/AE_taskDesign.png "Active Escape Design")



#### Scripts in this repository

This study uses all of the scripts included in this repository. In the order in which we run the scripts,:

AE_StimTest.py - a test of the shock machine to get acquainted with what a shock feels like. Participants receive one very mild shock, then a sequence of 3 pulses of the same shock intensity.

AE_Calibrations.py - a script that calls on three scripts within it. This is used to calibrate the shock intensity that will be used in the main task. Participants complete calibration for a perceptible shock and then an unpleasant shock. We do this outside of the scanner bore, but while the participants are laying on the scanner bed. Then, participants complete the calibration for the perceptible and unpleasant shock one more time, inside the scanner. These calibrations *start off* with the level of shock the participant decided on in the first iteration.

joystickTest.py - a script for the participant to get used to using the joystick. Participants are instructed to press the buttons on the joystick and use the thumbstick to move a cursor around, simulating the motor response in the main task.

AE_practice.py - a script for practice trials of the main task; also includes the instructions for the task. 

fixation.py - a script that shows a fixation on the screen. Used while the localizer, T1, and GRE scans are running. 

AE_final.py - the main task!
