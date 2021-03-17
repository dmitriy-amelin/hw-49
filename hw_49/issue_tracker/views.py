from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView

from issue_tracker.models import Task
from issue_tracker.forms import TaskForm, TaskDeleteForm
from issue_tracker.base_views import CustomFormView


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
            'type': task.type.all(),
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
        })
        return render(request, 'update_view.html', context={'form': form, 'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        form = TaskForm(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.save()
            task.type.set(types)
            return redirect('task-view', pk=task.id)
        return render(request, 'update_view.html', context={'form': form, 'task': task})


class TaskAdd(CustomFormView):
    template_name = 'task_add.html'
    form_class = TaskForm
    redirect_url = 'task-list'

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        task = Task()
        for key, value in form.cleaned_data.items():
            setattr(task, key, value)

        task.save()
        task.type.set(types)

        return super().form_valid(form)


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
