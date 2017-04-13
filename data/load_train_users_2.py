import sys, os
import csv

# csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

# Full path and name to your csv file
csv_filepathname = "users.csv"
# Full path to your django project directory
your_djangoproject_home = "../"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'airbnbNewUserPredictions.settings'

# from trial_prediction_2.models import train_users_2, countries
# from trial_predictions.models import train_users_2, countries
from airbnb.models import train_users_2, countries

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
