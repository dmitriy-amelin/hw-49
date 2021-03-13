from django import forms
from django.forms import widgets

from issue_tracker.models import Task, Type, Status


class TaskForm(forms.Form):
    summary = forms.CharField(max_length=200, required=True, label='Summary')
    description = forms.CharField(max_length=3000, label='Description', required=False, widget=widgets.Textarea)
    status = forms.ModelChoiceField(queryset=Status.objects.all())
    type = forms.ModelChoiceField(queryset=Type.objects.all())


class TaskDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')
