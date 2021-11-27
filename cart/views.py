from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from shop.models import Product
from .cart import Cart


@require_POST
def add_to_cart(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect("cart_details")


def remove_from_cart(request: HttpRequest, product_id: int):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect("cart_details")


def details(request: HttpRequest):
    cart = Cart(request)
    context = {
        "cart": cart,
    }
    return render(request, "cart/test_details.html", context)
