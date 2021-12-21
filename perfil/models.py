from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.

class Equipamento(models.Model):

       ESCOLHACONDICAO = (
        ("NOVO", "Novo"),
        ("USADO", "Usado"),
    )

    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)# Tabela Marca - 1 Modelo -> Mtos Equipamentos #Se é Lenovo, Dell, HP etc etc

    modelo = models.Charfield(max_length=50)

    num_serie = models.Charfield(max_length=30)

    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)# Tabela Categoria - 1 Categorias -> Mtos Equipamentos #Se é um notebook, Torre, Servidor etc etc
   
    hist_rma = models.TextField(null=True)

    host_contrato = models.TextField(null=True)

    especificacao = models.TextField()

    locacao = models.ForeignKey('Locacao', on_delete=models.CASCADE, null=True)# Tabela Locacao # - Mtos Equipamentos -> 1 Locacao #Quais equipamentos foram alugados
    
    condicao = models.Charfield(max_length=5, choices=ESCOLHACONDICAO) #O equipamento é NOVO ou USADO

    status = models.ForeignKey('Status_Notebook', on_delete=models.CASCADE) #1 Status -> 1 Equipamento
    
    
class Marca(models.Model):

    nome = models.Charfield(max_length=15)

class Categoria(models.Model):

    nome = models.Charfield(max_length=15)

class Software(models.Model):

    nome = models.Charfield(max_length=20)

    serial = models.TextField(null=True)

    equipamento = models.ForeignKey('Equipamento', on_delete=models.CASCADE, null=True)# Tabela Software - Mts Softwares -> 1 Equipamento

class Cliente(models.Model):

    nome = models.Charfield(max_length=50)

    cpnj = models.IntegerField()

    endereco = models.Charfield()

    cep = models.Charfield()

    contato = models.ForeignKey('Agenda', on_delete=models.CASCADE) # Mtos Contatos -> Mtos clientes
    

class Locacao(models.Model):

    STATUS_LOCACAO = (
        ('ABT', 'Aberto'),
        ('FCD', 'Fechado'),
        ('RNV', 'Renovado'),
        )

    num_contrato = models.Charfield(max_length=10)

    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)# Tabela Cliente # 1 Cliente -> Mtos Locacao #Qual cliente está fazendo a locação

    data_inicio = models.DateTimeField(default=timezone.now)

    duração = models.Charfield(max_length=20)   

    adtivos = models.TextField(null=True)

    historico = models.TextField(null=True)

    valor = models.Charfield(max_length=10)

    status = models.Charfield(max_length=3, choices=STATUS_LOCACAO) # O equipamento pode ou não ser alugado?


class Agenda(models.Model):
   
    nome = models.Charfield(max_length=50)
    
    email = models.Charfield(max_length=50)
    
    telefones = models.Charfield(max_length=50)

    empresa = models.ForeignKey('Cliente', on_delete=models.CASCADE)


class Status_Notebook(models.Model):

    ESCOLHA_STATUS = (
        ('DPN', 'Disponivel'),
        ('ECT', 'Em Contrato'),
        ('RMA', 'Manutenção'),
        ('VND', 'Vendido'),
        ('IDP', 'Indisponivel'),
    )

    status = models.Charfield(max_length=3, choices=ESCOLHA_STATUS)

    models.Charfield(max_length=3, choices=ESCOLHA_STATUS)
    
    data_inicio = models.DateTimeField(default=timezone.now)
    
    hist_status = Textfield()

class Produto(models.Model):

    nome = models.Charfield(max_length=50)

    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)# Tabela Marca - 1 Modelo -> Mtos Produtos #Se é Lenovo, Dell, HP etc etc

    quantidade = models.IntegerField()

    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)# Tabela Categoria # - 1 Categorias -> Mtos Equipamentos #Se é um notebook, Torre, Servidor etc 
        



















