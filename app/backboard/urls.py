from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse 



urlpatterns = [
    path('index', views.index, name = 'index'), 
    path('add_new_product', views.add_new_product, name = 'add_new_product'),
    path('customers', views.customers, name = 'customers'), 
    path('customer_detail', views.customer_detail, name = 'customer_detail'),
    path('order_detail', views.order_detail, name = 'order_detail'), 
    path('orders', views.orders, name = 'orders'), 
    path('products', views.products, name = 'products'), 
    path('bills', views.bills, name = 'bills'), 
]
