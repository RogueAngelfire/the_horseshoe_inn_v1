from django.urls import path
from . import views

urlpatterns = [
    path('', views.special_offers, name='special_offers'),
]
