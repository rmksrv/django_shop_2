from django.urls import path

from . import views

urlpatterns = [
    path("", views.details, name="cart_details"),
    path("add/<int:product_id>", views.add_to_cart, name="cart_add"),
    path("remove/<int:product_id>", views.remove_from_cart, name="cart_remove"),
]
