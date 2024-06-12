from rest_framework import viewsets
from .models import (
    Criteria,
    Divisions,
    Employees,
    Nominations,
    Organizations,
    Users,
    Requests,
)
from .serializers import (
    CriteriaSerializer,
    DivisionsListSerializer,
    EmployeesSerializer,
    NominationsSerializer,
    OrganizationsListSerializer,
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


class DivisionList(viewsets.ModelViewSet):
    queryset = Divisions.objects.all()
    serializer_class = DivisionsListSerializer


class OrganizationList(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsListSerializer
