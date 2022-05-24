from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from todoapp.views import ProjectModelViewSet, ToDoModelViewSet, ToDoCustomDjangoFilterViewSet, \
    ProjectCustomDjangoFilterViewSet, ProjectLimitOffsetPaginatonViewSet, ToDoLimitOffsetPaginatonViewSet
from users import views

router = DefaultRouter()
#router.register('user', UserModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

filter_router = DefaultRouter()
filter_router.register('project-custom', ProjectCustomDjangoFilterViewSet)
filter_router.register('todo-custom', ToDoCustomDjangoFilterViewSet)

pagination_router = DefaultRouter()
pagination_router.register('project-limitoffset', ProjectLimitOffsetPaginatonViewSet)
pagination_router.register('todo-limitoffset', ToDoLimitOffsetPaginatonViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    #generic
    path('user/generic/list/', views.UserListAPIView.as_view()),
    path('user/generic/retrieve/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('user/generic/update/<int:pk>/', views.UserUpdateAPIView.as_view()),
    #filter
    path('filters/', include(filter_router.urls)),
    #pagination
    path('pagination/', include(pagination_router.urls))
]
