from django.db import models

# Create your models here.
class countries(models.Model):
    country_destination = models.CharField(max_length=2)
    lat_destination = models.DecimalField()
    lng_destination = models.DecimalField()
    distance_km = models.DecimalField()
    destination_km2 = models.IntegerField()
    destination_language = models.CharField(max_length=3)
    language_levenshtein_distance = models.FloatField()

# album = models.Foreignkey(Album, on_delete = models.CASCADE)