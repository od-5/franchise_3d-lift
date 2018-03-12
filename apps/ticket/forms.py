# coding=utf-8
from django import forms
from .models import Ticket

__author__ = 'alexy'


class MainTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input', 'placeholder': u'Ваше имя'}),
            'phone': forms.TextInput(attrs={'class': 'input', 'placeholder': u'Ваш телефон'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': u'Ваш e-mail'})
        }

