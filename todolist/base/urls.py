from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import ToDoList, TaskDetails, CreateTask, EditTask, DeleteTask, CustomLoginView, RegisterView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ToDoList.as_view(), name='todo'),
    path('task/<int:pk>', TaskDetails.as_view(), name='task'),
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('edit-task/<int:pk>/', EditTask.as_view(), name='edit-task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
]