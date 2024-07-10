# app/forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Task

# Formulário de login personalizado
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome de usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Senha'}))

# Formulário para adicionar ou editar tarefas
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# Formulário para marcar uma tarefa como concluída
class CompleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['completed']
        widgets = {
            'completed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }