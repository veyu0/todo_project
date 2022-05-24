from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.renderers import JSONRenderer
# from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserModelSerializer


# class UserModelViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserModelSerializer
#
class UserListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
