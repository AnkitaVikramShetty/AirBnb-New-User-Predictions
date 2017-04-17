from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^predict/$', 'airbnb.views.prediction', name='predict'),
    url(r'^upload/$', 'airbnb.views.upload_file', name='upload')
]