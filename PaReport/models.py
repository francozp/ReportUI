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
    target_alias = models.CharField(max_length=200) # Field name made lowercase.
    request_server = models.CharField(db_column='Request_Server', max_length=200)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'a2a_mappings'


class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=200)
    application_name = models.CharField(max_length=200)
    application_type = models.CharField(max_length=200)
    host_name = models.CharField(max_length=200)
    account_type = models.CharField(max_length=200)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'accounts'
        unique_together = (('account_name', 'application_name', 'host_name'),)


class AccountsDates(models.Model):
    account = models.ForeignKey(Accounts, models.DO_NOTHING, primary_key=True)
    creation_date = models.DateTimeField()
    verification_date = models.DateTimeField()
    last_used = models.DateTimeField()
    report_date = models.DateTimeField()
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'accounts_dates'
        unique_together = (('account', 'report_date'),)


class Aliases(models.Model):
    id = models.AutoField(primary_key=True)
    alias_name = models.CharField(db_column='Alias_Name', max_length=200)  # Field name made lowercase.
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    account_name = models.CharField(db_column='Account_Name', max_length=200)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'aliases'


class Applications(models.Model):
    id = models.AutoField(primary_key=True)
    application_name = models.CharField(db_column='Application_Name', max_length=200)  # Field name made lowercase.
    application_type = models.CharField(db_column='Application_Type', max_length=200)  # Field name made lowercase.
    host_name = models.CharField(max_length=200)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'applications'
        unique_together = (('application_name', 'host_name'),)


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    table_name = models.CharField(max_length=200)
    date = models.DateTimeField()
    completed = models.IntegerField()
    closed = models.IntegerField()
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report'


class ReportA2AMappings(models.Model):
    mapping = models.ForeignKey(A2AMappings, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_a2a_mappings'
        unique_together = (('mapping', 'report'),)


class ReportAccounts(models.Model):
    account = models.ForeignKey(Accounts, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_accounts'
        unique_together = (('account', 'report'),)


class ReportAliases(models.Model):
    alias = models.ForeignKey(Aliases, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_aliases'
        unique_together = (('alias', 'report'),)


class ReportApplications(models.Model):
    application = models.ForeignKey(Applications, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_applications'
        unique_together = (('application', 'report'),)


class ReportServers(models.Model):
    server = models.ForeignKey('Servers', models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_servers'
        unique_together = (('server', 'report'),)


class ReportTargetGroups(models.Model):
    tg = models.ForeignKey('TargetGroups', models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_target_groups'
        unique_together = (('tg', 'report'),)


class ReportUserGroups(models.Model):
    usergroup = models.ForeignKey('UserGroups', models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_user_groups'
        unique_together = (('usergroup', 'report'),)


class ReportUsers(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'report_users'
        unique_together = (('user', 'report'),)


class Servers(models.Model):
    id = models.AutoField(primary_key=True)
    host_name = models.CharField(db_column='Host_Name', max_length=100)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_Address', max_length=100)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'servers'
        unique_together = (('host_name', 'ip_address'),)


class TargetGroups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'target_groups'


class TgAccounts(models.Model):
    tg = models.ForeignKey(TargetGroups, models.DO_NOTHING)
    account = models.ForeignKey(Accounts, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'tg_accounts'
        unique_together = (('account', 'tg', 'report'),)


class UserGroups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=300)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'user_groups'


class UserInTg(models.Model):
    tg_name = models.CharField(primary_key=True, max_length=200)
    user = models.ForeignKey('Users', models.DO_NOTHING)
    report_date = models.DateTimeField()
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'user_in_tg'
        unique_together = (('tg_name', 'user', 'report_date'),)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.CharField(db_column='User', max_length=100)  # Field name made lowercase.
    authentication = models.CharField(db_column='Authentication', max_length=100)  # Field name made lowercase.
    first_name = models.CharField(db_column='First_Name', max_length=200)  # Field name made lowercase.
    last_name = models.CharField(db_column='Last_Name', max_length=200)  # Field name made lowercase.
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'users'


class UsersInfo(models.Model):
    user = models.ForeignKey(Users, models.DO_NOTHING, primary_key=True)
    status = models.CharField(max_length=9, blank=True, null=True)
    last_login = models.DateTimeField()
    report = models.ForeignKey(Report, models.DO_NOTHING)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'users_info'
        unique_together = (('user', 'report'),)


class VerifiedReport(models.Model):
    account = models.ForeignKey(Accounts, models.DO_NOTHING, primary_key=True)
    report = models.ForeignKey(Report, models.DO_NOTHING)
    verified = models.CharField(max_length=200)
    admin = models.Manager()
    class Meta:
        managed = False
        db_table = 'verified_report'
        unique_together = (('account', 'report', 'verified'),)
