import future as future
import matlab.engine
import pandas as pd
import numpy as np
import os

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

    if fileName == '':
        fileName = "test_users.csv";

    # fileName = "test_users.csv";
    print(fileName)

    fileName = os.path.join('media', fileName);
    dataframe = pd.read_csv(fileName);
    ids = dataframe.id.values

    dataframe = dataframe.drop(['id', 'date_first_booking'], axis=1)
    dataframe = dataframe.fillna(-1)

    dac = np.vstack(dataframe.date_account_created.astype(str).apply(lambda x: list(map(int, x.split('/')))).values)
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

    # gender = av = dataframe.age.values
    dataframe['gender'] = dataframe['gender'].map({'-unknown-': 1, 'MALE': 2, 'FEMALE': 3, 'OTHER': 4})
    dataframe['signup_method'] = dataframe['signup_method'].map({'facebook': 1, 'basic': 2, 'google': 3})
    dataframe['language'] = dataframe['language'].map({'en': 1, 'ca': 2, 'cs': 3, 'da': 4, 'de': 5, 'el': 6, 'es': 7, 'fi': 8, 'fr': 9, 'hr': 10, 'hu': 11, 'id': 12, 'is': 13, 'it': 14, 'ja': 15, 'ko': 16, 'nl': 17, 'no': 18, 'pl': 19, 'pt': 20, 'ru': 21, 'sv': 22, 'th': 23, 'tr': 24, 'zh': 25})
    dataframe['affiliate_channel'] = dataframe['affiliate_channel'].map({'direct': 1, 'seo': 2, 'other': 3, 'api': 4, 'content': 5, 'remarketing': 6, 'sem-brand': 7, 'sem-non-brand': 8})
    dataframe['affiliate_provider'] = dataframe['affiliate_provider'].map({'direct': 1, 'google': 2, 'other': 3, 'craigslist': 4, 'facebook': 5, 'baidu': 6, 'bing': 7, 'daum': 8, 'email-marketing': 9, 'facebook-open-graph': 10, 'gsp': 11, 'meetup': 12, 'naver': 13, 'padmapper': 14, 'vast': 15, 'wayn': 16, 'yahoo': 17, 'yandex': 18})
    dataframe['first_affiliate_tracked'] = dataframe['first_affiliate_tracked'].map({'': -1, 'untracked': 1, 'omg': 2, 'linked': 3, 'local ops': 4, 'marketing': 5, 'product': 6, 'tracked-other': 7})
    dataframe['signup_app'] = dataframe['signup_app'].map({'Web': 1, 'Android': 2, 'iOS': 3, 'Moweb': 4})
    dataframe['first_device_type'] = dataframe['first_device_type'].map({'Mac Desktop': 1, 'Windows Desktop': 2, 'iPhone': 3, 'Other/Unknown': 4, 'Android Phone': 5, 'Android Tablet': 6, 'Desktop (Other)': 7, 'iPad': 8, 'SmartPhone (Other)': 9})
    dataframe['first_browser'] = dataframe['first_browser'].map({'-unknown-': 1, 'Chrome': 2, 'IE': 3, 'Firefox': 4, 'Safari': 5, 'Mobile Safari': 6, 'Android Browser': 7, 'AOL Explorer': 8, 'Apple Mail': 9, 'Arora': 10, 'Avant Browser': 11, 'BlackBerry Browser': 12, 'Camino': 13, 'Chrome Mobile': 14, 'Chromium': 15, 'CometBird': 16, 'Comodo Dragon': 17, 'Conkeror': 18, 'CoolNovo': 19, 'Crazy Browser': 20, 'Epic': 21, 'Flock': 22, 'Google Earth': 23, 'Googlebot': 24, 'IceDragon': 25, 'IceWeasel': 26, 'IE Mobile': 27, 'Iron': 28, 'Kindle Browser': 29, 'Maxthon': 30, 'Mobile Firefox': 31, 'Mozilla': 32, 'NetNewsWire': 33, 'OmniWeb': 34, 'Opera': 35, 'Opera Mini': 36, 'Opera Mobile': 37, 'Pale Moon': 38, 'Palm Pre web browser': 39, 'PS Vita browser': 40, 'RockMelt': 41, 'SeaMonkey': 42, 'Silk': 43, 'SiteKiosk': 44, 'SlimBrowser': 45, 'Sogou Explorer': 46, 'Stainless': 47, 'TenFourFox': 48, 'TheWorld Browser': 49, 'wOSBrowser': 50, 'Yandex.Browser': 51})
    #dataframe['country_destination'] = dataframe['country_destination'].map({'NDF': 1, 'US': 2, 'other': 3, 'FR': 4, 'CA': 5, 'AU': 6, 'DE': 7, 'ES': 8, 'GB': 9, 'IT': 10, 'NL': 11, 'PT': 12})

    #vals = dataframe.values
    # x = matlab.double([[1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19],
    #                   [1, -1, 1, 0, 1, 1, 1, 1, 1, 1, 2, 2010, 6, 28, 2009, 3, 19]])

    # vals = matlab.double(vals);

    preProcessedFileName = "pre_processed.csv";
    preProcessedFileName = os.path.join('media', preProcessedFileName);

    dataframe.to_csv(preProcessedFileName);
    preProcessedFileName = os.path.abspath(preProcessedFileName);

    # matFile = "classificationBaggedEnsembleByResampling.mat";
    matFile = "dummy.mat";

    matFile = os.path.join('new_user', 'matlabCode', matFile);

    matFile = os.path.abspath(matFile);
    y = eng.predictUsingClassificationBaggedEnsembleByResampling(matFile, preProcessedFileName);

    print(y);

    # y = make_predictions(eng, vals)
    # print(y)

    # stop_matlab(eng)

    save_predictions(y, ids, 'results.csv')
    eng.quit()