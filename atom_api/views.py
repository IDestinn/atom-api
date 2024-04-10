from rest_framework import viewsets, permissions
from .models import Users, Requests
from .serializers import UserSerializer, RequestSerializer


class UsersGetAll(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class RequestMainPage(viewsets.ModelViewSet):
    queryset = Requests.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [permissions.IsAuthenticated]
