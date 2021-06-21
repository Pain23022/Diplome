from django.db import models
from django.urls import reverse_lazy


class Category(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Menu(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    image = models.ImageField(upload_to='menu', verbose_name='Карттинка')
    description = models.TextField(verbose_name='описание')
    price = models.IntegerField(verbose_name='цена')
    weight = models.IntegerField(verbose_name='вес')
    availability = models.BooleanField(default=True, verbose_name='наличие')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='катигория')

    def get_absolute_url(self):
        return reverse_lazy('card', kwargs={'pk':self.pk})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class Order(models.Model):
    delivery = models.BooleanField(verbose_name='доставка')
    district = models.CharField(max_length=100, verbose_name='Район')
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.IntegerField(verbose_name='номер телефона')
    address = models.CharField(max_length=200, verbose_name='адрес')
    payment_method = models.CharField(max_length=100, verbose_name='способ оплаты')
    comments = models.TextField(verbose_name='комментии')
    total = models.IntegerField(verbose_name='сумма заказа ')

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
