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

class CuentasView(TemplateView):
    template_name = "verCuentas.html"