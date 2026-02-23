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
    
    status = models.IntegerField()

    def __str__(self):
        return f"{self.nomeEquipamento} - {self.numeroEquipamento} -{self.status}"

class Locacao(models.Model):
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.SET_NULL, null=True)

    