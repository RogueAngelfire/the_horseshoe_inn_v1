from django.contrib import admin
from .models import Product, Category

# Register your models here.


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
