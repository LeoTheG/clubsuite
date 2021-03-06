# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-04 19:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suite', '0027_auto_20170303_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='cid',
        ),
        migrations.AddField(
            model_name='division',
            name='cid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suite.Club'),
        ),
        migrations.AddField(
            model_name='event',
            name='did',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suite.Division'),
        ),
        migrations.AlterField(
            model_name='budget',
            name='did',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='suite.Division'),
        ),
        migrations.AlterField(
            model_name='club',
            name='image',
            field=models.ImageField(default='static/media/default.jpg', upload_to=''),
        ),
    ]
