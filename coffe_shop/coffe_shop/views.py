from django.shortcuts import render

from .models import Drink


# Create your views here.
def index(request):
    drinks = Drink.objects.all()
    return render(request, 'index.html', {'drinks': drinks})
