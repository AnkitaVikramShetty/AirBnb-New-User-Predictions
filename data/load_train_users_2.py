import sys, os
import csv

import numpy as np
import pandas as pd

# csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

# Full path and name to your csv file
csv_filepathname = "train_users_2_copy.csv"
# Full path to your django project directory
your_djangoproject_home = "../"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'airbnbNewUserPredictions.settings'

from new_user.models import train_users_2, countries
# from new_user.models import train_users_2, countries
# from trial_predictions.models import train_users_2, countries
# from new_user.models import train_users_2, countries

dataframe = pd.read_csv(csv_filepathname)

av = dataframe.age.values
dataframe['age'] = np.where(np.logical_or(av < 14, av > 100), -1, av)

dataframe = dataframe.fillna(-1)
dataframe.to_csv(csv_filepathname, index=False)
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

count = 0
for row in dataReader:
    count += 1
    if row[0] != 'id':  # Ignore the header row, import everything else
        print(count)
        train_user_2 = train_users_2()
        train_user_2.id = row[0]
        train_user_2.date_account_created = row[1]
        train_user_2.timestamp_first_active = row[2]
        train_user_2.date_first_booking = row[3]
        train_user_2.gender = row[4]
        train_user_2.age = row[5]
        train_user_2.signup_method = row[6]
        train_user_2.signup_flow = row[7]
        train_user_2.language = row[8]
        train_user_2.affiliate_channel = row[9]
        train_user_2.affiliate_provider = row[10]
        train_user_2.first_affiliate_tracked = row[11]
        train_user_2.signup_app = row[12]
        train_user_2.first_device_type = row[13]
        train_user_2.first_browser = row[14]
        train_user_2.country_destination = countries.objects.get(country_destination=row[15])
        train_user_2.save()
