from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from shop.models import Product
from shop.base_context import BaseContext

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
    context = BaseContext(
        page_title="Корзина",
        cart_length=len(Cart(request)),
    ).concat_with(
        {
            "cart": cart,
        }
    )
    return render(request, "cart/details.html", context)
