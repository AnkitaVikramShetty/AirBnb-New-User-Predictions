from django.db import models

# Create your models here.
class countries(models.Model):
    country_destination = models.CharField(max_length=2)
    lat_destination = models.FloatField()
    lng_destination = models.FloatField()
    distance_km = models.FloatField()
    destination_km2 = models.IntegerField()
    destination_language = models.CharField(max_length=3)
    language_levenshtein_distance = models.FloatField()

'''
class train_users_2(models.Model):
    id
    date_account_created 
    timestamp_first_active
    date_first_booking
    gender
    age
    signup_method
    signup_flow
    language
    affiliate_channel
    affiliate_provider
    first_affiliate_tracked
    signup_app
    first_device_type
    first_browser
    country_destination

    # album = models.Foreignkey(Album, on_delete = models.CASCADE)
    
class age_gender_bkts(models.Model):
    age_bucket
    country_destination
    gender
    population_in_thousands
    year

class test_users(models.Model):
    id
    date_account_created 
    timestamp_first_active
    date_first_booking
    gender
    age
    signup_method
    signup_flow
    language
    affiliate_channel
    affiliate_provider
    first_affiliate_tracked
    signup_app
    first_device_type
    first_browser

class sessions(models.Model):
    user_id
    action
    action_type
    action_detail
    device_type
    secs_elapsed
'''