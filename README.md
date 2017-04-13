# AirBnb-New-User-Predictions commands

windows powershell -> run as administrator
sudo
phyton --version -> Python 3.4.3
https://askubuntu.com/questions/320996/how-to-make-python-program-command-execute-python-3
pip --version (or) easy_install --version
Python34 -> Scripts -> easy_install -> properties -> location
computer -> properties -> advanced system settings -> environment variables -> PATH
easy_install django
django-admin --version
django-admin startproject website
python manage.py runserver
python manage.py startapp music
python manage.py migrate

python manage.py makemigrations trial_prediction_2
python manage.py sqlmigrate trial_prediction_2 <id>

python manage.py shell
from trial_prediction_2.models import countries, train_users_2, age_gender_bkts, test_users, sessions
countries.objects.all()

a = countries(country_destination="AU", ...)
a.save()
a.country_destination
a.id/a.pk

b = countries()
b.countries = "AU"
b.save()