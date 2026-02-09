#!/usr/bin/env python
# coding: utf-8

import numpy as np
import json
from pprint import pprint
from scipy.stats import rankdata
import sys
import os

# sub=sys.argv[0]
# TMScond=sys.argv[2]
dir="/work/stasiak/asap/processed"
# subjects = ["063", "064", "065", "066", "067", "068", "069", "070", "071", "072", "074", "075", "076", "077", "078", "079",  "081", "082", "084", "086"]
subjects = ['080']
runs = [1, 2, 3, 4, 5, 6, 7]
for sub in subjects:
    outdir1=os.path.join(dir, sub, "func")
    if not os.path.exists(outdir1):
       os.makedirs(outdir1)
    outdir=os.path.join(outdir1,"SliceTime")
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    for run in runs:
        currfn = os.path.join(outdir1,sub+ "_run"+str(run)+".json")
        data = json.load(open(currfn))
        #pprint(data)
        sliceTimes=data['SliceTiming']
        #sliceOrder=np.argsort(sliceTimes)+1
        sliceOrder=rankdata(sliceTimes).astype(int)
        fn=outdir + '/sliceTimeOrder_run' + str(run)
        np.savetxt(fn,sliceOrder.astype(int),fmt='%i')
