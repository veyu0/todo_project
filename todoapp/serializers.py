from rest_framework import serializers
from todoapp.models import Project, ToDo
#from users.serializers import UserModelSerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    project = ProjectSerializer()

    class Meta:
        model = ToDo
        fields = '__all__'