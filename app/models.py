# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Dr(models.Model):
    drid = models.IntegerField(db_column='DrID', primary_key=True)  # Field name made lowercase.
    prsnid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PrsnID', blank=True, null=True)  # Field name made lowercase.
    proid = models.ForeignKey('Proficiency', models.DO_NOTHING, db_column='ProID', blank=True, null=True)  # Field name made lowercase.
    uniid = models.ForeignKey('Uni', models.DO_NOTHING, db_column='UniID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dr'


class Hosp(models.Model):
    hospid = models.IntegerField(db_column='HospID', primary_key=True)  # Field name made lowercase.
    hopsname = models.CharField(db_column='HopsName', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    hospnumber = models.CharField(db_column='HospNumber', max_length=11, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hosp'


class Patient(models.Model):
    patientid = models.IntegerField(db_column='PatientID', primary_key=True)  # Field name made lowercase.
    height = models.FloatField(db_column='Height', blank=True, null=True)  # Field name made lowercase.
    weight = models.FloatField(blank=True, null=True)
    prsnid = models.ForeignKey('Person', models.DO_NOTHING, db_column='PrsnID', blank=True, null=True)  # Field name made lowercase.
    emergencycontact = models.CharField(db_column='emergencyContact', max_length=11, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class Person(models.Model):
    prsnid = models.CharField(db_column='PrsnID', primary_key=True, max_length=11)  # Field name made lowercase.
    prsnname = models.CharField(db_column='PrsnName', max_length=45)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=45)  # Field name made lowercase.
    prsnphone = models.CharField(db_column='PrsnPhone', max_length=11)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6, blank=True, null=True)  # Field name made lowercase.
    birth = models.IntegerField(db_column='Birth', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person'


class Pharmacy(models.Model):
    pharid = models.IntegerField(db_column='PharID', primary_key=True)  # Field name made lowercase.
    pharname = models.CharField(db_column='PharName', max_length=45)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=45, blank=True, null=True)  # Field name made lowercase.
    pharphone = models.CharField(db_column='PharPhone', max_length=11, blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=11, blank=True, null=True)  # Field name made lowercase.
    drid = models.ForeignKey(Dr, models.DO_NOTHING, db_column='DrID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pharmacy'


class Proficiency(models.Model):
    proid = models.IntegerField(db_column='ProID', primary_key=True)  # Field name made lowercase.
    proname = models.CharField(db_column='ProName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'proficiency'


class Uni(models.Model):
    uniid = models.IntegerField(db_column='UniID', primary_key=True)  # Field name made lowercase.
    uniname = models.CharField(db_column='UniName', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'uni'


class Visit(models.Model):
    visitid = models.IntegerField(db_column='VisitID', primary_key=True)  # Field name made lowercase.
    visitdate = models.DateField(db_column='VisitDate')  # Field name made lowercase.
    appointmentdate = models.DateField(db_column='AppointmentDate')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15)  # Field name made lowercase.
    drid = models.ForeignKey(Dr, models.DO_NOTHING, db_column='DrID')  # Field name made lowercase.
    patientid = models.ForeignKey(Patient, models.DO_NOTHING, db_column='PatientID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visit'


class Work(models.Model):
    workid = models.IntegerField(db_column='WorkID', primary_key=True)  # Field name made lowercase.
    hospid = models.IntegerField(db_column='HospID', blank=True, null=True)  # Field name made lowercase.
    fee = models.IntegerField(db_column='Fee', blank=True, null=True)  # Field name made lowercase.
    start = models.TimeField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    end = models.TimeField(db_column='End', blank=True, null=True)  # Field name made lowercase.
    weekday = models.CharField(db_column='Weekday', max_length=10, blank=True, null=True)  # Field name made lowercase.
    drid = models.ForeignKey(Dr, models.DO_NOTHING, db_column='DrID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'work'
