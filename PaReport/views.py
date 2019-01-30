from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.shortcuts import redirect
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, DetailView, ListView, FormView,CreateView
import datetime
from .models import *

class IndexView(TemplateView):
    template_name = "index.html" 

class CuentasView(ListView):
    model = Accounts
    template_name = "verCuentas.html"
    context_object_name = 'accounts'
    def render_to_response(self, context):
        return super(CuentasView, self).render_to_response(context)
        
class UsuariosView(ListView):
    model = Users
    template_name = "verUsuarios.html"
    context_object_name = 'users'
    def render_to_response(self, context):
        return super(UsuariosView, self).render_to_response(context)

class AplicacionesView(ListView):
    model = Applications
    template_name = "verAplicaciones.html"
    context_object_name = "applications"
    def render_to_response(self, context):
        return super(AplicacionesView, self).render_to_response(context)
