from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return 'Категория товара: %s' % self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=100)
    delivery_date = models.DateField(auto_now_add=True, auto_now=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    color = models.CharField(max_length=10, default='black')
    category = models.ForeignKey(ProductCategory, blank=True, default=None, null=True)
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return 'Цена: %s | Название %s' % (self.price, self.name)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, null=True)
    image = models.ImageField(upload_to='product_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "Заказ %s" % self.product.name

    class Meta:
        verbose_name = 'Фото товара'
        verbose_name_plural = 'Фото товаров'

