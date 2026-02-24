from django.shortcuts import render, redirect
from .models import Equipamentos
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "checkpoint/home.html")

def equipamentos(request):
    if request.method == "POST":
        numeroEquipamento = request.POST.get("numeroEquipamento")
        nomeEquipamento = request.POST.get("nomeEquipamento")
        status = request.POST.get("status")
        messages.success(request,"Equipamento cadastrado com sucesso!")
        Equipamentos.objects.create(numeroEquipamento=numeroEquipamento,nomeEquipamento=nomeEquipamento,status=status) == request.POST.get("equipamentos")
    return render(request, 'checkpoint/equipamentos.html')



def editar_equipamento(request, id):
    equipamentos = Equipamentos.objects.get(id=id)
    if request.method == "POST":
        equipamentos.nomeEquipamento = request.POST.get('nomeEquipamento')
        equipamentos.numeroEquipamento = request.POST.get('numeroEquipamento')
        equipamentos.status = request.POST.get('status')
        equipamentos.save()
        messages.success(request,"Equipamento editado com sucesso!")
        return redirect('/home.html')   
    return render(request, "checkpoint/editar_equipamento.html", {"id": id})
    # return redirect("checkpoint:equipamentos")

def excluir_equipamento(request, id):
    return render(request, "checkpoint/excluir_equipamento.html", {"id": id})
    # return redirect("checkpoint:equipamentos")

def cadastro_usuario(request):
    return render(request, "checkpoint/cadastro_usuario.html")

def itens_cadastro(request):
    return render(request, "checkpoint/itens_cadastro.html")

