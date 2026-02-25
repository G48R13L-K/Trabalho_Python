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

class Usuarios(models.Model):
    nomeUsuario = models.CharField(max_length=100)
    senha = models.CharField(max_length=12)
    cpf = models.IntegerField()
    def __str__(self):
        return f"{self.nomeUsuario} - {self.senha} -{self.cpf}"

class Locacao(models.Model):
    equipamento = models.ForeignKey(Equipamentos, on_delete=models.SET_NULL, null=True)
    usuario = models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    dataLocacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipamento} - {self.usuario} -{self.dataLocacao}"
    

    
