from django.shortcuts import render, redirect
from .models import Equipamentos, Locacao
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "checkpoint/home.html")

def equipamentos(request):
    if request.method == "POST":
        nomeEquipamento = request.POST.get("nomeEquipamento")
        numeroEquipamento = request.POST.get("numeroEquipamento")
        status = request.POST.get("status")
        Equipamentos.objects.create(nomeEquipamento=nomeEquipamento,numeroEquipamento=numeroEquipamento,status=status)
        messages.success(request,"Equipamento cadastrado com sucesso!")
        return redirect('itens_cadastro')
        
    return render(request, 'checkpoint/equipamentos.html')
    



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

def excluir_equipamento(request, id):
    equipamento = Equipamentos.objects.get(id=id)
    if request.method == "POST":
        equipamento.delete()
        messages.success(request,"Equipamento excluído com sucesso!")
        return redirect('itens_cadastro')
    return render(request, "checkpoint/excluir_equipamento.html", {"id": id})
    # return redirect("checkpoint:equipamentos")

def cadastro_usuario(request):
    return render(request, "checkpoint/cadastro_usuario.html")

def itens_cadastro(request):
    equipamentos = Equipamentos.objects.all()
    return render(request, "checkpoint/itens_cadastro.html", {"equipamentos": equipamentos})

def listar_locacao(request):
    locacoes = Locacao.objects.all()
    return render(request, "checkpoint/listar_locacao.html", {"locacoes": locacoes})

def home_funcionario(request):
    return render(request, "checkpoint/home_funcionario.html")