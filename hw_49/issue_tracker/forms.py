from django import forms
from django.forms import widgets

from issue_tracker.models import Task, Type, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Краткое описание')
    description = forms.CharField(max_length=3000, label='Полное описание', required=False, widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelMultipleChoiceField(required=False, label='Типы',
                                          queryset=Type.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)


class TaskDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')
