import future as future
import matlab.engine
import pandas as pd
import numpy as np
import os

from new_user.matlabCode.preProcess import pre_process


def start_matlab():
    eng = matlab.engine.connect_matlab()
    # print(matlab.engine.find_matlab())

    return eng

def make_predictions(eng, x):
    print("Calling function")
    y = eng.predictUsingClassificationBaggedEnsembleByResampling("classificationBaggedEnsembleByResampling.mat",x);

    return y

def stop_matlab(eng):
    eng.quit()


def save_predictions(y, ids, filename):
    sub = pd.DataFrame(np.column_stack((ids, y)), columns=['id', 'country_destination'])
    sub['country_destination'] = sub['country_destination'].map(
        {1: 'NDF', 2: 'US', 3: 'other', 4: 'FR', 5: 'CA', 6: 'AU', 7: 'DE', 8: 'ES', 9: 'GB', 10: 'IT', 11: 'NL',
         12: 'PT'})

    sub.to_csv(os.path.join('media', filename), index=False)
    print('Results generated')

def user_prediction(fileName):
    eng = start_matlab()
    ids, preProcessedFileName = pre_process(fileName)
    print(preProcessedFileName)

    # matFile = "classificationBaggedEnsembleByResampling.mat";
    matFile = "dummy.mat";

    matFile = os.path.join('new_user', 'matlabCode', matFile);

    matFile = os.path.abspath(matFile);
    print(matFile)
    y = eng.predictUsingClassificationBaggedEnsembleByResampling(matFile, preProcessedFileName);

    print(y);

    # y = make_predictions(eng, vals)
    # print(y)

    # stop_matlab(eng)

    save_predictions(y, ids, 'results.csv')
    eng.quit()