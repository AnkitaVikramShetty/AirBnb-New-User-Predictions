from django.http import  HttpResponse

def index(request):
    return  HttpResponse("<h1> Trial Prediction - Home Page </h1>")
