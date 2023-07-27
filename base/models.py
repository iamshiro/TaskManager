from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField("Задача",max_length=200)
    description = models.TextField("Описание задачи",null=True, blank=True)
    complete = models.BooleanField(default=False)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

