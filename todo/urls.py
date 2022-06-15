from django.contrib import admin
from django.urls import path, include, re_path
from graphene_django.views import GraphQLView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as view
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet, ToDoCustomDjangoFilterViewSet, \
    ProjectCustomDjangoFilterViewSet, ProjectLimitOffsetPaginatonViewSet, ToDoLimitOffsetPaginatonViewSet
from users import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

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

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', view.obtain_auth_token),
    path('api/users/0.1', include('users.urls', namespace='0.1')),
    path('api/users/0.2', include('users.urls', namespace='0.2')),
    #generic
    path('user/generic/list/', views.UserListAPIView.as_view()),
    path('user/generic/retrieve/<int:pk>/', views.UserRetrieveAPIView.as_view()),
    path('user/generic/update/<int:pk>/', views.UserUpdateAPIView.as_view()),
    #filter
    path('filters/', include(filter_router.urls)),
    #pagination
    path('pagination/', include(pagination_router.urls)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path("graphql/", GraphQLView.as_view(graphiql=True)),
]
