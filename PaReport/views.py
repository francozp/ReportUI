from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
import datetime
from .models import *
from .forms import *

def build_query(table, columns, data):
    execute = False
    query = "SELECT * FROM " + table + " WHERE "
    columns = ["account_name", "application_name", "application_type", "host_name", "account_type", "verified"]
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
        q = Accounts.cuentas.raw(query)
    else:
        q = {}
    return q

class IndexView(TemplateView):
    template_name = "index.html" 

class QueryView(FormView):
    template_name = "query.html"
    form_class = QueryForm
    def get_context_data(self, **kwargs):
        context = super(QueryView, self).get_context_data(**kwargs)
        print(self.request.method)
        if self.request.method == 'POST':
            form = QueryForm(self.request.POST)
        else:
            form = QueryForm()
        context['form'] = form
        return context

    def render_to_response(self, context):
        return super(QueryView, self).render_to_response(context)

    def post(self, request, *args, **kwargs):
            context = self.get_context_data()
            data = self.request.POST
            data = dict(data) # De querydict a diccionario python
            columns = ["account_name", "application_name", "application_type", "host_name", "account_type", "verified"]
            context["sql"] = build_query("accounts", columns, data)
            return super(FormView, self).render_to_response(context)


    def form_valid(self, form):
        context = self.get_context_data()
        print(context)
        return super(QueryView, self).form_valid(form)


class CuentasView(ListView):
    model = Accounts
    template_name = "verCuentas.html"
    def render_to_response(self, context):
        return super(CuentasView, self).render_to_response(context)
        
class UsuariosView(ListView):
    model = Users
    template_name = "verUsuarios.html"

    def render_to_response(self, context):
        return super(UsuariosView, self).render_to_response(context)

class AplicacionesView(ListView):
    model = Applications
    template_name = "verAplicaciones.html"
    def render_to_response(self, context):
        return super(AplicacionesView, self).render_to_response(context)

class ServidoresView(ListView):
    model = Servers
    template_name = "verServidores.html"
    def render_to_response(self, context):
        return super(ServidoresView, self).render_to_response(context)

class AliasesView(ListView):
    model = Aliases
    template_name = "verAliases.html"
    def render_to_response(self, context):
        return super(AliasesView, self).render_to_response(context)

class MappingsView(ListView):
    model = A2AMappings
    template_name = "verMappings.html"
    def render_to_response(self, context):
        return super(MappingsView, self).render_to_response(context)

class TgView(ListView):
    model = TargetGroups
    template_name = "verTargetgroups.html"
    def render_to_response(self, context):
        return super(TgView, self).render_to_response(context)

class UgView(ListView):
    model = UsersGroups
    template_name = "verUsergroups.html"
    def render_to_response(self, context):
        return super(UgView, self).render_to_response(context)