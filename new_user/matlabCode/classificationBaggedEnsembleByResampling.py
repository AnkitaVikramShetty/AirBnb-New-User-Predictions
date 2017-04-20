import future as future
import matlab.engine
import pandas as pd
import numpy as np

def start_matlab():
    eng = matlab.engine.connect_matlab()
    # print(matlab.engine.find_matlab())

    return eng

def make_predictions(eng, x):
    print("Calling function")
    y = eng.predictUsingClassificationBaggedEnsembleByResampling("S:\Files\MASTERS\database design\project\\test.mat",x);

    return y

def stop_matlab(eng):
    eng.quit()


def save_predictions(y):
    pass


def user_prediction():
    eng = start_matlab()

    dataframe = pd.read_csv("S:/Users/Maaz/airbnbNewUserPredictions/media/test_users.csv");
    dataframe = dataframe.drop(['id', 'date_first_booking'], axis=1)
    dataframe = dataframe.fillna(-1)

    dac = np.vstack(dataframe.date_account_created.astype(str).apply(lambda x: list(map(int, x.split('-')))).values)
    dataframe['dac_year'] = dac[:, 0]
    dataframe['dac_month'] = dac[:, 1]
    dataframe['dac_day'] = dac[:, 2]
    dataframe = dataframe.drop(['date_account_created'], axis=1)

    tfa = np.vstack(dataframe.timestamp_first_active.astype(str).apply(
        lambda x: list(map(int, [x[:4], x[4:6], x[6:8], x[8:10], x[10:12], x[12:14]]))).values)
    dataframe['tfa_year'] = tfa[:, 0]
    dataframe['tfa_month'] = tfa[:, 1]
    dataframe['tfa_day'] = tfa[:, 2]
    dataframe = dataframe.drop(['timestamp_first_active'], axis=1)

    av = dataframe.age.values
    dataframe['age'] = np.where(np.logical_or(av < 14, av > 100), -1, av)

    gender = av = dataframe.age.values
    dataframe['gender'] = dataframe['gender'].map({'-unknown-': 1, 'MALE': 2, 'FEMALE': 3, 'OTHER': 4})

    vals = dataframe.values
    x = matlab.double([[1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19],
                      [1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19]])
    y = make_predictions(eng, x)
    print(y)

    stop_matlab(eng)
    save_predictions(y)