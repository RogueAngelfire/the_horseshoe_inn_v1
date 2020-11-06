from django.contrib import admin
from .models import Menu, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Menu, MenuAdmin)
