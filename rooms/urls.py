from django.urls import path
from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<int:room_id>/', views.room_detail, name='room_detail'),
    path('add/', views.add_room, name='add_room'),
    path('edit/<int:room_id>/', views.edit_room, name='edit_room'),
    path('delete/<int:room_id>/', views.delete_room, name='delete_room'),
]
