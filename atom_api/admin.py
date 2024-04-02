from django.contrib import admin
from .models import Nominees, Nominations, Criteria, Users, Divisions, Roles, Requests, NominationTypes, Organizations, RequestsOfNominees, RequestTypes, CriterionResponse

admin.site.register(Nominees)
admin.site.register(Nominations)
admin.site.register(Criteria)
admin.site.register(Users)
admin.site.register(Divisions)
admin.site.register(Roles)
admin.site.register(Requests)
admin.site.register(NominationTypes)
admin.site.register(Organizations)
admin.site.register(RequestsOfNominees)
admin.site.register(RequestTypes)
admin.site.register(CriterionResponse)
# Register your models here.
