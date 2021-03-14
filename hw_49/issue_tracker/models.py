from django.db import models


class Status(models.Model):
    name_of_status = models.CharField(max_length=100, null=False, blank=False, verbose_name='Статус')

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name_of_status


class Type(models.Model):
    name_of_type = models.CharField(max_length=100, null=False, blank=False, verbose_name='Тип')

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name_of_type


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
    type = models.ManyToManyField('issue_tracker.Type',
                                  related_name='tasks',
                                  db_table='task_types'
                                  )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
