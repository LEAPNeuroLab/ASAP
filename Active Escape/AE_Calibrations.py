# ASAP Calibrations
# Joanne Stasiak
#2022
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Run calibration scripts for the main task to grab the shock values from the resultant text files
'''

from stimCalibration_Perceptible10v1 import * #Run the first perceptible calibration - this is done in the MRI room, but outside of the scanner bore
from stimCalibration_Unpleasant10v1_sure import * #Run the first unpleasant calibration - this is done in the MRI room, but outside of the scanner bore
from stimCalibration_Perceptible10v2 import * #Run the second perceptible calibration - this is done inside of the scanner
#And will start off with their perceptible shock that they decided on

from stimCalibration_Unpleasant10v2_sure import *#Run the second unpleasant calibration (also in the scanner)
#This will also start off with the level of unpleasant shock decided on in the first round
