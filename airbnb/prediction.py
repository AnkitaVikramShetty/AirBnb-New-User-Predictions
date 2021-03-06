# importing packages
import os
import time
from pprint import pprint

import numpy as np
import pandas as pd
import scipy.sparse as sp
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import LabelEncoder

from airbnb.models import train_users_2, sessions

start_time = time.time()


# -----------Make user features ---------------- #
def make_user_features(train, test):
    # encoding country destinations in train set
    outcome = train.country_destination
    labels = outcome.values
    le = LabelEncoder()
    y = le.fit_transform(labels)
    train = train.drop(['country_destination'], axis=1)

    # storing user ids in test set
    id_test = test['id']

    # appending test to train and dropping date first booking which is redundant
    data = pd.concat((train, test), axis=0, ignore_index=True)
    data = data.drop(['date_first_booking'], axis=1)

    # extracting features from date_account_created
    data['dac_year'] = data.date_account_created.apply(lambda x: x.year)
    data['dac_month'] = data.date_account_created.apply(lambda x: x.month)
    data['dac_weekday'] = data.date_account_created.apply(lambda x: x.weekday())
    data = data.drop(['date_account_created'], axis=1)

    # extracting features from timestamp_first_active
    data['tfa_year'] = data.timestamp_first_active.apply(lambda x: x.year)
    data['tfa_month'] = data.timestamp_first_active.apply(lambda x: x.month)
    data['tfa_weekday'] = data.timestamp_first_active.apply(lambda x: x.weekday())
    data = data.drop(['timestamp_first_active'], axis=1)

    # filling age nan with age median
    data.age = data.age.fillna(data.age.median())

    # binning age column
    bins = list(np.arange(15, 85, 5))
    bins.insert(0, 0)
    bins.append(int(max(data.age)))
    group_names = ['<15', '15-20', '20-25', '25-30', '30-35', '35-40', '40-45', '45-50',
                   '50-55', '55-60', '60-65', '65-70', '70-75', '75-80', '>80']
    data['age_bucket'] = pd.cut(data['age'], bins, labels=group_names)

    # cleaning gender column and filling nan in all dataframe with 'unknown'
    data.gender = data.gender.replace('-unknown-', 'unknown')
    data.ix[:, data.columns != 'age_bucket'] = data.ix[:, data.columns != 'age_bucket'].fillna('unknown')

    # generating dummy variables in top of categorical columns
    to_be_dummified = ['gender', 'signup_method', 'signup_flow', 'language', 'affiliate_channel',
                       'affiliate_provider', 'first_affiliate_tracked', 'signup_app',
                       'first_device_type', 'first_browser', 'age_bucket']
    for f in to_be_dummified:
        dummies = pd.get_dummies(data[f], prefix=f)
        data = data.drop([f], axis=1)
        data = pd.concat((data, dummies), axis=1)

    return data[:train.shape[0]], data[train.shape[0]:], y, le


# ------- Make Sessions features --------- #
def make_sessions_features(data, df_sessions):
    # Drop row with nan values from the "user_id" column as they're useless
    df_sessions = df_sessions.dropna(subset=["user_id"])

    # Frequency of devices - by user
    device_freq = df_sessions.groupby('user_id').device_type.value_counts()

    # Frequency of actions taken - by user
    action_freq = df_sessions.groupby('user_id').action.value_counts()

    # Total list of users
    users = data.id.values

    def feature_dict(df):
        f_dict = dict(list(df.groupby(level='user_id')))
        res = {}
        for k, v in f_dict.items():
            v.index = v.index.droplevel('user_id')
            res[k] = v.to_dict()
        return res

    # Make a dictionary with the frequencies { 'user_id' : {"IPhone": 2, "Windows": 1}}
    action_dict = feature_dict(action_freq)
    device_dict = feature_dict(device_freq)

    # Transform to a list of dictionaries
    action_rows = [action_dict.get(k, {}) for k in users]
    device_rows = [device_dict.get(k, {}) for k in users]

    device_transf = DictVectorizer()
    tf = device_transf.fit_transform(device_rows)

    action_transf = DictVectorizer()
    tf2 = action_transf.fit_transform(action_rows)

    # Concatenate the two datasets
    # Those are row vectors with the frequencies of both device and actions [0, 0, 0, 2, 0, 1, ...]
    features = sp.hstack([tf, tf2])

    # We create a dataframe with the new features and we write it to disk
    df_sess_features = pd.DataFrame(features.todense())

    df_sess_features['id'] = users

    # left joining data and sessions on user_id
    final = pd.merge(data, df_sess_features, how='left', left_on='id', right_on='id')
    final.ix[:, final.columns != 'age_bucket'].fillna(-1, inplace=True)

    final.drop(['id'], axis=1, inplace=True)
    return final


# ---------- Generate result --------------- #
def generate_result(y_pred, id_test, le, filename):
    ids = []  # list of ids
    cts = []  # list of countries
    for i in range(len(id_test)):
        idx = id_test[i]
        ids += [idx] * 5
        cts += le.inverse_transform(np.argsort(y_pred[i])[::-1])[:5].tolist()

    # Generate result
    sub = pd.DataFrame(np.column_stack((ids, cts)), columns=['id', 'country'])
    sub.to_csv(os.path.join('media', filename), index=False)
    print('Result File Successfully Generated')


# ---------- Function to predict country destination using bagging via random forest classifier ------ #
def predict():
    print("In prediction")
    return
    pretest = pd.read_csv(os.path.join('media', 'test_users.csv'), header=0, parse_dates=[1, 2, 3])
    pretrain = pd.DataFrame(list(train_users_2.objects.all().values()))
    df_sessions = pd.DataFrame(list(sessions.objects.all().values()))
    print(pretrain.head())
    train, test, y, le = make_user_features(pretrain, pretest)
    data = pd.concat((train, test), axis=0, ignore_index=True)
    final = make_sessions_features(data, df_sessions)

    X_train = final.ix[:train.shape[0] - 1]
    X_test = final.ix[train.shape[0]:]
    print('Train Set shape:', X_train.shape)
    print('Test Set shape:', X_test.shape)
    print('Labels shape:', y.shape)

    # fitting a Random Forest Classifier to select negligible features

    clf = RandomForestClassifier(n_estimators=160, oob_score=True, n_jobs=-1, criterion='entropy')
    clf.fit(X_train, y)
    print('Number of features to be discarded: ', np.count_nonzero(clf.feature_importances_ < 1e-4))

    # getting unimportant features
    unimportant_features = clf.feature_importances_ < 1e-4

    # Splitting Train set into Train and Test again to perform CV
    # The classification task is very challenging due to the data being extremely skewed.
    # Hence, we make sure to stratify our samples as almost 95% of them are covered by 3 classes only: NDF, US, OTHER.

    sub_X_train, sub_X_test, sub_y_train, sub_y_test = train_test_split(X_train, y, test_size=0.33, random_state=42,
                                                                        stratify=y)
    bagg = BaggingClassifier(random_state=42)

    param_grid = {"n_estimators": [10, 50, 100],
                  "max_samples": [0.1, 0.5, 1.0],
                  "max_features": [0.1, 0.5, 1.0]}

    baggsearch = GridSearchCV(bagg, param_grid, scoring='f1_weighted', cv=3, verbose=4, n_jobs=-1)
    baggsearch.fit(sub_X_train, sub_y_train)
    pprint(sorted(baggsearch.grid_scores_, key=lambda x: -x.mean_validation_score))
    print('F1 Weighted Score on Test Set',
          f1_score(sub_y_test, baggsearch.best_estimator_.predict(sub_X_test), average='weighted'))

    # training 5 separate Bagging Classifiers
    def bagging_prediction(X_train, y_train, X_test,
                           n_estimators=100,
                           max_samples=0.1,
                           max_features=1.0,
                           random_state=None):
        bagg = BaggingClassifier(random_state=random_state,
                                 n_estimators=n_estimators,
                                 max_samples=max_samples,
                                 max_features=max_features)
        bagg.fit(X_train.ix[:, ~unimportant_features], y_train)
        return bagg.predict_proba(X_test.ix[:, ~unimportant_features])

    probs = []
    for i in range(5):
        p = bagging_prediction(X_train, y,
                               X_test,
                               n_estimators=100,
                               random_state=i)
        probs.append(p)

    # We take the average of the 5 models
    avg_probs = sum(probs) / len(probs)
    y_pred = avg_probs
    id_test = pretest.id.values
    generate_result(y_pred, id_test, le, 'finalresult.csv')

    print("--- %s seconds ---" % (time.time() - start_time))


