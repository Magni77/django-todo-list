from django.shortcuts import render, get_object_or_404
from .models import TaskModel
from .taskForm import TaskForm
from django.contrib import messages
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import datetime


def task_list(request):
    qs = TaskModel.objects.all()#.filter(time__lte=datetime.datetime.now())
    late = qs.filter(time__lte=datetime.datetime.now())

    context = {
        "objects_list": qs,
        "old_tasks": late
    }
    template = 'task_list_view.html'
    return render(request, template, context)


def task_details(request, id):
    obj = get_object_or_404(TaskModel, id=id)
    context = {
        "object": obj
    }
    template = 'task_detail_view.html'
    return render(request, template, context)

@login_required
def task_create(request):
    form = TaskForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Created new task')
        context = {
            'form': TaskForm()
        }

    template = 'create_task_view.html'
    return render(request, template, context)

@login_required
def task_edit(request, id):
    obj = get_object_or_404(TaskModel, id=id)
    form = TaskForm(request.POST or None, instance= obj)
    context = {
        'form': form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        messages.success(request, 'Edited!')
        return HttpResponseRedirect("/tasks/{num}".format(num=obj.id))

    template = 'create_task_view.html'
    return render(request, template, context)

@login_required
def delete_task(request, id):
    obj = get_object_or_404(TaskModel, id=id)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, 'Deleted!')
        return HttpResponseRedirect('/tasks/')
    context = {
        'object': obj
    }
    template = 'delete_view.html'
    return render(request, template, context)

@login_required
def mark_as_completed(request, id):
    obj = get_object_or_404(TaskModel, id=id)
    if request.method == 'GET':
        obj.completed = True
        obj.save()
        messages.success(request, 'Completed!')
        return HttpResponseRedirect("/tasks/{num}".format(num=obj.id))
