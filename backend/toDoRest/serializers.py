from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Project, ToDo
from userRest.serializers import UserSerializer


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectReadSerializer(HyperlinkedModelSerializer):
    users = UserSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'

class ToDoSerializer(ModelSerializer):
    project = ProjectReadSerializer()
#    user_create = HyperlinkedRelatedField(view_name='user_create-detail', read_only=True)

    class Meta:
        model = ToDo
        fields = '__all__'


class ToDoSetSerializer(ModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'