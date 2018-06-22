# coding=utf-8
from django.conf.urls import url

from .views import ticket_form, TicketCreateView

urlpatterns = [
    url(r'^$', ticket_form, name='send'),
    url(r'^calc/$', TicketCreateView.as_view(), name='calc'),
]
