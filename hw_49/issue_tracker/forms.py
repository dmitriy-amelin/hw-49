from django import forms

from issue_tracker.models import Task, Type, Status


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type', 'created_at', 'updated_at']


class ModelChoiceField(forms.ModelForm):
    model = Type
    fields = ['type']