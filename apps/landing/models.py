# coding=utf-8
from django.db import models

from core.base_model import SortableModel

__author__ = 'alexy'


class Setup(models.Model):
    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'

    def __unicode__(self):
        return u'Настройки сайта'

    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256, blank=True)
    phone1 = models.CharField(verbose_name=u'Дополнительный телефон', max_length=256, blank=True)
    site = models.CharField(verbose_name=u'Адрес сайта>', max_length=256, blank=True)
    site1 = models.CharField(verbose_name=u'Дополнительный адрес сайта', max_length=256, blank=True)
    address = models.TextField(verbose_name=u'Адрес', blank=True, null=True)
    email = models.EmailField(verbose_name=u'e-mail', blank=True)
    ticket_email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    video = models.TextField(verbose_name=u'HTML-код видео', blank=True, null=True)
    bp = models.FileField(verbose_name=u'Бизнес план', upload_to='franchise', blank=True, null=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)


class Block1(SortableModel):
    class Meta:
        verbose_name = u'Новая модель размещения рекламы в лифте'
        verbose_name_plural = u'Новая модель размещения рекламы в лифте'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')


class Block2(SortableModel):
    class Meta:
        verbose_name = u'Доходность третьего этапа'
        verbose_name_plural = u'Доходность третьего этапа'
        ordering = ['order', ]

    def __unicode__(self):
        return str(self.stand)

    stand = models.IntegerField(verbose_name=u'Количество стендов')
    price = models.IntegerField(verbose_name=u'Цена')


class Client(SortableModel):
    class Meta:
        verbose_name = u'Наши клиенты'
        verbose_name_plural = u'Наши клиенты'
        ordering = ['order', ]

    def __unicode__(self):
        return self.img.url

    img = models.ImageField(upload_to='franchise', verbose_name=u'Изображение')


class Block3(SortableModel):
    class Meta:
        verbose_name = u'Купив нашу франшизу вы получите'
        verbose_name_plural = u'Купив нашу франшизу вы получите'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    # icon = models.ImageField(upload_to='franchise', verbose_name=u'Иконка')


class Block4(SortableModel):
    class Meta:
        verbose_name = u'Пункт франшизы'
        verbose_name_plural = u'Пункты франшизы'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')


class Block41(SortableModel):
    class Meta:
        verbose_name = u'Комплектация франшизы'
        verbose_name_plural = u'Комплектации франшизы'
        ordering = ['order', ]

    def __unicode__(self):
        return self.name

    def item_id_list(self):
        if self.item.all():
            return [i.id for i in self.item.all()]
        else:
            return None

    name = models.CharField(verbose_name=u'Название', max_length=256)
    cost = models.PositiveIntegerField(verbose_name=u'Стоимость, руб', default=0)
    item = models.ManyToManyField(to=Block4, verbose_name=u'Что входит в состав')


class Block5(SortableModel):
    class Meta:
        verbose_name = u'Дополнительные услуги'
        verbose_name_plural = u'Дополнительные услуги'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    price = models.CharField(verbose_name=u'Стоимость', max_length=100)


class Block6(SortableModel):
    class Meta:
        verbose_name = u'Преимущества'
        verbose_name_plural = u'Преимущества'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
