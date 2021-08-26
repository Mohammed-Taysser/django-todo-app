"""
temp doc
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from . import models, forms
from django.views.generic import ListView, FormView, DeleteView, UpdateView
# Create your views here.


class Home(ListView):
    """docstring for Home."""

    template_name = 'todo_CBV/pages/home.html'
    model = models.Task
    context_object_name = 'db_objects_todo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'home'
        return context


class AddTask(FormView):
    """docstring for AddTask."""

    form_class = forms.AddTask
    success_url = 'todo_CBV:home'
    template_name = 'todo_CBV/pages/add.html'

    def form_valid(self, form):
        if form.is_valid:
            form.save()
            return redirect('todo_CBV:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'add new task'
        return context


class DeleteTask(DeleteView):
    """docstring for DeleteTask."""

    model = models.Task
    success_url = '/v2/'


def update_task(request, task_id):
    ''' temp doc '''
    current_todo = get_object_or_404(models.Task, pk=task_id)
    if request.POST:
        form = forms.UpdateTask(request.POST, request.FILES, instance=current_todo)
        if form.is_valid:
            form.save()
            return redirect('todo_CBV:home')

    return render(request, 'todo/pages/update.html', {
        'title': 'update | ' + current_todo.title,
        'current_todo': current_todo,
    })


class UpdateTask(UpdateView):
    """docstring for UpdateTask."""

    model = models.Task
    fields = ['title', 'description', 'is_complete', 'image']
    success_url = '/v2/'
    template_name = 'todo_CBV/pages/update.html'


def update_task_completeness(request, task_id):
    ''' temp doc '''
    current_todo = get_object_or_404(models.Task, pk=task_id)
    data = {'is_complete': False}
    if current_todo.is_complete:
        current_todo.is_complete = False
    else:
        current_todo.is_complete = True
        data['is_complete'] = True
    current_todo.save()

    return JsonResponse(data)
