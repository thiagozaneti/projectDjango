from django.db import models

# Create your models here.


class Todo(models.Model):
    titulo = models.CharField(
        verbose_name="titulo", max_length=50, null=False, blank=False
    )
    created_at = models.DateTimeField(
        verbose_name="criado a", auto_now_add=True, null=False, blank=False
    )  ##horario automatico
    deadline = models.DateTimeField(
        verbose_name=" data de inicio ", null=False, blank=False
    )
    finished_at = models.DateTimeField(verbose_name="data de conclusão", null=True)
