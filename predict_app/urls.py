from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^predict_upload/$', 'predict_app.views.predict_upload', name='predict_upload'),
    url(r'^predict_predict/$', 'predict_app.views.predict_predict', name='predict_predict'),
    url(r'^predict_visualize/$', 'predict_app.views.predict_visualize', name='predict_visualize'),
]