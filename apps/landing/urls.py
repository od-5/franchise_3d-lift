# coding=utf-8
from django.conf.urls import url, include

from .views import LandingView, OkView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='index'),
    url(r'^ok/$', OkView.as_view(), name='ok'),
]