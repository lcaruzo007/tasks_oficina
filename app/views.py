# app/views.py
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import *

# Página de Login
class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    next_page =reverse_lazy('task-list')

# Página Principal de Tarefas
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

# Detalhes da Tarefa
class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Adicionar Tarefa
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Editar Tarefa
class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

# Excluir Tarefa
class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

# Listagem de Tarefas Concluídas
class CompletedTaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'completed_task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user, completed=True)


# Página de Logout
class CustomLogoutView(LogoutView):
     next_page = reverse_lazy('login')
