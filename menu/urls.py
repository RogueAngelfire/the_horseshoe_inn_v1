from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<menu_id>/', views.menu_detail, name='menu_detail'),
]
