# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0017_auto_20170416_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(allow_unicode=True)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('instruction', models.TextField()),
                ('direction', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
