# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class A2AMappings(models.Model):
    id = models.IntegerField(primary_key=True)
    target_alias = models.ForeignKey('Aliases', models.DO_NOTHING, db_column='Target_Alias')  # Field name made lowercase.
    request_server = models.CharField(db_column='Request_Server', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a2a_mappings'


class Accounts(models.Model):
    account_name = models.CharField(db_column='Account_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    application_name = models.ForeignKey('Applications', models.DO_NOTHING, db_column='Application_Name')  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=100)  # Field name made lowercase.
    host_name = models.ForeignKey('Applications', models.DO_NOTHING, db_column='Host_Name')  # Field name made lowercase.
    account_type = models.IntegerField(db_column='Account_Type')  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=29)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accounts'
        unique_together = (('account_name', 'application_name', 'host_name'),)


class AccountsDates(models.Model):
    id = models.IntegerField()
    creation_date = models.DateTimeField()
    verification_date = models.DateTimeField()
    last_used = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'accounts_dates'


class Aliases(models.Model):
    alias_name = models.CharField(db_column='Alias_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    host_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='Host_Name')  # Field name made lowercase.
    application_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='Application_Name')  # Field name made lowercase.
    account_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='Account_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aliases'


class Applications(models.Model):
    application_name = models.CharField(db_column='Application_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=200)  # Field name made lowercase.
    host_name = models.ForeignKey('Servers', models.DO_NOTHING, db_column='Host_Name')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('application_name', 'host_name'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
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


class Report(models.Model):
    table_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    completed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report'


class Servers(models.Model):
    host_name = models.CharField(db_column='Host_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'servers'


class TargetGroups(models.Model):
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'target_groups'


class UserInGroup(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')
    group_name = models.ForeignKey('UsersGroups', models.DO_NOTHING, db_column='group_name')

    class Meta:
        managed = False
        db_table = 'user_in_group'


class UserInTg(models.Model):
    id_tg = models.ForeignKey(TargetGroups, models.DO_NOTHING, db_column='id_tg')
    user = models.ForeignKey('Users', models.DO_NOTHING, db_column='user')

    class Meta:
        managed = False
        db_table = 'user_in_tg'


class Users(models.Model):
    user = models.CharField(db_column='User', primary_key=True, max_length=100)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=100)  # Field name made lowercase.
    authentication = models.CharField(db_column='Authentication', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=200)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=200)  # Field name made lowercase.
    last_login = models.DateTimeField(db_column='Last_Login')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users'


class UsersGroups(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_groups'
