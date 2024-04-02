# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Nominees(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30, blank=True, null=True)
    position = models.CharField(max_length=100)
    division = models.ForeignKey('Divisions', models.DO_NOTHING, db_column='division')
    organization = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='organization')
    divide = models.CharField(max_length=100)
    experience = models.CharField(max_length=20)
    is_experience_in_atom_above_year = models.BooleanField()
    no_offenses = models.BooleanField()
    no_discipline_offensives = models.BooleanField()
    photo = models.BinaryField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.position}"

    class Meta:
        managed = False
        db_table = 'nominees'


class Nominations(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey('NominationTypes', models.DO_NOTHING, db_column='type')
    name = models.CharField(unique=True, max_length=50)
    type_of_request = models.ForeignKey('RequestTypes', models.DO_NOTHING, db_column='type_of_request')
    division = models.ForeignKey('Divisions', models.DO_NOTHING, db_column='division')
    division_management_company = models.CharField(max_length=50)
    edit_time = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = 'nominations'


class Criteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    nomination = models.ForeignKey(Nominations, models.DO_NOTHING, db_column='nomination')
    criteria_type = models.CharField(max_length=50)
    description = models.TextField()
    edit_time = models.DateTimeField(blank=True, null=True)
    editor = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    creator = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} {self.criteria_type}"

    class Meta:
        managed = False
        db_table = 'criteria'


class Users(models.Model):
    login = models.CharField(primary_key=True, max_length=30)
    password = models.CharField(max_length=64)
    role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='role')

    def __str__(self) -> str:
        return self.login

    class Meta:
        managed = False
        db_table = 'users'


class Divisions(models.Model):
    name = models.CharField(primary_key=True, max_length=256)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = 'divisions'


class Roles(models.Model):
    name = models.CharField(primary_key=True, max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        managed = False
        db_table = 'roles'


class Requests(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.ForeignKey('RequestTypes', models.DO_NOTHING, db_column='type')
    project_team_name = models.CharField(max_length=100, blank=True, null=True)
    division = models.ForeignKey(Divisions, models.DO_NOTHING, db_column='division')
    organization = models.ForeignKey('Organizations', models.DO_NOTHING, db_column='organization')
    nomination_type = models.ForeignKey('NominationTypes', models.DO_NOTHING, db_column='nomination_type')
    nomination = models.ForeignKey(Nominations, models.DO_NOTHING, db_column='nomination')
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

    def __str__(self) -> str:
        return self.id
    
    class Meta:
        managed = False
        db_table = 'requests'


class NominationTypes(models.Model):
    name = models.CharField(primary_key=True, max_length=256)

    def __str__(self) -> str:
        return self.name

    class Meta:
        managed = False
        db_table = 'nomination_types'


class Organizations(models.Model):
    name = models.CharField(primary_key=True, max_length=256)
    division = models.ForeignKey(Divisions, models.DO_NOTHING, db_column='division')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        managed = False
        db_table = 'organizations'


class RequestsOfNominees(models.Model):
    id = models.BigAutoField(primary_key=True)
    nomine = models.ForeignKey(Nominees, models.DO_NOTHING, db_column='nomine')
    request = models.ForeignKey(Requests, models.DO_NOTHING, db_column='Request')  # Field name made lowercase.

    def __str__(self) -> str:
        return f"{self.nomine} {self.request}"
    
    class Meta:
        managed = False
        db_table = 'requests_of_nominees'


class RequestTypes(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        managed = False
        db_table = 'request_types'


class CriterionResponse(models.Model):
    id = models.BigAutoField(primary_key=True)
    request = models.ForeignKey(Requests, models.DO_NOTHING)
    criteria = models.ForeignKey(Criteria, models.DO_NOTHING)
    answer = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return f"{self.request} {self.criteria}"
    class Meta:
        managed = False
        db_table = 'criterion_response'
