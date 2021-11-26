from typing import Optional

from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Category, Product


def product_list(request, category_slug: Optional[str] = None):
    products = Product.objects.filter(available=True)
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return HttpResponse(products)
