from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from issue_tracker.models import Type, Task, Status
from issue_tracker.forms import TaskForm, ModelChoiceField


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['tasks'] = Task.objects.all()
        return super().get_context_data(**kwargs)


class TaskView(TemplateView):

    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class TaskUpdate(View):

    task = get_object_or_404(Task, id=pk)
    type = forms.ModelChoiceField(queryset=Type.objects.all())

    if request.method == 'GET':
        get()

    def get(self, request, pk):


            form = TaskForm(initial={
                'summary': self.task.summary,
                'description': self.task.description,
                'status': self.task.status,
                'type': self.task.type,
                'created_at': self.task.created_at,
                'updated_at': self.task.updated_at
            })
            return render(request, 'update_view.html', context={'form': form, 'task': self.task})

