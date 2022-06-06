from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todoapp.views import ProjectViewSet, ToDoViewSet
from users.views import UserModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet)
router.register('project', ProjectViewSet)
router.register('todo', ToDoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
