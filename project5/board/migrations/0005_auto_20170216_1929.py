# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0004_auto_20170216_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='category_set',
            field=models.CharField(choices=[('c', '가슴'), ('s', '어깨'), ('b', '등'), ('l', '하체'), ('p', '복근'), ('a', '유산소')], default='a', max_length=1),
        ),
    ]