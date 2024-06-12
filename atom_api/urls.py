from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"users", views.UsersGetAll)
router.register(r"requests", views.RequestMainPage)
router.register(r"employees", views.EmployeesView)
router.register(r"nominations", views.NominationsView)
router.register(r"criteria", views.CriteriaView)
router.register(r"divisions", views.DivisionList)
router.register(r"organizations", views.OrganizationList)


urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
