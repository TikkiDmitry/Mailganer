# Generated by Django 4.1.4 on 2023-02-26 17:41

from django.db import migrations, models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mail',
            name='date',
            field=models.DateTimeField(verbose_name='Дата отправки сообщения', blank=True, default=datetime.now()),
            preserve_default=False,
        ),
    ]