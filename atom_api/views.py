from rest_framework import viewsets
from .models import Users, Requests
from .serializers import UserSerializer, RequestSerializer


class UsersGetAll(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class RequestMainPage(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestSerializer
