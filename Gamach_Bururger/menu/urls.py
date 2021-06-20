from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= 'main'),
    path('/card',views.index, name='card'),
    path('/delivery', views.index, name='delivery'),
    path('/pay', views.index, name='pay'),
]
