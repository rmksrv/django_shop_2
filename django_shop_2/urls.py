from django.contrib import admin
from django.urls import include, path

from shop.views import product_list as index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="index"),  # TODO: make as redirect
    path("shop/", include("shop.urls")),
    path("cart/", include("cart.urls")),
]
