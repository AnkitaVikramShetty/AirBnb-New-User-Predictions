import csv
import os

import time
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
import django_tables2 as tables

# Create your views here.
from new_user.matlabCode.classificationBaggedEnsembleByResampling import user_prediction
from new_user.matlabCode.visualizedData import visualize

from . models import test_users

def index(request):
    return render(request, "<h1>Welcome to Trial prediction 2 app homepage</h1>", context=None)

def user_upload(request):
    if request.method == 'POST' and request.FILES['users']:
        users = request.FILES['users']
        fileSystem = FileSystemStorage()

        filename = fileSystem.save(users.name, users)
        fileUrl = fileSystem.url(filename)

        return render(request, 'user_upload.html', {
            'originalFileName': users.name,
            'fileName': filename,
            'fileUrl': fileUrl
        })

    return render(request, 'user_upload.html')

def user_predict(request):
    user_prediction(request.GET.get('fileName',''))

    while not os.path.exists(os.path.join('media', 'results.csv')):
        time.sleep(1)

    if os.path.isfile(os.path.join('media', 'results.csv')):
        print("Exists")
        with open(os.path.join('media', 'results.csv')) as result:
            data = [{k: str(v) for k, v in row.items()}
                    for row in csv.DictReader(result, skipinitialspace=True)]
        table = render_result(data)
    else:
        raise ValueError("%s isn't a file!" % os.path.join('media', 'results.csv'))
    return render(request, 'new_user.html', {'result': table})

class render_result(tables.Table):
    id = tables.Column()
    country_destination = tables.Column()

    def render_id(self, value):
        return '%s' % value

def user_visualize(request):
    visualize(request.GET.get('fileName', ''))
    return render(request, 'user_visualize.html')