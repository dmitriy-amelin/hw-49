from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from issue_tracker.models import Type, Task, Status
from issue_tracker.forms import TaskForm


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

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type,
        })
        return render(request, 'update_view.html', context={'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)

        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = request.POST.get('summary')
            task.description = request.POST.get('description')
            task.status = request.POST.get('status')
            task.type = request.POST.get('type')
            task.save()

            return redirect('task-view', pk=task.id)

        return render(request, 'update_view.html', context={'form': form, 'task': task})
