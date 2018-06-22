# coding=utf-8
from __future__ import unicode_literals

from annoying.decorators import ajax_request
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.ticket.forms import MainTicketForm
from apps.ticket.models import Ticket


@ajax_request
def ticket_form(request):
    if request.method == "POST":
        form = MainTicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            return {
                'success': True
            }
    return {
        'success': False
    }


class TicketCreateView(CreateView):
    model = Ticket
    fields = ['name', 'phone', 'email']
    success_url = reverse_lazy('website:ok')
    template_name = 'index.html'
