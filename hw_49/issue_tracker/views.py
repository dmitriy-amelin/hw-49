from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from issue_tracker.models import Type, Task, Status
# from issue_tracker.forms import TaskForm, TaskDeleteForm


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)