import rest_framework.request
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, HyperlinkedRelatedField
from .models import Project, ToDo
from userRest.serializers import UserSerializer
from rest_framework.fields import empty


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class ProjectReadSerializer(HyperlinkedModelSerializer):
    users = UserSerializer(many=True)
    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance,data,**kwargs)
    class Meta:
        model = Project
        fields = '__all__'

class ToDoSerializer(ModelSerializer):
    def __init__(self, instance=None, data=empty, **kwargs):
        super().__init__(instance, data, **kwargs)
        if kwargs['context']['request'].method == 'GET' or kwargs['context']['request'].method == 'DELETE':
            self.fields.fields['project'] = ProjectReadSerializer()
            self.fields.serializer.fields['project'] = ProjectReadSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'
