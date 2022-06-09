import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from todoapp.models import Project
from todoapp.views import ProjectViewSet


class TestProjectViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()

        request = factory.post('/api/projects/', {'name': 'Work', 'link': 'test', 'users': 'Faith'}, format='json')
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # этот тест провалился :(
    def test_create_admin(self):
        factory = APIRequestFactory()

        request = factory.post('/api/projects/', {'name': 'Work', 'link': 'test', 'users': 'Faith'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        force_authenticate(request, admin)
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestProjectClientViewSet(APIClient):
    def test_get_detail(self):
        project = mixer.blend(Project)
        client = APIClient()

        response = client.get(f'/api/projects/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        project = mixer.blend(Project)
        client = APIClient()

        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/projects/{project.id}/', {'name': 'Work', 'link': 'test', 'users': 'Faith'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'Work')
        self.assertEqual(project.link, 'test')
        self.assertEqual(project.users, 'Faith')
        client.logout()


class TestToDotViewSet(APITestCase):
    def test_get_list(self):
        response = self.client.get('/api/todo/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
