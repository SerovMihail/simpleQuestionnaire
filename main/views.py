from django.shortcuts import render
from products.models import Product, ProductImage


def home(request):
    products = Product.objects.all()
    products_images = ProductImage.objects.filter(is_active=True)

    return render(request, 'main/home.html', locals())


def articles(request):

    return render(request, 'main/articles.html', locals())
