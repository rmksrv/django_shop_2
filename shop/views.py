from typing import Optional

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render

from .models import Category, Product
from .utils import with_base_context


def product_list(request: HttpRequest, category_slug: Optional[str] = None):
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = with_base_context({
        "products": products,
    })
    return render(request, "shop/product_list.html", context)


def product_details(request: HttpRequest, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    context = with_base_context({
        "product": product,
    })
    return render(request, "shop/product_details.html", context)
