from datetime import timedelta

from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class CardStatus(models.Model):
    name = models.CharField(
        max_length=24,
        unique=True,
        null=False,
        blank=False,
        verbose_name='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'


class CardSeries(models.Model):
    name = models.CharField(
        max_length=6,
        unique=True,
        null=False,
        blank=False,
        verbose_name='name',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'series'
        verbose_name_plural = 'series'


class Card(models.Model):
    card_number = models.PositiveBigIntegerField(
        verbose_name='card_number',
        default=0,
    )
    status = models.ForeignKey(
        CardStatus,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='status',
    )
    series = models.ForeignKey(
        CardSeries,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='series',
    )
    date_created = models.DateField(
        default=now,
        verbose_name='date_created',
    )
    expire_date = models.DateField(
        default=now() + timedelta(days=365),
        verbose_name='expire_date',
    )
    last_used_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='last_used_date',
    )
    total = models.PositiveIntegerField(
        default=0,
        verbose_name='total',
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name='discount',
    )

    def get_absolute_url(self):
        return reverse('discount_card_detail', kwargs={'card_number': self.card_number})

    def __str__(self):
        return str(self.card_number)

    class Meta:
        verbose_name = 'card'
        verbose_name_plural = 'cards'


class Product(models.Model):
    name = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        verbose_name='name',
    )
    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='price',
    )
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0,
        verbose_name='discount',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'


class Order(models.Model):
    date_created = models.DateTimeField(
        default=now,
        verbose_name='date_created',
    )
    card = models.ForeignKey(
        Card,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='card',
    )

    class Meta:
        verbose_name = 'order'
        verbose_name_plural = 'orders'


class OrderProduct(models.Model):
    discount = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='discount',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.DO_NOTHING,
        null=False,
        blank=False,
        verbose_name='product',
    )
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name='order',
    )

    class Meta:
        verbose_name = 'orderProduct'
        verbose_name_plural = 'orderProducts'
