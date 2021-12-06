#!/usr/bin/env python

import sys
import json
import pip 
import os
import subprocess

sys.path.insert(0, 'src/data')
sys.path.insert(0, 'src/analysis')
sys.path.insert(0, 'src/model')

from etl import get_data
from analysis import compute_aggregates
from model import train


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
   

    # step2 = 'cd extern/engines/python && '
    # p = 'python setup.py install'
    # os.system('cd C:/Program Files/MATLAB/R2021b && ' + step2 + p)
    # os.system('python3 setup.py install') 
    # os.system('cmd /k "date"') 

    #if you get error like error: could not create 'build' : Access is denied
    #must run these commands by running command prompt on administrator

    print("starting")

    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.matlab_script_00_download(nargout=0)

    eng.matlab_script_01_datainfo(nargout=0)

    #filepath to Rscript
    command ='C:/Program Files/R/R-4.0.2/bin/Rscript'

    retcode = subprocess.check_call([command, 'readMCdata.R'], shell=True)
    retcode = subprocess.check_call([command, 'configCytoEuler_inhibitor.R'], shell=True)
    retcode = subprocess.check_call([command, 'massCytoRuns_inhibitor.R'], shell=True)
    retcode = subprocess.check_call([command, 'aggregate.R'], shell=True)

     # from pip._internal import main as pip
    # pip(['install', '--user', 'oct2py'])
    # import oct2py



    # script = "b = 5;\n" \
    #          "h = 3;\n" \
    #          "a = 0.5*(b.* h)"

    # with open("myScript.m","w+") as f:
    #     f.write(script)

    # eng = matlab.engine.start_matlab()
    # eng.myScript(nargout=0)

    # from oct2py import Oct2Py
    # oc = Oct2Py()


    # script = "function y = myScript(x)\n" \
    #          "    y = x-5" \
    #          "end"

    # with open("myScript.m","w+") as f:
    #     f.write(script)

    # oc.myScript(7)

    


    print("finished installing")


    if 'data' in targets:
        with open('config/data-params.json') as fh:
            data_cfg = json.load(fh)

        # make the data target
        data = get_data(**data_cfg)

    if 'analysis' in targets:
        with open('config/analysis-params.json') as fh:
            analysis_cfg = json.load(fh)

        # make the data target
        compute_aggregates(data, **analysis_cfg)

    if 'model' in targets:
        with open('config/model-params.json') as fh:
            model_cfg = json.load(fh)

        # make the data target
        train(data, **model_cfg)

    return


if __name__ == '__main__':
    # run via:
    # python main.py data model
    targets = sys.argv[1:]
    main(targets)
