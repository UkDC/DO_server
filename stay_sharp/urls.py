
from django.contrib import admin
from django.urls import path, include
from stay_sharp import views

urlpatterns = [
    path('account_table', views.account_table, name='account_table'),
    path('feedback', views.feedback, name='feedback'),
    path('calculation', views.CalculationView.as_view(), name='calculation'),
    path('', views.main, name='main'),
    path('choose_the_angle', views.Choose_the_angleView.as_view(), name='choose_the_angle'),
    path('sighup', views.RegisterFormView.as_view(), name='sighup'),
    path('register_done', views.RegisterDoneView.as_view(), name='register_done'),
    path('асtivate/<str:sign>', views.user_activate, name='register_activate'),
]