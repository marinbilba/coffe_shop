from django.shortcuts import render

# Create your views here.
from shop.models import *

items = [Drink(DrinkTypes.Tea, TeaTypes.Green, DrinkSizes.Small),
         Drink(DrinkTypes.Tea, TeaTypes.Black, DrinkSizes.Small),
         Drink(DrinkTypes.Tea, TeaTypes.Mint, DrinkSizes.Small),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Espresso, DrinkSizes.Small),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Latte, DrinkSizes.Small),
         Drink(DrinkTypes.Coffee, CoffeeTypes.Americano, DrinkSizes.Small),
         Drink(DrinkTypes.Juice, JuiceType.Apple, DrinkSizes.Small),
         Drink(DrinkTypes.Juice, JuiceType.Carrot, DrinkSizes.Small),
         Drink(DrinkTypes.Juice, JuiceType.Orange, DrinkSizes.Small)]


def index(request):
    return render(request, 'index.html', {'items': items})
