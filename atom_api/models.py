from django.db import models


class Criteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    nomination = models.ForeignKey(
        "Nominations", models.DO_NOTHING, db_column="nomination"
    )
    criteria_type = models.CharField(max_length=50)
    description = models.TextField()
    edit_time = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.nomination} №{self.criteria_type}"

    class Meta:
        db_table = "criteria"


class CriterionResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    request = models.ForeignKey("Requests", models.DO_NOTHING)
    criteria = models.ForeignKey(Criteria, models.DO_NOTHING)
    answer = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.request} {self.criteria}"

    class Meta:
        db_table = "criterion_response"


class Divisions(models.Model):
    name = models.CharField(primary_key=True, max_length=256)
    management_company = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "divisions"


class Employees(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_login = models.ForeignKey(
        "Users", models.DO_NOTHING, db_column="user_login", blank=True, null=True
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=100)
    organization = models.ForeignKey(
        "Organizations", models.DO_NOTHING, db_column="organization"
    )
    subdivision = models.CharField(max_length=100, blank=True, null=True)
    experience = models.CharField(max_length=20)
    is_experience_in_atom_above_year = models.BooleanField()
    no_offenses = models.BooleanField()
    no_discipline_offensives = models.BooleanField()
    photo = models.BinaryField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        if self.patronymic:
            return f"{self.last_name} {self.first_name[0]}. {self.patronymic[0]}. {self.position}"
        return f"{self.last_name} {self.first_name} {self.position}"

    class Meta:
        db_table = "employees"


class NominationTypes(models.Model):
    name = models.CharField(primary_key=True, max_length=256)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "nomination_types"


class Nominations(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey(NominationTypes, models.DO_NOTHING, db_column="type")
    name = models.CharField(unique=True, max_length=256)
    is_team_type = models.BooleanField()
    division = models.ForeignKey(
        Divisions, models.DO_NOTHING, db_column="division", blank=True, null=True
    )
    edit_time = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "nominations"


class Organizations(models.Model):
    name = models.CharField(primary_key=True, max_length=256)
    division = models.ForeignKey(Divisions, models.DO_NOTHING, db_column="division")

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "organizations"


class RequestStatuses(models.Model):
    name = models.CharField(primary_key=True, max_length=128)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "request_statuses"


class Requests(models.Model):
    id = models.BigAutoField(primary_key=True)
    is_team_type = models.BooleanField()
    project_team_name = models.CharField(max_length=100, blank=True, null=True)
    organization = models.ForeignKey(
        Organizations, models.DO_NOTHING, db_column="organization"
    )
    nomination = models.ForeignKey(
        Nominations, models.DO_NOTHING, db_column="nomination"
    )
    about_information = models.CharField(max_length=500, blank=True, null=True)
    not_secret = models.BooleanField()
    to_data_processing = models.BooleanField()
    to_processing_other_data = models.BooleanField()
    creator_is_tech_support = models.BooleanField()
    new_products = models.BooleanField()
    global_achievements = models.BooleanField()
    market_share_increase = models.BooleanField()
    сost_reduction = models.BooleanField()
    core_achievement = models.CharField(max_length=1000)
    consent_file = models.BinaryField(blank=True, null=True)
    is_start_reconciliation = models.BooleanField()
    edit_time = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=100)
    status = models.ForeignKey(RequestStatuses, models.DO_NOTHING, db_column="status")

    def __str__(self) -> str:
        return f"{self.id} {self.nomination}-{self.organization}"

    class Meta:
        db_table = "requests"


class RequestsOfEmployees(models.Model):
    id = models.BigAutoField(primary_key=True)
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column="employee")
    request = models.ForeignKey(Requests, models.DO_NOTHING, db_column="request")

    def __str__(self) -> str:
        return f"{self.employee} {self.request}"

    class Meta:
        db_table = "requests_of_employees"


class Roles(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = "roles"


class Users(models.Model):
    login = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=128)
    role = models.ForeignKey(Roles, models.DO_NOTHING, db_column="role")

    def __str__(self) -> str:
        return self.login

    class Meta:
        db_table = "users"
