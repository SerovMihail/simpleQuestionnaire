from django.db import models


class Product(models.Model):
    item_name = models.CharField(max_length=100)
    delivery_date = models.DateField()
    price = models.DecimalField()

    def __str__(self):
        return '%s' % self.item_name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'