
from django.contrib import admin
from django.urls import path, include
from stay_sharp import views

urlpatterns = [
    path('account_table', views.account_table, name='account_table'),
    path('calculation', views.calculation, name='calculation'),
    path('', views.main, name='main'),
    path('login', views.login, name='login'),
    path('drawing', views.drawing, name='drawing')

]