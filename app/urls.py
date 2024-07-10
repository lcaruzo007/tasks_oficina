# app/urls.py

from django.urls import path
from .views import *
 # Defina um namespace para suas URLs

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),  # URL para o logout
    path('', task_list, name='task-list'),
    path('task/<int:pk>/', TaskDetailView.as_view(), name='detalhes'),
    path('task/add/', TaskCreateView.as_view(), name='criar'),
    path('task/<int:pk>/edit/', TaskUpdateView.as_view(), name='editar'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='deletar'),
    path('completed/', CompletedTaskListView.as_view(), name='completar'),
]
