from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import ProjectFilter, ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectSerializer, ToDoSerializer


# class ProjectViewSet(ModelViewSet):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#
#
# class ToDoViewSet(ModelViewSet):
#     queryset = ToDo.objects.all()
#     serializer_class = ToDoSerializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ProjectSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ToDoSerializer


class ProjectCustomDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filterset_class = ProjectFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination


class ToDoCustomDjangoFilterViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    filterset_class = ToDoFilter


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ToDoLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    pagination_class = ToDoLimitOffsetPagination
