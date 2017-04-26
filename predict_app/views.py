from django.core.files.storage import FileSystemStorage
from django.http import  HttpResponse
from django.shortcuts import render

from predict_app.scripts import load_users
import django_tables2 as tables

def index(request):
    return  HttpResponse("<h1> Trial Prediction - Home Page </h1>")

def predict_upload(request):
    if request.method == 'POST' and request.FILES['users']:
        users = request.FILES['users']
        # print(request.FILES)

        fileSystem = FileSystemStorage()
        # sqliteDatabase = test_users()

        filename = fileSystem.save(users.name, users)
        fileUrl = fileSystem.url(filename)

        # sqliteDatabase.save(users.value);
        load_users(users);

        return render(request, 'user_upload.html', {
            'originalFileName': users.name,
            'fileName': filename,
            'fileUrl': fileUrl
        })

    return render(request, 'user_upload.html')

class render_result(tables.Table):
    results_id = tables.Column()
    country_destination = tables.Column()

    def render_id(self, value):
        return '%s' % value
