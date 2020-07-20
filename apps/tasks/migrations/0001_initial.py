# -*- coding: utf-8 -*-
# Generated by Django 1.11.22 on 2020-03-15 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskMsg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('database', models.CharField(help_text='数据库名称', max_length=30, verbose_name='数据库名称')),
                ('user', models.CharField(help_text='用户', max_length=30, verbose_name='用户')),
                ('port', models.IntegerField(help_text='端口', max_length=4, verbose_name='端口')),
                ('password', models.CharField(help_text='数据库密码', max_length=30, verbose_name='数据库密码')),
                ('host', models.CharField(help_text='地址', max_length=30, verbose_name='地址')),
                ('charset', models.CharField(help_text='编码', max_length=30, verbose_name='编码')),
            ],
            options={
                'verbose_name': '开启任务信息',
                'verbose_name_plural': '开启任务信息',
            },
        ),
    ]
