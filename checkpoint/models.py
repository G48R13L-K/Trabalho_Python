from django.db import models

class Equipamentos(models.Model):
    nomeEquipamento = models.CharField(max_length=100)
    numeroEquipamento = models.IntegerField(default=0)

    opcoesStatus = [
            ('Disponivel', 'Disponivel'),
            ('Indisponivel', 'Indisponivel'),
            ('Manutencao', 'Manutencao'),
        ]
    status = models.CharField(max_length=20, choices=opcoesStatus, default='Novo')
    

    def __str__(self):
        return f"{self.nomeEquipamento} - {self.numeroEquipamento} -{self.status}"


class Locacao(models.Model):
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.SET_NULL, null=True)
    nomeCliente = models.CharField(max_length=100)
    cpfCliente = models.CharField(max_length=14, null=True, blank=True)
    dataLocacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipamento} - {self.nomeCliente} - {self.cpfCliente} -{self.dataLocacao}"

    
