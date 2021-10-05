from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer
from rest_framework.pagination import LimitOffsetPagination
from .filters import ProjectFilter, ToDoFilterSet
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin
from djangorestframework_camel_case.render import CamelCaseJSONRenderer, CamelCaseBrowsableAPIRenderer
from django.shortcuts import render

class ProjectPagination(LimitOffsetPagination):
    default_limit = 10

class ToDoPagination(LimitOffsetPagination):
    default_limit = 1

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectPagination
    filterset_class = ProjectFilter

class ToDoViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoPagination

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


# Create your views here.
