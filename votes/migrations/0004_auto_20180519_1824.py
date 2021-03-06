# Generated by Django 2.0.5 on 2018-05-19 16:24

from django.db import migrations, models
import votes.models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0003_auto_20180519_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproposalphasevote',
            name='salt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userproposalphasevote',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='userproposalphasevote',
            name='unique_id',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
