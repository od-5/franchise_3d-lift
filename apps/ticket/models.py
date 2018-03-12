# coding=utf-8
from django.conf import settings
from django.core.mail import send_mail
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.landing.models import Setup
from core.base_model import Created

__author__ = 'alexey'


class Ticket(Created):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'

    def __unicode__(self):
        return self.name

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Выполнено'),
        (3, u'Отмена'),
    )

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256)
    email = models.EmailField(verbose_name=u'e-mail', max_length=60, )
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE,
                                              default=0, blank=True, null=True)

    def send_notify_mail(self):
        email = False
        setup = Setup.objects.all().first()
        if setup and setup.ticket_email:
            email = setup.ticket_email
        if email:
            theme = u'Франшиза 3d-lift.ru - Заявка с сайта'
            message = u'Имя: %s\nТелефон: %s\nEmail: %s\n' % (self.name, self.phone, self.email)
            send_mail(
                theme,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [email, ]
            )
        return False


@receiver(post_save, sender=Ticket)
def new_mail(sender, created, **kwargs):
    ticket = kwargs['instance']
    if created:
        print 'send mail'
        ticket.send_notify_mail()
