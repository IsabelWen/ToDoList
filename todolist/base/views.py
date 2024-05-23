# Django imports
from django.forms.models import BaseModelForm
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

# Django imports for authentication
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Model import
from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('todo')
    
class RegisterView(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo')

    # Function to login user when signed up
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)
    
    # Function to redirect authenticated user to todo-list
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo')
        return super(RegisterView, self).get(*args, **kwargs)

class ToDoList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'base/todolist.html'

    # Function to only show user his own tasks
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        # Filter tasks by search input
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains=search_input)
        context['search_input'] = search_input
        
        return context

class TaskDetails(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

# Create a custom widget for date field
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'complete']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date', 'class' : 'date-field'}),
        }

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo')

    # Add task only to the currents user todo-list
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('todo')

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/delete_task.html'
    success_url = reverse_lazy('todo')