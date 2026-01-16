from django.urls import path
from django.views.generic import ListView, UpdateView, DeleteView

from tasks.models import Task
from tasks.forms.task_form import TaskEditForm


urlpatterns = [
    # Główna strona
    path('', ListView.as_view(model=Task), name='main-page'),
    
    # Strona edycji zadania
    path('task-edit/<int:pk>/', UpdateView.as_view(
        model=Task,
        form_class=TaskEditForm,
        success_url='/'
        ), name='task-edit'),
    
    # Strona dla usunięcia zadania
    path('task-delete/<int:pk>/', DeleteView.as_view(
        model=Task,
        success_url='/'
        ), name='task-delete')
]
