from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
import datetime
from .models import *
from .forms import *
import csv

def build_query(table, columns, data, model):
    execute = False
    query = "SELECT * FROM " + table + " WHERE "
    for i in range(len(columns)):
        if(data["detalle"][i]):
            if(execute):
                query += " and "
            execute = True
            if("..." in data["criterio"][i]):
                if("%" in data["criterio"][i]):
                    data["criterio"][i] = data["criterio"][i].replace("%...%","'%%" + data["detalle"][i] + "%%'")
                elif("^" in data["criterio"][i]):
                    data["criterio"][i] = data["criterio"][i].replace("^...$","'^" + data["detalle"][i] + "$'")
                else:
                    data["criterio"][i] = data["criterio"][i].replace("...","'" + data["detalle"][i] + "'")
                query += columns[i] + " " + data["criterio"][i] 
            else:    
                query += columns[i] + " " + data["criterio"][i] + " '" + data["detalle"][i] +"'"
    if(execute):
        q = model.admin.raw(query)
    else:
        q = {}
    return q, str(query)

def export_csv_file(request, queryset, columns,table_name):
    response = HttpResponse(content_type='text/csv')
    name = "Report_" + table_name + ".csv"
    response['Content-Disposition'] = 'attachment;filename='+name
    writer = csv.writer(response)
    writer.writerow(columns)
    for row in queryset:
        if(table_name == "Accounts"):
            writer.writerow([row.account_name,row.application_name, row.application_type, row.host_name, row.account_type])
        elif(table_name == "A2AMappings"):
            writer.writerow([row.target_alias.alias_name, row.request_server])
        elif(table_name == "Applications"):
            writer.writerow([row.application_name, row.application_type, row.host_name])
        elif(table_name == "Aliases"):
            writer.writerow([row.alias_name, row.host_name, row.application_name, row.account_name])
        elif(table_name == "Servers"):
            writer.writerow([row.host_name, row.ip_address])
        elif(table_name == "Target Groups"):
            writer.writerow([row.name,row.type,row.description])
        elif(table_name == "Users"):
            writer.writerow([row.user, row.authentication, row.first_name, row.last_name])
        elif(table_name == "User Groups"):
            writer.writerow([row.name, row.description])
    return response

class IndexView(TemplateView):
    template_name = "renta.html" 

class CuentasView(FormView):
    template_name = "verCuentas.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(CuentasView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] = Accounts.admin.raw("SELECT * from accounts") 
        return context

    def render_to_response(self, context):
        return super(CuentasView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["account_name", "application_name", "application_type", "host_name", "account_type"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    if(data["form"][0] == "Privates"):
                        query = "select distinct * from accounts where account_name not like 'fcssa%%' and account_name not like 'PA2%%' and account_name not like 'TA%%' and account_name not like 'FIREC%%' and account_name not like 'FC-UAT%%' and account_name not like 'desa%%' and account_name not like 'FC-%%' and account_name not like 'FC_%%' and account_name not like 'TB%%' and account_name not like 'tb%%' and account_name not like 'TC%%' and account_name not like 'DA%%' and account_name not like 'IA%%' and account_name not like 'ia%%' and account_name not like 'DA%%' and account_name not like 'sclclavelo' and account_name not like 'ta%%' and account_name not like 'IB%%' and account_name not like 'DB%%' and account_name not like 'DC%%' and account_name not like 'IC%%' and account_name not like 'PCLFIRE%%' and account_name not like 'fcist_1' order by host_name"
                        context["data"],context["consulta"] = Accounts.admin.raw(query), str(query)
                        print(query)
                        print(context["data"])
                        context["filtered"] = True
                    else:
                        context['data'] = Accounts.admin.raw(data["form"][0])
                        return export_csv_file(request, context['data'],columns,"Accounts")
            else:
                context["data"],context["consulta"] = build_query("accounts", columns, data, Accounts)
                context["filtered"] = True
                
            return super(CuentasView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        return super(CuentasView, self).form_valid(form)

class UsuariosView(FormView):
    template_name = "verUsuarios.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(UsuariosView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  Users.admin.raw("SELECT * from users") 
        return context

    def render_to_response(self, context):
        return super(UsuariosView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["user","authentication", "first_name", "last_Name"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    if(data["form"][0] == "CHL"):
                        query = "SELECT * FROM `users` WHERE `Authentication` LIKE 'CHL'"
                        context["data"],context["consulta"] = Users.admin.raw(query), str(query)
                        context["filtered"] = True
                    else:
                        context['data'] = Users.admin.raw(data["form"][0])
                        return export_csv_file(request, context['data'],columns,"Users")
            else:
                context["data"],context["consulta"] = build_query("users", columns, data, Users)
                context["filtered"] = True
            return super(UsuariosView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class AplicacionesView(FormView):
    template_name = "verAplicaciones.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(AplicacionesView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  Applications.admin.raw("SELECT * from applications") 
        return context

    def render_to_response(self, context):
        return super(AplicacionesView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["application_name","application_type", "host_name"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = Accounts.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"Applications")
            else:
                context["data"],context["consulta"] = build_query("accounts", columns, data, Accounts)
                context["filtered"] = True
            return super(AplicacionesView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class ServidoresView(FormView):
    template_name = "verServidores.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(ServidoresView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  Servers.admin.raw("SELECT * from servers") 
        return context

    def render_to_response(self, context):
        return super(ServidoresView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["host_name","ip_address"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = Servers.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"Servers")
            else:
                context["data"],context["consulta"] = build_query("servers", columns, data, Servers)
                context["filtered"] = True
            return super(ServidoresView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class AliasesView(FormView):
    template_name = "verAliases.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(AliasesView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  Aliases.admin.raw("SELECT * from aliases") 
        return context

    def render_to_response(self, context):
        return super(AliasesView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["alias_name","host_name","application_name","account_name"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = Aliases.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"Aliases")
            else:
                context["data"],context["consulta"] = build_query("aliases", columns, data, Aliases)
                context["filtered"] = True
            return super(AliasesView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class MappingsView(FormView):
    template_name = "verMappings.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(MappingsView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  A2AMappings.admin.raw("SELECT * from a2a_mappings") 
        return context

    def render_to_response(self, context):
        return super(MappingsView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["target_alias","request_server"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = A2AMappings.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"A2AMappings")
            else:
                context["data"],context["consulta"] = build_query("a2a_mappings", columns, data, A2AMappings)
                context["filtered"] = True
            return super(MappingsView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class TgView(FormView):
    template_name = "verTargetgroups.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(TgView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  TargetGroups.admin.raw("SELECT * from target_groups") 
        return context

    def render_to_response(self, context):
        return super(TgView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["name","type","description"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = TargetGroups.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"Target Groups")
            else:
                context["data"],context["consulta"] = build_query("target_groups", columns, data, TargetGroups)
                context["filtered"] = True
            return super(TgView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()

class UgView(FormView):
    template_name = "verUsergroups.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(UgView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        context["data"] =  UserGroups.admin.raw("SELECT * from user_groups") 
        return context

    def render_to_response(self, context):
        return super(UgView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["name","description"]
            if(data["form"][0] != "filtrar"):
                if(data["form"][0] != "exportar"):
                    context['data'] = UserGroups.admin.raw(data["form"][0])
                return export_csv_file(request, context['data'],columns,"User Groups")
            else:
                context["data"],context["consulta"] = build_query("user_groups", columns, data, UserGroups)
                context["filtered"] = True
            return super(UgView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()