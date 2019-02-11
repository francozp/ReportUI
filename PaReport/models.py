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
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a2a_mappings'
        unique_together = (('id', 'report_id'),)


class Accounts(models.Model):
    id = models.IntegerField()
    account_name = models.CharField(primary_key=True, max_length=200)
    application_name = models.ForeignKey('Applications', models.DO_NOTHING, db_column='application_name')
    application_type = models.CharField(max_length=200)
    host_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)
    verified = models.CharField(max_length=200)
    report = models.ForeignKey('Report', models.DO_NOTHING)
    cuentas = models.Manager()
    class Meta:
        managed = False
        db_table = 'accounts'
        unique_together = (('account_name', 'application_name', 'host_name', 'report'),)


class AccountsDates(models.Model):
    account_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='account_name', related_name='+' )
    app_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='app_name', related_name='+' )
    host_name = models.CharField(max_length=200)
    creation_date = models.DateTimeField()
    verification_date = models.DateTimeField()
    last_used = models.DateTimeField()
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_dates'


class Aliases(models.Model):
    alias_name = models.CharField(db_column='Alias_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=200)  # Field name made lowercase.
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'aliases'
        unique_together = (('alias_name', 'report_id'),)


class Applications(models.Model):
    application_name = models.CharField(db_column='Application_Name', primary_key=True, max_length=200)  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=200)  # Field name made lowercase.
    host_name = models.ForeignKey('Servers', models.DO_NOTHING, db_column='Host_Name')  # Field name made lowercase.
    report = models.ForeignKey('Report', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('application_name', 'host_name', 'report'),)


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    completed = models.IntegerField()
    closed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'report'


class Servers(models.Model):
    host_name = models.CharField(db_column='Host_Name', primary_key=True, max_length=100)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=100)  # Field name made lowercase.
    report = models.ForeignKey(Report, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'servers'
        unique_together = (('host_name', 'ip_address', 'report'),)


class TargetGroups(models.Model):
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'target_groups'
        unique_together = (('id', 'report_id'),)


class TgAccounts(models.Model):
    tg = models.ForeignKey(TargetGroups, models.DO_NOTHING)
    account_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='account_name', related_name='+' )
    app_name = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='app_name', related_name='+' )
    host_name = models.CharField(max_length=200)
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tg_accounts'


class TgApplications(models.Model):
    app_name = models.ForeignKey(Applications, models.DO_NOTHING, db_column='app_name', related_name='+' )
    host_name = models.ForeignKey(Applications, models.DO_NOTHING, db_column='host_name', related_name='+' )
    tg = models.ForeignKey(TargetGroups, models.DO_NOTHING)
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tg_applications'


class TgServers(models.Model):
    tg = models.ForeignKey(TargetGroups, models.DO_NOTHING)
    host_name = models.ForeignKey(Servers, models.DO_NOTHING, db_column='host_name')
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tg_servers'


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
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'
        unique_together = (('user', 'report_id'),)


class UsersGroups(models.Model):
    name = models.CharField(db_column='Name', primary_key=True, max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    report_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('name', 'report_id'),)
