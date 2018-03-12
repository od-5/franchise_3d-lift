# coding=utf-8
from django import forms

from .models import MailTicket

__author__ = 'alexy'


class MailTicketTicketForm(forms.ModelForm):
    class Meta:
        model = MailTicket
        fields = ('email', 'phone')
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': u'Ваш e-mail'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': u'Ваш номер телефона'})
        }
