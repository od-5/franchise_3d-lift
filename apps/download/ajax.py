# coding: utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from apps.landing.models import Setup
from .forms import MailTicketTicketForm


__author__ = 'alexy'


@ajax_request
@csrf_exempt
def bp_download(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            form = MailTicketTicketForm(data=request.POST)
            if form.is_valid():
                form.save()
                setup = Setup.objects.first()
                if setup and setup.bp:
                    file = Setup.objects.first().bp.url
                else:
                    file = u'/static/art-lift.pdf'
                return {
                    'success': True,
                    'file': file
                }
    else:
        return {
            'error': True
        }
