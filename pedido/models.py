from django.contrib.auth.models import User
from django.db import models


class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    order = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveBigIntegerField()
    varation = models.CharField(max_length=255)
    variation_id = models.PositiveBigIntegerField()
    price = models.FloatField()
    promocional_price = models.FloatField(default=0)
    quantity = models.PositiveBigIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order}'

    class Meta:
        verbose_name = 'Item do pedido'
        verbose_name_plural = 'Itens do pedido'
