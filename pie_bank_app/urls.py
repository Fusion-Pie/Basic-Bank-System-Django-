from django.contrib import admin
from django.urls import path
from pie_bank_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('details/', views.details, name='details'),
    path('payment/', views.payment, name='payment'),
    path('history/',views.history,name='history')
]
