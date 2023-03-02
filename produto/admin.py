from django.contrib import admin

from . import models


class VariacaoInline(admin.TabularInline):
    """
    exibir um campo extra em branco para facilitar a criação de uma nova 
    variação
    """
    model = models.Variacao
    extra = 1


class ProdutoAdmin(admin.ModelAdmin):
    # quando entrar no produto, define quais os 'filhos' desse produto serão
    # exibidos
    inlines = [
        VariacaoInline
    ]


admin.site.register(models.Produto, ProdutoAdmin)
admin.site.register(models.Variacao)
