# Generated by Django 3.1.6 on 2021-03-17 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0005_auto_20210317_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=200, verbose_name='Краткое описание'),
        ),
    ]
