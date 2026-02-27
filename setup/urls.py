from django.contrib import admin
from django.urls import path
from checkpoint.views import (
    encerrar_locacao,
    home,
    equipamentos,
    editar_equipamento,
    excluir_equipamento,
    itens_cadastro,
    listar_locacao,
    home_funcionario,
    reservar,
    logout_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('home/', home),
    path('editar_equipamento/<int:id>/', editar_equipamento, name='editar_equipamento'),
    path('excluir_equipamento/<int:id>/', excluir_equipamento, name='excluir_equipamento'),
    path('equipamentos/', equipamentos, name='equipamentos'),
    path('itens_cadastro/', itens_cadastro, name='itens_cadastro'),
    path('listar_locacao/', listar_locacao, name='listar_locacao'),
    path('home_funcionario/', home_funcionario, name='home_funcionario'),
    path('reservar/<int:id>/', reservar, name='reservar'),
    path('encerrar_locacao/<int:id>/', encerrar_locacao, name='encerrar_locacao'),
    path('logout/', logout_view, name='logout'),
]