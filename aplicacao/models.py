from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length = 50)
    imagem = models.ImageField(upload_to="produtos/", blank=True, null=True, max_length = 250)
    descricao = models.TextField()
    valor = models.DecimalField('Valor do produto', max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length = 150)
    foto = models.ImageField(upload_to="funcionarios/", blank=True, null=True, max_length = 250)
    cpf = models.IntegerField()
    email = models.EmailField()
    telefone = models.IntegerField()
    
    def __str__(self):
        return self.nome
    
class Cliente(models.Model):
    nome = models.CharField(max_length = 150)
    foto = models.ImageField(upload_to="clientes/", blank=True, null=True, max_length=250)
    cpf = models.IntegerField()
    email = models.EmailField()
    telefone = models.IntegerField()
    
    def __str__(self):
        return self.nome