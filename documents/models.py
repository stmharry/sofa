# -*- coding: utf-8 -*-

from django.db import models

from fields import Paper, Book, Urgency, Secrecy, Process, ClassSerial


class Undertaker(models.Model):
    name = models.CharField(
        max_length=16,
        verbose_name=u'承辦人姓名',
    )

    class Meta:
        verbose_name = u'承辦人'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Document(models.Model):
    # RECEPTION
    reception_date = models.DateField(
        auto_now_add=True,
        verbose_name=u'收文日期',
    )
    reception_time = models.TimeField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name=u'收文時間',
    )
    reception_serial = models.CharField(
        max_length=10,
        verbose_name=u'收文號',
    )

    transmission_date = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
        verbose_name=u'發文日期',
    )
    transmitter = models.CharField(
        max_length=64,
        verbose_name=u'發文機關',
        blank=True,
    )
    transmission_serial = models.CharField(
        max_length=64,
        blank=True,
        verbose_name=u'發文字號',
    )
    paper = models.CharField(
        max_length=2,
        choices=Paper.CHOICES,
        default=Paper.DEFAULT,
        verbose_name=u'文別',
    )
    book = models.CharField(
        max_length=1,
        choices=Book.CHOICES,
        default=Book.DEFAULT,
        verbose_name=u'本別',
    )
    urgency = models.CharField(
        max_length=2,
        choices=Urgency.CHOICES,
        default=Urgency.NORMAL,
        verbose_name=u'速別',
    )
    secrecy = models.CharField(
        max_length=1,
        choices=Secrecy.CHOICES,
        default=Secrecy.DEFAULT,
        verbose_name=u'密等',
    )
    electric = models.BooleanField(
        default=False,
        verbose_name=u'電子收文',
    )
    undertaker = models.ForeignKey(
        Undertaker,
        verbose_name=u'承辦人',
    )
    summary = models.TextField(
        blank=True,
        verbose_name=u'主旨',
    )

    # CLOSURE
    process = models.CharField(
        max_length=2,
        choices=Process.CHOICES,
        default=Process.NONE,
        blank=True,
        verbose_name=u'處理情形',
    )

    closure_date = models.DateField(
        blank=True,
        null=True,
        verbose_name=u'結案日期',
    )

    class_serial = models.CharField(
        max_length=6,
        choices=ClassSerial.CHOICES,
        blank=True,
        verbose_name=u'分類號',
    )
    pages = models.IntegerField(
        blank=True,
        null=True,
        verbose_name=u'數量',
    )

    class Meta:
        verbose_name = u'公文'
        verbose_name_plural = verbose_name

    def title(self):
        return u'{} {}'.format(
            self.transmitter,
            self.get_paper_display(),
        )
    title.short_description = u'標題'
