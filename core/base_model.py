# coding=utf-8
from __future__ import unicode_literals

from django.db import models


class SortableModel(models.Model):
    order = models.PositiveIntegerField(verbose_name='Сортировка', default=1)

    class Meta:
        abstract = True


class Created(models.Model):
    created = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created', ]

    @property
    def created_time(self):
        return self.created.strftime('%d.%m.%Y - %H:%M')


