from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to Trial prediction 2 app homepage</h1>")

def go_to_new_user(request):
    return render(request, 'new_user.html')