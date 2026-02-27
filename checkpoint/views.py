from datetime import timezone

from django.shortcuts import render, redirect
from .models import Equipamentos, Locacao
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse

def home(request):
    equipamentos = Equipamentos.objects.all()

    return render(request, "checkpoint/home.html", {
        "equipamentos": equipamentos
    })
@login_required
def equipamentos(request):
    if request.method == "POST":
        nomeEquipamento = request.POST.get("nomeEquipamento")
        numeroEquipamento = request.POST.get("numeroEquipamento")
        status = request.POST.get("status")
        Equipamentos.objects.create(nomeEquipamento=nomeEquipamento,numeroEquipamento=numeroEquipamento,status=status)
        messages.success(request,"Equipamento cadastrado com sucesso!")
        return redirect('itens_cadastro')
        
    return render(request, 'checkpoint/equipamentos.html')

@login_required   
def editar_equipamento(request, id):
    equipamentos = Equipamentos.objects.get(id=id)
    if request.method == "POST":
        equipamentos.nomeEquipamento = request.POST.get('nomeEquipamento')
        equipamentos.numeroEquipamento = request.POST.get('numeroEquipamento')
        equipamentos.status = request.POST.get('status')

        equipamentos.save()
        messages.success(request,"Equipamento editado com sucesso!")
        return redirect('itens_cadastro')   
    return render(request, "checkpoint/editar_equipamento.html", {"equipamento": equipamentos})   

def reservar(request, id):
    equipamento = Equipamentos.objects.get(id=id)

    if request.method == "POST":
        nomeCliente = request.POST.get('nomeCliente')
        cpfCliente = request.POST.get('cpfCliente')

        locacao = Locacao.objects.create(
            equipamento=equipamento,
            nomeCliente=nomeCliente,
            cpfCliente=cpfCliente
            
        )

        equipamento.status = 'Indisponivel'
        equipamento.save()

        return render(request, "checkpoint/reservar.html", {
            "equipamento": equipamento,
            "reserva_realizada": True,
            "locacao": locacao
            
            
        })

    return render(request, "checkpoint/reservar.html", {
        "equipamento": equipamento
    })
@login_required
def excluir_equipamento(request, id):
    equipamento = Equipamentos.objects.get(id=id)
    if request.method == "POST":
        equipamento.delete()
        messages.success(request,"Equipamento excluído com sucesso!")
        return redirect('itens_cadastro')
    return render(request, "checkpoint/excluir_equipamento.html", {"id": id})
    # return redirect("checkpoint:equipamentos")


def itens_cadastro(request):
    equipamentos = Equipamentos.objects.all()
    return render(request, "checkpoint/itens_cadastro.html", {"equipamentos": equipamentos})

@login_required
def listar_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, "checkpoint/listar_locacao.html", {"locacoes": locacoes})

@login_required
@permission_required('checkpoint.view_home_funcionario', raise_exception=True) 
def home_funcionario(request):
    return render(request, "checkpoint/home_funcionario.html")


@login_required
def encerrar_locacao(request, id):
    locacao = Locacao.objects.get(id=id)
    if request.method == "POST":
        equipamento = locacao.equipamento
        equipamento.status = 'Disponivel'
        equipamento.save()
        messages.success(request,"Locação encerrada com sucesso!")
        return redirect('listar_locacao')
    
@login_required
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
    
    return redirect('home')