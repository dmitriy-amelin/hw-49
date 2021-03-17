from django.core.validators import MinLengthValidator
from django.db import models


class Status(models.Model):
    name_of_status = models.CharField(max_length=100, null=False, blank=False, verbose_name='Статус',
                                      validators=(MinLengthValidator(2),)
                                      )

    class Meta:
        db_table = 'status'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name_of_status


class Type(models.Model):
    name_of_type = models.CharField(max_length=100, null=False, blank=False, verbose_name='Тип',
                                    validators=(MinLengthValidator(2),)
                                    )

    class Meta:
        db_table = 'type'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name_of_type


class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name='Краткое описание', validators=(MinLengthValidator(3),))
    description = models.TextField(max_length=3000, blank=True, verbose_name='Полное описание',
                                   validators=(MinLengthValidator(10),))
    status = models.ForeignKey('issue_tracker.Status',
                               on_delete=models.PROTECT,
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
