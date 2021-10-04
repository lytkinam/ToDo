from rest_framework.viewsets import ModelViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer, ToDoSetSerializer
from django.shortcuts import render


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ToDoViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

class ToDoSetViewSet(ModelViewSet):
    serializer_class = ToDoSetSerializer
    queryset = ToDo.objects.all()


# Create your views here.
