# coding=utf-8
from __future__ import unicode_literals

from annoying.decorators import ajax_request

from apps.ticket.forms import MainTicketForm


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
