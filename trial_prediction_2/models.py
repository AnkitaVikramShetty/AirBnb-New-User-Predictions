from django import forms
from django.db import models
from airbnbNewUserPredictions import settings

# Create your models here.


class countries(models.Model):
    country_destination = models.CharField(max_length=2, primary_key=True)
    lat_destination = models.FloatField()
    lng_destination = models.FloatField()
    distance_km = models.FloatField()
    destination_km2 = models.FloatField()
    destination_language = models.CharField(max_length=3)
    language_levenshtein_distance = models.FloatField()

class train_users_2(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date_account_created = models.CharField(max_length=50, blank=True)
    timestamp_first_active = models.CharField(max_length=6)
    date_first_booking = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(blank=True)
    signup_method = models.CharField(max_length=20)
    signup_flow = models.IntegerField
    language = models.CharField(max_length=3)
    affiliate_channel = models.CharField(max_length=15)
    affiliate_provider = models.CharField(max_length=15)
    first_affiliate_tracked = models.CharField(max_length=15, blank=True)
    signup_app = models.CharField(max_length=15)
    first_device_type = models.CharField(max_length=15)
    first_browser = models.CharField(max_length=15)
    country_destination = models.ForeignKey(countries, on_delete = models.CASCADE)
    
class age_gender_bkts(models.Model):
    age_bucket = models.CharField(max_length=15)
    country_destination = models.ForeignKey(countries, on_delete = models.CASCADE)
    gender =  models.CharField(max_length=10)
    population_in_thousands =  models.IntegerField
    year = models.IntegerField

class test_users(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date_account_created = models.CharField(max_length=50, blank=True)
    timestamp_first_active = models.CharField(max_length=6)
    date_first_booking = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10)
    age = models.IntegerField(blank=True)
    signup_method = models.CharField(max_length=20)
    signup_flow = models.IntegerField
    language = models.CharField(max_length=3)
    affiliate_channel = models.CharField(max_length=15)
    affiliate_provider = models.CharField(max_length=15)
    first_affiliate_tracked = models.CharField(max_length=15, blank=True)
    signup_app = models.CharField(max_length=15)
    first_device_type = models.CharField(max_length=15)
    first_browser = models.CharField(max_length=15)

class sessions(models.Model):
    user_id = models.ForeignKey(train_users_2, on_delete=models.CASCADE)
    action = models.CharField(max_length=50)
    action_type = models.CharField(max_length=50, blank=True)
    action_detail = models.CharField(max_length=50, blank=True)
    device_type = models.CharField(max_length=50)
    secs_elapsed = models.IntegerField


