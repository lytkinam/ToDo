from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ToDoViewSet, ToDoSetViewSet


class toDoRouter(DefaultRouter):
      def __init__(self):
          super().__init__()
          self.register('project', ProjectViewSet)
          self.register('todo', ToDoViewSet, 'todo')
          self.register('todo_set', ToDoSetViewSet, 'todo_set')
