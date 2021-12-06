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
    Runs the main project pipeline logic
    '''


    #Paths to rStudio and Matlab Applications: 
    rStudioPath ='C:/Program Files/R/R-4.0.2/bin/Rscript'
    matLabPath ='C:/Program Files/MATLAB/R2021b'



    step1 = 'cd ' + matLabPath + ' && ' 
    step2 = 'cd extern/engines/python && '
    p = 'python setup.py install'
    os.system(step1 + step2 + p)
    os.system('python3 setup.py install') 
    os.system('cmd /k "date"') 

    #if you get error like error: could not create 'build' : Access is denied
    #must run these commands by running command prompt on administrator

    print("------------STEP 1) starting matlab files")

    import matlab.engine
    eng = matlab.engine.start_matlab()
    eng.matlab_script_00_download(nargout=0)
    eng.matlab_script_01_datainfo(nargout=0)
    eng.matlab_script_02_getInfo(nargout=0)


    print("------------STEP 2) starting rstudio files")

    retcode = subprocess.check_call([rStudioPath, 'readMCdata.R'], shell=True)
    retcode = subprocess.check_call([rStudioPath, 'configCytoEuler_inhibitor.R'], shell=True)
    retcode = subprocess.check_call([rStudioPath, 'massCytoRuns_inhibitor.R'], shell=True)
    retcode = subprocess.check_call([rStudioPath, 'aggregate.R'], shell=True)

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
