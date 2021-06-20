from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'main'),
    path('/card',views.card, name='card'),
    path('/delivery', views.delivery, name='delivery'),
    path('/pay', views.pay, name='pay'),
]
