# Generated by Django 2.0.5 on 2018-06-03 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0014_auto_20180602_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='close_date',
            field=models.DateField(blank=True, default=datetime.date(2018, 6, 8)),
        ),
    ]