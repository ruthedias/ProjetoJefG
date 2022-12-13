from django.contrib import admin
from aplicacao.models import *

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')


admin.site.register(Categoria)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Funcionario, FuncionarioAdmin)
admin.site.register(Cliente)