from typing import Optional

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from cart.cart import Cart
from .models import Category, Product
from .base_context import BaseContext


def product_list(request: HttpRequest, category_slug: Optional[str] = None):
    products = Product.objects.filter(available=True)
    page_title = "Товары"
    banner_image_url = BaseContext.banner_image_url
    banner_header_text = BaseContext.banner_header_text

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

        page_title = category.name
        banner_image_url = category.image.url
        banner_header_text = category.name

    context = BaseContext(
        page_title=page_title,
        banner_with_button=False,
        banner_image_url=banner_image_url,
        banner_header_text=banner_header_text,
        banner_button_request_method="post",
        cart_length=len(Cart(request)),
    ).concat_with(
        {
            "products": products,
        }
    )
    return render(request, "shop/product_list.html", context)


def product_details(request: HttpRequest, product_slug: str):
    product = get_object_or_404(Product, slug=product_slug, available=True)
    context = BaseContext(
        page_title=product.name,
        banner_image_url=product.image.url,
        banner_header_text=product.name,
        banner_content_html_text=product.preview_description,
        banner_button_text="В корзину",
        banner_button_request_method="post",
        banner_button_href=reverse("cart_add", args=[product.id]),
        cart_length=len(Cart(request)),
    ).concat_with({"product": product})
    return render(request, "shop/product_details.html", context)
