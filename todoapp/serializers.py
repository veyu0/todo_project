from rest_framework.serializers import HyperlinkedModelSerializer
from todoapp.models import Project, ToDo
from users.serializers import UserModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(HyperlinkedModelSerializer):
    users = UserModelSerializer()
    project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'