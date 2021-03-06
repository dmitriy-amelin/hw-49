# Generated by Django 3.1.6 on 2021-03-17 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0004_auto_20210317_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=3000, verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.TextField(max_length=200, verbose_name='Краткое описание'),
        ),
    ]
