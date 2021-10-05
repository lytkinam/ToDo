from django_filters.rest_framework import FilterSet, CharFilter, NumberFilter, DateRangeFilter, DateFromToRangeFilter
from .models import Project, ToDo

class ProjectFilter(FilterSet):
    title = CharFilter(field_name='title', lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']

class ToDoFilterSet(FilterSet):
    project = NumberFilter(field_name='project')
    date_create = DateFromToRangeFilter(field_name='date_create')
    date_create_range = DateRangeFilter(field_name='date_create')

    class Meta:
        model = ToDo
        fields = ['project', 'date_create']
