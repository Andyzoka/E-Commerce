from django.contrib.auth.models import User
from django.db import models


class Pedido(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Usuário')
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aprovado'),
            ('C', 'Criado'),
            ('R', 'Reprovado'),
            ('P', 'Pendente'),
            ('E', 'Enviado'),
            ('F', 'Finalizado'),
        )
    )

    def __str__(self):
        return f'Pedido N° {self.pk}'


class ItemPedido(models.Model):
    order = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, verbose_name='Pedido')
    product = models.CharField(max_length=255, verbose_name='Produto')
    product_id = models.PositiveBigIntegerField(verbose_name='Produto-id')
    varation = models.CharField(max_length=255, verbose_name='Variação')
    variation_id = models.PositiveBigIntegerField(verbose_name='Variação-id')
    price = models.FloatField(verbose_name='Preço')
    promocional_price = models.FloatField(default=0, verbose_name='Preço-id')
    quantity = models.PositiveBigIntegerField(verbose_name='Quantidade')
    image = models.CharField(max_length=2000, verbose_name='Imagem')

    def __str__(self):
        return f'Item do {self.order}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
