from django.conf.urls import patterns, include, url

urlpatterns = patterns('airbnbNewUserPredictions.api.views',
    url(r'^product/$', 'product', name='product'),
)
