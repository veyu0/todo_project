from rest_framework import status, viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import ProjectFilter, ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectSerializer, ToDoSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class BookViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ProjectSerializer


class ToDoModelViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = ToDoSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        queryset = get_object_or_404(ToDo, pk=pk)
        queryset.is_active = False
        queryset.save()
        content = {'Статус изменен на неактивный'}
        return Response(content, status=200)


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
