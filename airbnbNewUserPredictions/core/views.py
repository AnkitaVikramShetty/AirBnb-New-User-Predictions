# coding: utf-8

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from new_user.scripts.loadTestUsersToDatabase import load_users
from predict_app.scripts.load_users import load_users_method


def home_page(request):
    return render(request, 'core/index.html', context=None)


def about_us(request):
    return render(request, 'core/about.html', context=None)


def visualizations(request):
    return render(request, 'core/visualization.html', context=None)


def upload(request):
    if request.method == 'POST' and request.FILES['users']:
        users = request.FILES['users']
        # print(request.FILES)

        fileSystem = FileSystemStorage()
        # sqliteDatabase = test_users()

        filename = fileSystem.save(users.name, users)
        fileUrl = fileSystem.url(filename)

        # sqliteDatabase.save(users.value);
        load_users(users)
        load_users_method(users)

        return render(request, 'core/upload.html', {
            'originalFileName': users.name,
            'fileName': filename,
            'fileUrl': fileUrl
        })

    return render(request, 'core/upload.html')