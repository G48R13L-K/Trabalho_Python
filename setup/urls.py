"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from checkpoint.views import home, equipamentos, itens_cadastro, cadastroUsuarios, locacoesRegistro
from checkpoint.views import editar_equipamento


import checkpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('equipamentos/', equipamentos, name='equipamentos'),
    path('editar_equipamento/<int:id>/', editar_equipamento, name='editar_equipamento'),
    path('itensCadastro/', itens_cadastro, name='itensCadastro'),
    path('cadastroUsuarios/', cadastroUsuarios, name='cadastroUsuarios'),
    path('locacoesRegistro/', locacoesRegistro, name='locacoesRegistro'),

]
