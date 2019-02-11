from django.contrib import admin
from .models import*

admin.site.register(A2AMappings)
admin.site.register(Report)
admin.site.register(AccountsDates)
admin.site.register(Accounts)
admin.site.register(Aliases)
admin.site.register(Applications)
admin.site.register(Servers)
admin.site.register(TargetGroups)
admin.site.register(TgAccounts)
admin.site.register(TgApplications)
admin.site.register(TgServers)
admin.site.register(Users)
admin.site.register(UsersGroups)
admin.site.register(UserInGroup)
admin.site.register(UserInTg)