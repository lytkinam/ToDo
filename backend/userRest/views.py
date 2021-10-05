from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin

#модель User: есть возможность просмотра списка и каждого пользователя в отдельности, можно вносить изменения, нельзя удалять и создавать;
class UserViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
# Create your views here.
