from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    completed = models.BooleanField(default=False, verbose_name='Concluído')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')  # Relacionamento com o usuário

    class Meta:
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'

    def __str__(self):
        return self.title
# Create your models here.
