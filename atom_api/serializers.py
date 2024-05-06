from rest_framework import serializers
from .models import Criteria, Employees, Nominations, Users, Requests


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ["login", "password", "role"]


class RequestSerializer(serializers.ModelSerializer):
    division = serializers.CharField(source="organization.division")
    nomination_name = serializers.CharField(source="nomination.name")

    class Meta:
        model = Requests
        fields = [
            "id",
            "is_team_type",
            "project_team_name",
            "division",
            "organization",
            "nomination_name",
            "status",
            "editor",
            "creator",
        ]


class EmployeesSerializer(serializers.ModelSerializer):
    division = serializers.CharField(source="organization.division")

    class Meta:
        model = Employees
        fields = [
            "last_name",
            "first_name",
            "patronymic",
            "position",
            "division",
            "organization",
            "subdivision",
        ]


class NominationsSerializer(serializers.ModelSerializer):
    management_company = serializers.SerializerMethodField()

    def get_management_company(self, obj):
        if obj.division:
            return obj.division.management_company
        return None

    class Meta:
        model = Nominations
        fields = [
            "is_team_type",
            "name",
            "type",
            "division",
            "management_company",
            "editor",
            "creator",
        ]


class CriteriaSerializer(serializers.ModelSerializer):
    nomination_name = serializers.CharField(source="nomination.name")
    nomination_type = serializers.CharField(source="nomination.type")

    class Meta:
        model = Criteria
        fields = [
            "name",
            "nomination_name",
            "nomination_type",
            "criteria_type",
            "description",
            "editor",
            "creator",
        ]
