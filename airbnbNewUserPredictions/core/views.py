# coding: utf-8

import datetime

from django.core.checks import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse as r
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from airbnbNewUserPredictions.core.models import Product
from airbnbNewUserPredictions.sniffer.crawler import AirbnbNewUserPredictions


def home_page(request):
    return render(request, 'core/index.html', context=None)


def about_us(request):
    return render(request, 'core/about.html', context=None)


def elements(request):
    return render(request, 'core/elements.html', context=None)


def visualizations(request):
    return render(request, 'core/visualization.html', context=None)
