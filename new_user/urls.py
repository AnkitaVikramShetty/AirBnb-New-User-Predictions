from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_upload/$', 'new_user.views.user_upload', name='user_upload'),
    url(r'^user_predict/$', 'new_user.views.user_predict', name='user_predict'),
    url(r'^user_visualize/$', 'new_user.views.user_visualize', name='user_visualize'),
]