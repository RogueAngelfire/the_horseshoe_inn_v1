from django.contrib import admin
from .models import Room, Category

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'category',
        'name',
        'description',
        'price',
        'rating',
        'image',
    )



class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Room, RoomAdmin)
admin.site.register(Category, CategoryAdmin)
