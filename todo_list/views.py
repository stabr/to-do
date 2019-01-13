# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import Task
from . forms import TaskForm


# Create your views here.
def home(request):
    all_items = Task.objects.all
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to the list.'))
    return render(request, 'home.html', {'all_items': all_items})


def delete(request, list_id):
    # item = Task.objects.get(pk=list_id)
    item = get_object_or_404(Task, pk=list_id)
    item.delete()
    messages.success(request, ('Item Has Been Deleted.'))
    return redirect('todo_list:home')


def cross_off(request, list_id):
    item = get_object_or_404(Task, pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo_list:home')


def uncross(request, list_id):
    item = get_object_or_404(Task, pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo_list:home')


def edit(request, list_id):
    item = get_object_or_404(Task, pk=list_id)
    if request.method == 'POST':
        form = TaskForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been Edited.'))
            return redirect('todo_list:home')
        else:
            messages.success(request, ('Item has been Edited.'))
    return render(request, 'edit.html', {'item': item})
