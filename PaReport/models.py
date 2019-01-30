from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime

class A2AMappings(models.Model):
    id = models.IntegerField(primary_key=True)
    target_alias = models.CharField(db_column='Target_Alias', max_length=200)  # Field name made lowercase.
    request_server = models.CharField(db_column='Request_Server', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'a2a_mappings'


class Accounts(models.Model):
    account_name = models.CharField(db_column='Account_Name', max_length=200)  # Field name made lowercase.
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=100)  # Field name made lowercase.
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
    account_type = models.IntegerField(db_column='Account_Type')  # Field name made lowercase.
    verified = models.CharField(db_column='Verified', max_length=29)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='update_date')

    class Meta:
        managed = False
        db_table = 'accounts'


class Aliases(models.Model):
    alias_name = models.CharField(db_column='Alias_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aliases'


class Applications(models.Model):
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=200)  # Field name made lowercase.
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'applications'

class Servers(models.Model):
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
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


class TgAccounts(models.Model):
    id_account = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='id_account')
    id_tg = models.ForeignKey(TargetGroups, models.DO_NOTHING, db_column='id_tg')

    class Meta:
        managed = False
        db_table = 'tg_accounts'


class TgApplications(models.Model):
    id_tg = models.ForeignKey(TargetGroups, models.DO_NOTHING, db_column='id_tg')
    id_app = models.ForeignKey(Applications, models.DO_NOTHING, db_column='id_app')

    class Meta:
        managed = False
        db_table = 'tg_applications'


class TgServers(models.Model):
    id_tg = models.ForeignKey(TargetGroups, models.DO_NOTHING, db_column='id_tg')
    id_server = models.ForeignKey(Servers, models.DO_NOTHING, db_column='id_server')

    class Meta:
        managed = False
        db_table = 'tg_servers'


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
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'users_groups'
