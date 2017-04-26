from new_user.matlabCode.preProcess import pre_process
from new_user.models import test_users, pre_processed_data
import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import seaborn as sns
import os

def visualize(originalFileName):
    pre_process();
    # users = pd.read_csv(fileName);
    users = pd.DataFrame(list(pre_processed_data.objects.all().values()))

    users['gender'] = users['gender'].map({"1": '-unknown-', "2": 'MALE', "3": 'FEMALE', "4": 'OTHER'});
    users.gender.value_counts(dropna=False).plot(kind='bar', color='#FD5C64', rot=0)
    plt.xlabel('Gender')
    sns.despine()

    plt.savefig(os.path.join('airbnbNewUserPredictions/static/img/gender_count.png'))
    plt.close()

    sns.distplot(users[users.age != -1].age, color='#FD5C64')
    plt.xlabel('Age')
    sns.despine()

    plt.savefig(os.path.join('airbnbNewUserPredictions/static/img/age.png'))
    plt.close()

    # if originalFileName == '':
    #     originalFileName = "test_users.csv";
    #
    # # fileName = "test_users.csv";
    # print(originalFileName)
    #
    # fileName = os.path.join('media', originalFileName);

    users = pd.DataFrame(list(test_users.objects.all().values()))
    # users = pd.read_csv(fileName);

    users['date_account_created'] = pd.to_datetime(users['date_account_created'])

    sns.set_style("whitegrid", {'axes.edgecolor': '0'})
    sns.set_context("poster", font_scale=1.1)
    users.date_account_created.value_counts().plot(kind='line', linewidth=1.2, color='#FD5C64')

    plt.savefig(os.path.join('airbnbNewUserPredictions/static/img/date_account_created.png'))
    plt.close()