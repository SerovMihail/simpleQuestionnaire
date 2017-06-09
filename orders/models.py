from django.db import models
from products.models import Product
from django.db.models.signals import post_save


class Status(models.Model):
    status_name = models.CharField(max_length=20)
    last_update = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return 'Статус %s' % self.status_name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'


class Order(models.Model):
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
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

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)


class ProductInOrder(models.Model):
    price_per_item = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    total_price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    count_item = models.IntegerField(default=1)
    order = models.ForeignKey(Order, blank=True, null=True, default=None)
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'Продукт %s' % self.product.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        self.price_per_item = self.product.price
        self.total_price = self.count_item * self.price_per_item

        super(ProductInOrder, self).save(*args, **kwargs)


def post_save_products_in_order(sender, instance, created, **kwargs):
    order = instance.order
    all_products_in_order = ProductInOrder.objects.filter(order=order, is_active=True)

    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True)


post_save.connect(post_save_products_in_order, sender=ProductInOrder)