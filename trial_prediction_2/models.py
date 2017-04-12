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

# album = models.Foreignkey(Album, on_delete = models.CASCADE)