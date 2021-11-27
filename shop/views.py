from typing import Optional

from django.http import HttpRequest
from django.shortcuts import HttpResponse, get_object_or_404, render

from .models import Category, Product


def product_list(request: HttpRequest, category_slug: Optional[str] = None):
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        "products": products,
    }
    return render(request, "test_product_list.html", context)


def product_details(request: HttpRequest, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    context = {
        "product": product,
    }
    return render(request, "test_product_details.html", context)
