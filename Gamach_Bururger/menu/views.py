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

def card(request,pk):
    menu = Menu.objects.get(pk=pk)
    category = Category.objects.all()
    order = Order.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'order': order,
    }
    return render(request,'menu/card.html',context)

def delivery(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    order = Order.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'order': order,
    }
    return render(request,'menu/delivery.html',context)

def pay(request):
    menu = Menu.objects.all()
    category = Category.objects.all()
    order = Order.objects.all()
    context = {
        'menu': menu,
        'category': category,
        'order': order,
    }
    return render(request,'menu/pay.html',context)
