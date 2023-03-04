from django.db import models
from datetime import datetime
# Create your models here.


class Mail(models.Model):
    mail = models.CharField('Почта', max_length=100)
    message = models.TextField('Сообщение')
    checkbox = models.BooleanField('Отложенная отправка')
    date = models.DateTimeField('Дата отправки сообщения', blank=True, default=datetime.now())

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'Почта'
