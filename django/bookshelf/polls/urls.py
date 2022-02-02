from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bitches', views.bitches, name='bitches'),
]
