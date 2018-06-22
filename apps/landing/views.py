# coding=utf-8
from __future__ import unicode_literals

from django.views.generic import TemplateView

from apps.ticket.forms import MainTicketForm
from .models import Setup, Block1, Block2, Client, Block3, Block4, Block5, Block6, Block41


class LandingView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        block1 = Block1.objects.all()
        block2 = Block2.objects.all()
        block3 = Block3.objects.all()
        block4 = Block4.objects.all()
        block41 = Block41.objects.all()
        block5 = Block5.objects.all()
        block6 = Block6.objects.all()
        client_qs = Client.objects.all()
        context.update({
            'block1': block1,
            'block2': block2,
            'block3': block3,
            'block4': block4,
            'block41': block41,
            'block5': block5,
            'block6': block6,
            'client_list': client_qs,
            'form': MainTicketForm(),
            'setup': Setup.objects.first()
        })
        return context


class OkView(TemplateView):
    template_name = 'ok.html'

    def get_context_data(self, **kwargs):
        context = super(OkView, self).get_context_data(**kwargs)
        context.update({
            'setup': Setup.objects.first()
        })
        return context
