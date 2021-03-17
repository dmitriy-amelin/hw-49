from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, FormView
from django.urls import reverse

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


class TaskUpdate(FormView):
    form_class = TaskForm
    template_name = 'update_view.html'

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        types = form.cleaned_data.pop('type')
        form.save()
        self.task.type.set(types)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task-view', kwargs={'pk': self.kwargs.get('pk')})

    def get_object(self):
        task = get_object_or_404(
            Task, id=self.kwargs.get('pk')
            )
        return task


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
