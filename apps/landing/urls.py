# coding=utf-8
from django.conf.urls import url, include

from .views import LandingView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='index'),
]