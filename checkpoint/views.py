from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    return render(request, "checkpoint/home.html")

def itens_cadastro(request):
    if request.method == "POST":
        id = request.POST.get("id")
        nome = request.POST.get("nome")
        status = request.POST.get("status")

        id_equipamento = request.POST.get("equipamentos")
