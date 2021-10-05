from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ToDoViewSet


class toDoRouter():
    @staticmethod
    def urls():
        router = DefaultRouter()
        router.register('project', ProjectViewSet)
        router.register('todo', ToDoViewSet, 'todo')
        return router.urls

    @staticmethod
    def api():
        return 'api/'