from django.urls import path
from . import views

urlpatterns = [path("users/", views.UsersGetAll.as_view(), name="users-get")]
