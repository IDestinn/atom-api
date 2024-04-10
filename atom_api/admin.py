from django.contrib import admin
from .models import (
    Employees,
    Nominations,
    Criteria,
    Users,
    Divisions,
    Roles,
    Requests,
    NominationTypes,
    Organizations,
    RequestsOfEmployees,
    CriterionResponse,
    RequestStatuses,
)

admin.site.register(Employees)
admin.site.register(Nominations)
admin.site.register(Criteria)
admin.site.register(Users)
admin.site.register(Divisions)
admin.site.register(Roles)
admin.site.register(Requests)
admin.site.register(NominationTypes)
admin.site.register(Organizations)
admin.site.register(RequestsOfEmployees)
admin.site.register(CriterionResponse)
admin.site.register(RequestStatuses)
# Register your models here.
