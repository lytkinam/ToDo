from django.db import models
from userRest.models import User

class Project(models.Model):
    title = models.CharField(max_length=256)
    url_repo = models.CharField(max_length=256)
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.title

class ToDo(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE)
    text = models.CharField(max_length=256)
    date_create = models.DateTimeField()
    date_update = models.DateTimeField()
    user_create = models.ForeignKey(User, on_delete = models.CASCADE, related_name='todo')
    is_active = models.BooleanField()

    def __str__(self):
        return f'{self.text} ( {self.project.title})'

