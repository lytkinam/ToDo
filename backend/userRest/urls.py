from rest_framework.routers import DefaultRouter
from .views import UserViewSet


class userRouter():
      @staticmethod
      def urls():
          router = DefaultRouter()
          router.register('user', UserViewSet)
          return router.urls

      @staticmethod
      def api():
          return 'api-user/'


