from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_list, name="product_list"),
    path('<str:category_slug>/', views.product_list, name="product_list_of_category"),
    path('details/<str:product_slug>', views.product_details, name="product_details"),
]
