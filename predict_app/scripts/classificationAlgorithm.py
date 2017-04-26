import matlab.engine
import pandas as pd
import numpy as np
import os

from predict_app.models import results, pre_processed_data, test_users

from sqlalchemy import create_engine

from predict_app.scripts.preprocessData import pre_process_data


def start_matlab():
    eng = matlab.engine.connect_matlab()
    return eng

def make_predictions(eng, x):
    y = eng.predictUsingClassificationBaggedEnsembleByResampling("classificationBaggedEnsembleByResampling.mat",x);
    return y

def stop_matlab(eng):
    eng.quit()

def save_predictions(y, ids, filename):
    sub = pd.DataFrame(np.column_stack((ids, y)), columns=['results_id', 'country_destination'])
    sub['country_destination'] = sub['country_destination'].map(
        {1: 'NDF', 2: 'US', 3: 'other', 4: 'FR', 5: 'CA', 6: 'AU', 7: 'DE', 8: 'ES', 9: 'GB', 10: 'IT', 11: 'NL',
         12: 'PT'})

    results.objects.all().delete()
    disk_engine = create_engine('sqlite:///db.sqlite3')
    sub.to_sql('predict_app_results', disk_engine, if_exists='append', index=False)

    sub.to_csv(os.path.join('media', filename), index=False)
    print('Results generated')

def predict_app_prediction(fileName):
    eng = start_matlab()

    pre_process_data()
    dataframe = pd.DataFrame(list(pre_processed_data.objects.all().values()))
    dataframe = dataframe.drop(['id'], axis=1)

    preProcessedFileName = "pre_processed.csv";
    preProcessedFileName = os.path.join('media', preProcessedFileName);

    dataframe.to_csv(preProcessedFileName);
    preProcessedFileName = os.path.abspath(preProcessedFileName);

    # matFile = "classificationBaggedEnsembleByResampling.mat";
    matFile = "dummy.mat";

    matFile = os.path.join('predict_app', 'scripts', matFile);

    matFile = os.path.abspath(matFile);
    print(matFile)

    y = eng.predictUsingClassificationBaggedEnsembleByResampling(matFile, preProcessedFileName);
    print(y);

    os.remove(preProcessedFileName)
    print("File Removed!")
    # y = make_predictions(eng, vals)
    # print(y)

    # stop_matlab(eng)
    dataframe = pd.DataFrame(list(test_users.objects.all().values()))
    ids = dataframe.id.values

    save_predictions(y, ids, 'results.csv')
    eng.quit()