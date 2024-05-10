from django.urls import path
from .views import ToDoList, TaskDetails, CreateTask, EditTask, DeleteTask

urlpatterns = [
    path('', ToDoList.as_view(), name='todo'),
    path('task/<int:pk>', TaskDetails.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
]