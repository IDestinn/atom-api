from rest_framework import serializers
from .models import Users, Requests


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
        ]
