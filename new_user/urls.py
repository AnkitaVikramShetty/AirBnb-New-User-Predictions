from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^go_to_new_user/$', 'new_user.views.go_to_new_user', name='go_to_new_user'),
]