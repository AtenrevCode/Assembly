# Generated by Django 2.0.5 on 2018-05-22 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0007_auto_20180523_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='nest_comment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='votes.Comment'),
        ),
    ]
