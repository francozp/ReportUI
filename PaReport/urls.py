"""PaReport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path, reverse
from .views import *

urlpatterns = [
    path('index', IndexView.as_view(), name = 'index'),
    path('cuentas', CuentasView.as_view(), name = 'cuentas'),
    path('usuarios', UsuariosView.as_view(), name = 'usuarios'),
    path('aplicaciones', AplicacionesView.as_view(), name = 'aplicaciones'),
    path('servidores', ServidoresView.as_view(), name = 'servidores'),
    path('aliases', AliasesView.as_view(), name = 'aliases'),
    path('mappings', MappingsView.as_view(), name = 'mappings'),
    path('targetgroups', TgView.as_view(), name = 'targetgroups'),
    path('usergroups', UgView.as_view(), name = 'usergroups'),
    path('consultas/', QueryView.as_view(success_url='/cuentas'), name = 'consultas')
]
