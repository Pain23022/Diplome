from django.shortcuts import render
from .models import *

def index(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    order = Order.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'order': order,
    }
    return render(request, 'menu/index.html', context)

def card(request):
    return render(request,'menu/card.html')

def delivery(request):
    return render(request,'menu/delivery.html')

def pay(request):
    return render(request,'menu/pay.html')
