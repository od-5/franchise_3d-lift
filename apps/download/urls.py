# coding=utf-8
from django.conf.urls import url

from .ajax import bp_download

urlpatterns = [
    url(r'^$', bp_download, name='send'),
]
