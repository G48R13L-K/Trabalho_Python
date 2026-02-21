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
from checkpoint.views import home, equipamentos
from checkpoint.views import editar_equipamento
from checkpoint.views import excluir_equipamento, itens_cadastro



import checkpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('equipamentos/', equipamentos, name='equipamentos'),
    path('editar_equipamento/<int:id>/', editar_equipamento, name='editar_equipamento'),
    path('excluir_equipamento/<int:id>/', excluir_equipamento, name='excluir_equipamento'),
    path('itens_cadastro/', itens_cadastro, name='itens_cadastro'),
    ]
