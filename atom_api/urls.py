from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.UsersGet.as_view(), name="users-get")
]
