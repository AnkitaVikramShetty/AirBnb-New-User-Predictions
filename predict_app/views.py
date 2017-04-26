import csv
import os
import time

from django.core.files.storage import FileSystemStorage
from django.http import  HttpResponse
from django.shortcuts import render

import django_tables2 as tables

from predict_app.scripts.classificationAlgorithm import predict_app_prediction
from predict_app.scripts.load_users import load_users_method
from predict_app.scripts.visualizedPredictedData import visualize

def index(request):
    return  HttpResponse("<h1> Trial Prediction - Home Page </h1>")

def predict_upload(request):
    if request.method == 'POST' and request.FILES['users']:
        users = request.FILES['users']
        print(request.FILES)

        fileSystem = FileSystemStorage()
        # sqliteDatabase = test_users()

        filename = fileSystem.save(users.name, users)
        fileUrl = fileSystem.url(filename)

        # sqliteDatabase.save(users.value);
        load_users_method(users);

        return render(request, 'predict_upload.html', {
            'originalFileName': users.name,
            'fileName': filename,
            'fileUrl': fileUrl
        })

    return render(request, 'predict_upload.html')

class render_result(tables.Table):
    results_id = tables.Column()
    country_destination = tables.Column()

    def render_id(self, value):
        return '%s' % value

def predict_predict(request):
    predict_app_prediction(request.GET.get('fileName',''))

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
    return render(request, 'predict_app.html', {'result': table})

def predict_visualize(request):
    visualize(request.GET.get('fileName', ''))
    return render(request, 'predict_visualize.html')
