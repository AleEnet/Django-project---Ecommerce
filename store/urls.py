from django.urls import path
from .views import store, checkout, cart, main

urlpatterns = [
    path('', main, name = "main" ),
    path("store/",store,name = "store"),
    path("cart/", cart, name = "cart" ),
    path("checkout/", checkout, name = "checkout" ),
]