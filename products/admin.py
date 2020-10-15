from django.contrib import admin
from .models import Product, Category, Room

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    """ Added following class 15/10/20 to all rooms and date booking"""


class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'event_dates',
        'number_available',
        'is_available',
        'date',
        'description',
        'price',
        'rating',
        'image_url',
        'image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Room, RoomAdmin)
