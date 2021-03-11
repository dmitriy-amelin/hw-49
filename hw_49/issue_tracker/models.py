from django.db import models


class Status(models.Model):
    name_of_status = models.CharField(max_length=100, null=False, blank=False, verbose_name='Статус')


class Type(models.Model):
    name_of_type = models.CharField(max_length=100, null=False, blank=False, verbose_name='Тип')


class Task(models.Model):
    summary = models.TextField(verbose_name='Краткое описание')
    description = models.TextField(blank=True, verbose_name='Полное описание')
    status = models.ForeignKey('issue_tracker.Status',
                               on_delete=models.CASCADE,
                               related_name='status',
                               verbose_name='Статус',
                               null=False,
                               blank=False
                               )
    type = models.ForeignKey('issue_tracker.Type',
                             on_delete=models.CASCADE,
                             related_name='type',
                             verbose_name='Тип',
                             null=False,
                             blank=False
                             )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
