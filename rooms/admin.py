from django.contrib import admin
from .models import Room

# Register your models here.

""" code didn't work
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event_dates',
        'number_available',
        'is_available',
        'require_breakfast',
        'date',
        'description',
        'price',
        'rating',
        'image_url',
        'image',
    )

    booking = ('room_number',)
    )
"""
admin.site.register(Room)


