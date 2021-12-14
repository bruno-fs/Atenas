from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Equipamentos(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)# Tabela Marca - 1 Modelo -> Mtos Equipamentos
                                                            #Se é Lenovo, Dell, HP etc etc
    modelo = models.Charfield(max_length=50)
    num_serie = models.Charfield(max_length=30)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)# Tabela Categoria - 1 Categorias -> Mtos Equipamentos
                                                            #Se é um notebook, Torre, Servidor etc etc
    hist_rma = models.TextField(null=True)
    host_contrato = models.TextField(null=True)
    especificacao = models.TextField()
    softwares = models.ForeignKey('Softwares', on_delete=models.CASCADE)# Tabela Software - Mts Softwares -> 1 Equipamento
                                                            #Quais softwares estão instalados no computador

    ESCOLHACONDICAO = (
        ("NOVO", "Novo"),
        ("USADO", "Usado"),
    )
    condicao = models.Charfield(max_length=5, choices=ESCOLHACONDICAO) #O equipamento é NOVO ou USADO

    ESCOLHASTATUS = (
        ('DPN', 'Disponivel'),
        ('ECT', 'Em Contrato'),
        ('RMA', 'Manutenção'),
        ('VND', 'Vendido'),
        ('IDP', 'Indisponivel'),
    )
    status = models.Charfield(max_length=3, choices=ESCOLHASTATUS) #O equipamento pode ou não ser alugado?




class Marca(models.Model):
    nome = models.Charfield(max_length=15)

class Categoria(models.Model):
    nome = models.Charfield(max_length=15)

class Software(models.Model):
    nome = models.Charfield(max_length=20)
    serial = models.TextField(null=True)

class Cliente(models.Model):
    nome = models.Charfield(max_length=50)
    cpnj = models.Charfield(max_length=20)
    endereco = models.Charfield(max_length=100)
    contato = models.Charfield(max_lenght=50)

class Locacao():
    num_contrato = models.Charfield(max_length=10)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)# Tabela Cliente
                                                            # 1 Cliente -> Mtos Locacao
                                                        #Qual cliente está fazendo a locação

    data_inicio = models.DateTimeField(default=timezone.now)
    duração = models.Charfield(max_length=20)
    equipamentos = models.ForeignKey('Equipamentos', on_delete=models.CASCADE)# Tabela Equipamentos
                                                                            # - Mtos Equipamentos -> 1 Locacao
                                                                            #Quais equipamentos foram alugados

    adtivos = models.TextField()
    historico = models.TextField()
    valor = models.Charfield(max_length=10)

    STATUS_LOCACAO = (
        ('ABT', 'Aberto'),
        ('FCD', 'Fechado'),
        ('RNV', 'Renovado'),
        )

    status = models.Charfield(max_length=3, choices=STATUS_LOCACAO) # O equipamento pode ou não ser alugado?

class Produtos(models.Model):
    nome = models.Charfield(max_length=50)
    marcamodels.ForeignKey('Marca', on_delete=models.CASCADE)# Tabela Marca - 1 Modelo -> Mtos Equipamentos
                                                            #Se é Lenovo, Dell, HP etc etc
    quantidade = models.IntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)# Tabela Categoria
                                                            # - 1 Categorias -> Mtos Equipamentos
                                                            #Se é um notebook, Torre, Servidor etc etc
