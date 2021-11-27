from decimal import Decimal

from django.conf import settings
from django.http import HttpRequest

from shop.models import Product


class Cart:
    def __init__(self, request: HttpRequest):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product: Product, qty: int = 1):
        product_id = str(product.id)
        self.cart[product_id] = {
            "qty": qty,
            "price": str(product.price),
        }
        self.save()

    def remove(self, product: Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def total_price(self):
        return sum(
            Decimal(item["qty"] * item["price"])
            for item in self.cart.values()
        )

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            self.cart[str(product.id)]["product"] = product

        for item in self.cart.values():
            item["price"] = Decimal(item["price"])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item["qty"] for item in self.cart.values())
