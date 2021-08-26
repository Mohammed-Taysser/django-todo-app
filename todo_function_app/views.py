"""
temp doc
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.utils.translation import gettext as _
from . import models, forms
# Create your views here.


def home(request):
    ''' temp doc '''
    return render(request, 'todo_function/pages/home.html', {
        'title': _('home'),
        'db_objects_todo': models.Task.objects.all().order_by('-created_data'),
    })


def add_task(request):
    ''' temp doc '''
    if request.POST:
        form = forms.AddTask(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('todo_function:home')

    return render(request, 'todo_function/pages/add.html', {
        'title': _('add new task'),
    })


def delete_task(request, task_id):
    ''' temp doc '''
    current_todo = get_object_or_404(models.Task, pk=task_id)
    current_todo.delete()
    return redirect('todo_function:home')


def update_task(request, task_id):
    ''' temp doc '''
    current_todo = get_object_or_404(models.Task, pk=task_id)
    if request.POST:
        form = forms.UpdateTask(request.POST, request.FILES, instance=current_todo)
        if form.is_valid:
            form.save()
            return redirect('todo_function:home')

    return render(request, 'todo_function/pages/update.html', {
        'title': _('update') + ' | ' + current_todo.title,
        'current_todo': current_todo,
    })


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
