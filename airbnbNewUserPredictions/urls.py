"""airbnbNewUserPredictions URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Home page view
    url(r'^$', 'airbnbNewUserPredictions.core.views.home_page', name='home'),
    # About button
    url(r'^about/$', 'airbnbNewUserPredictions.core.views.about_us', name='about'),
    # Elements button
    url(r'^visualizations/$', 'airbnbNewUserPredictions.core.views.visualizations', name='visualizations'),
    url(r'^upload_page/$', 'airbnbNewUserPredictions.core.views.upload', name='upload_page'),
    url(r'^new_user/', include('new_user.urls')),
    url(r'^predict_app/', include('predict_app.urls')),
    url(r'^airbnb/', include('airbnb.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
