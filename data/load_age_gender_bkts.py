import sys, os
import csv

#csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

# Full path and name to your csv file
csv_filepathname="age_gender_bkts.csv"
# Full path to your django project directory
your_djangoproject_home = "../"


sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'airbnbNewUserPredictions.settings'

from new_user.models import age_gender_bkts, countries
# from trial_prediction_2.models import age_gender_bkts, countries
# from trial_predictions.models import age_gender_bkts, countries


dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')

count = 0
for row in dataReader:
    count += 1
    print(count)
    if row[0] != 'age_bucket': # Ignore the header row, import everything else
        age_gender_bkt = age_gender_bkts()
        age_gender_bkt.age_bucket = row[0]
        age_gender_bkt.country_destination = countries.objects.get(country_destination = row[1])
        age_gender_bkt.gender = row[2]
        age_gender_bkt.population_in_thousands = row[3]
        age_gender_bkt.year = row[4]
        age_gender_bkt.save()