import csv
import os
import sys

# csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

# Full path and name to your csv file
csv_filepathname = "sessions_10.csv"
# Full path to your django project directory
your_djangoproject_home = "../"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'airbnbNewUserPredictions.settings'

# Make sure to uncomment line based on the app you are using
# from trial_predictions.models import countries
# from trial_prediction_2.models import countries
from airbnb.models import sessions, train_users_2, countries

count = 0
dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    count += 1
    if row[0] != 'user_id':  # Ignore the header row, import everything else
        print(count)
        session = sessions()
        session.user_id = train_users_2.objects.get(id=row[0])
        session.action = row[1]
        session.action_type = row[2]
        session.action_detail = row[3]
        session.device_type = row[4]
        session.secs_elapsed = row[5]
        session.save()
