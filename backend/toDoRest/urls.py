from rest_framework.routers import DefaultRouter
from .views import UserViewSet


class ToDoRouter(DefaultRouter):
      def __init__(self):
          super().__init__()
          self.register('user',UserViewSet)
