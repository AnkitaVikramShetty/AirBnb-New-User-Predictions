from django.contrib import admin
from .models import test_users, countries

# Register your models here.
admin.site.register(test_users)
admin.site.register(countries)