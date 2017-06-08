from django.db import models
from products.models import Product


class Status(models.Model):
    status_name = models.CharField(max_length=20)
    last_update = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return 'Статус %s' % self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class Order(models.Model):
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=Product.price)
    count_items = models.IntegerField(default=1)
    order_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    comment = models.TextField(blank=True)
    status = models.ForeignKey(Status,  blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    created = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return 'Продукт %s' % self.order_name

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class ProductInOrder(models.Model):
    price_per_item = models.DecimalField(decimal_places=2, max_digits=10, default=Product.price)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)

    def __str__(self):
        return 'Продукт %s' % self.product.item_name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'