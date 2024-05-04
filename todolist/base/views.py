from django.shortcuts import render
from django.http import HttpResponse

def todoList(request):
    return HttpResponse('To-Do List')