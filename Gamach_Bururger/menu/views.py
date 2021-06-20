from django.shortcuts import render
from .models import Menu

def index(request):
    menu = Menu.objects.all()
    return render(request, 'menu/index.html',{'menu': menu},)

def card(request):
    return render(request,'menu/card.html')

def delivery(request):
    return render(request,'menu/delivery.html')

def pay(request):
    return render(request,'menu/pay.html')
