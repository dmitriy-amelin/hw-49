from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from issue_tracker.models import Task
from issue_tracker.forms import TaskForm, TaskDeleteForm


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
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.type = form.cleaned_data.get('type')
            task.save()

            return redirect('task-view', pk=task.id)
        return render(request, 'update_view.html', context={'form': form, 'task': task})


class TaskAdd(View):

    def get(self, request):
        form = TaskForm()
        return render(request, 'task_add.html', context={'form': form})

    def post(self, request):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(
                summary=form.cleaned_data.get('summary'),
                description=form.cleaned_data.get('description'),
                status=form.cleaned_data.get('status'),
                type=form.cleaned_data.get('type')
            )
            return redirect('task-view', pk=task.id)
        return render(request, 'task_add.html', context={'form': form})


class TaskDelete(View):

    def get(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = TaskDeleteForm()
        return render(request, 'task_delete.html', context={'task': task, 'form': form})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = TaskDeleteForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data['title'] != task.summary:
                form.errors['title'] = ['Название задачи не совпадает']
                return render(request, 'task_delete.html', context={'task': task, 'form': form})
            task.delete()
            return redirect('task-list')
        return render(request, 'task_delete.html', context={'task': task, 'form': form})
