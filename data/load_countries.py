import csv
import os
import sys

# csv.field_size_limit(sys.maxsize)
csv.field_size_limit(2147483647)

# Full path and name to your csv file
csv_filepathname = "countries.csv"
# Full path to your django project directory
your_djangoproject_home = "../"

sys.path.append(your_djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'airbnbNewUserPredictions.settings'

# Make sure to uncomment line based on the app you are using
# from trial_predictions.models import countries
# from trial_prediction_2.models import countries
from airbnb.models import countries

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"')
for row in dataReader:
    if row[0] != 'country_destination':  # Ignore the header row, import everything else
        country = countries()
        country.country_destination = row[0]
        country.lat_destination = row[1]
        country.lng_destination = row[2]
        country.distance_km = row[3]
        country.destination_km2 = row[4]
        country.destination_language = row[5]
        country.language_levenshtein_distance = row[6]
        country.save()
