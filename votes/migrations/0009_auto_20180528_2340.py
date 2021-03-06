# Generated by Django 2.0.5 on 2018-05-28 21:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0008_auto_20180523_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalphasevote',
            name='user_pw',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='proposalphasevote',
            name='identifier',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='usercommentvote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userproposalphasevote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
