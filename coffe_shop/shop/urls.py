from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_to_cart/<str:price>', views.add_to_cart, name='add_to_cart'),
    path('reset_price', views.reset_price, name='reset_price'),
]
