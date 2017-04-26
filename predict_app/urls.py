from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^predict_upload/$', 'predict_app.views.predict_upload', name='predict_upload'),
]