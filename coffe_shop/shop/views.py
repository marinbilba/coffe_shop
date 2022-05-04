from django.http import JsonResponse
from django.shortcuts import render

from shop.models import *

items = [Drink(DrinkTypes.Tea, TeaTypes.Green, DrinkSizes.Medium),
         Drink(DrinkTypes.Tea, TeaTypes.Black, DrinkSizes.Small),
         Drink(DrinkTypes.Tea, TeaTypes.Mint, DrinkSizes.Large),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Espresso, DrinkSizes.Large),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Latte, DrinkSizes.Small),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Americano, DrinkSizes.Small),
         Drink(DrinkTypes.Juice, JuiceType.Apple, DrinkSizes.Small),
         Drink(DrinkTypes.Juice, JuiceType.Carrot, DrinkSizes.Medium),
         Drink(DrinkTypes.Juice, JuiceType.Orange, DrinkSizes.Large)]

total_price = 0.0


def index(request):
    return render(request, 'index.html', {'items': items, 'total_price': total_price})


def add_to_cart(request, price):
    global total_price
    total_price += float(price)
    return JsonResponse({'text': 'Just rendering some JSON :)'})


def reset_price(request):
    global total_price
    total_price = 0.0
    return JsonResponse({'text': 'Jus rendering some JSON :)'})
