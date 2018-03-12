# coding=utf-8
from django.core.mail import send_mail
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.landing.models import Setup
from core.base_model import Created

__author__ = 'alexy'


class MailTicket(Created):
    class Meta:
        verbose_name = u'Оставленный e-mail'
        verbose_name_plural = u'Оставленные e-mail'

    phone = models.CharField(verbose_name=u'Телефон', max_length=100)
    email = models.EmailField(verbose_name=u'E-mail', max_length=100)

    def __unicode__(self):
        return self.email

    def send_notyfy_email(self):
        email = False
        setup = Setup.objects.all().first()
        if setup and setup.ticket_email:
            email = setup.ticket_email
        if email:
            message = u'email: %s, телефон: %s' % (self.email, self.phone)
            # print settings.EMAIL_HOST_USER
            send_mail(
                u'franchise.3d-lift.ru - оставлен email',
                message,
                settings.EMAIL_HOST_USER,
                [email, ]
            )
        return False


@receiver(post_save, sender=MailTicket)
def new_download(sender, created, **kwargs):
    mailticket = kwargs['instance']
    if created:
        mailticket.send_notyfy_email()
