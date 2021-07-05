from django.urls import path
from ShoppingCart import views

urlpatterns = [ 
    path('', views.cart, name="Shopping cart")
]