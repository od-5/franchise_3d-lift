# coding=utf-8
from django.conf.urls import url

from .views import ticket_form

urlpatterns = [
    url(r'^$', ticket_form, name='send'),
]
