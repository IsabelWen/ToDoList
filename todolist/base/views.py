# Django imports
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Model import
from .models import Task

class ToDoList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/todolist.html'

class TaskDetails(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class CreateTask(CreateView):
    model = Task
    fields  = '__all__'
    success_url = reverse_lazy('todo')

class EditTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('todo')

class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/delete_task.html'
    success_url = reverse_lazy('todo')