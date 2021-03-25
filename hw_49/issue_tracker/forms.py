from django import forms
from django.forms import widgets

from issue_tracker.models import Task, Type, Status


class TaskForm(forms.ModelForm):

    type = forms.ModelMultipleChoiceField(required=False, label='Типы',
                                          queryset=Type.objects.all(),
                                          widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')


class TaskDeleteForm(forms.Form):
    title = forms.CharField(max_length=120, required=True, label='Введите название задачи, чтобы удалить её')


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')