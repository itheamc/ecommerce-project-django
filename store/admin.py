from django.contrib import admin
from .models import *


# Creating ModelAdmin
class StoreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'phone', 'address', 'user', 'added_on', 'updated_on']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'added_on', 'updated_on']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'mrp', 'category', 'store', 'added_on', 'updated_on']


# Registering the models
admin.site.register(Store, StoreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
