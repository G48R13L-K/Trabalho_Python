from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "checkpoint/home.html")

def equipamentos(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        status = request.POST.get("status")

        id_equipamento = request.POST.get("equipamentos")
    return render(request, 'checkpoint/equipamentos.html')

def editar_equipamento(request, id):
    return render(request, "checkpoint/editar_equipamento.html", {"id": id})

def excluir_equipamento(request, id):
    return render(request, "checkpoint/excluir_equipamento.html", {"id": id})

def itens_cadastro(request):
    return render(request, "checkpoint/itens_cadastro.html")