from django.urls import path
from .views import ToDoList, TaskDetails, CreateTask

urlpatterns = [
    path('', ToDoList.as_view(), name='todo'),
    path('task/<int:pk>', TaskDetails.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
]