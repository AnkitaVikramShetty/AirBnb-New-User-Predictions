import csv
import os.path
import time

import django_tables2 as tables
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from airbnb.prediction import predict


class RenderResult(tables.Table):
    id = tables.Column()
    country = tables.Column()

    def render_id(self, value):
        return '%s' % value


def index(request):
    return render(request, 'airbnb.html', context=None)


def upload_file(request):
    if request.method == 'POST' and request.FILES['test_users']:
        test_users = request.FILES['test_users']
        fs = FileSystemStorage()
        filename = fs.save(test_users.name, test_users)
        uploaded_file_url = fs.url(filename)
        return render(request, 'upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'upload.html')


def prediction(request):
    predict()

    while not os.path.exists(os.path.join('media', 'finalresult.csv')):
        time.sleep(1)

    if os.path.isfile(os.path.join('media', 'finalresult.csv')):
        print("Exists")
        with open(os.path.join('media', 'finalresult.csv')) as result:
            data = [{k: str(v) for k, v in row.items()}
                    for row in csv.DictReader(result, skipinitialspace=True)]
        table = RenderResult(data)
    else:
        raise ValueError("%s isn't a file!" % os.path.join('media', 'finalresult.csv'))
    return render(request, 'airbnb.html', {'result': table})


