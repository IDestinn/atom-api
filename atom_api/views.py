from rest_framework import viewsets
from .models import Criteria, Employees, Nominations, Users, Requests
from .serializers import (
    CriteriaSerializer,
    EmployeesSerializer,
    NominationsSerializer,
    UserSerializer,
    RequestSerializer,
)


class UsersGetAll(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class RequestMainPage(viewsets.ModelViewSet):
    queryset = Requests.objects.all().order_by("id")
    serializer_class = RequestSerializer


class EmployeesView(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class NominationsView(viewsets.ModelViewSet):
    queryset = Nominations.objects.all().order_by("id")
    serializer_class = NominationsSerializer


class CriteriaView(viewsets.ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaSerializer
