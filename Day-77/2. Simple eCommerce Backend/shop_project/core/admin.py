from django.contrib import admin
from .models import Category, Product, Order

class ProductInline(admin.TabularInline):
    model = Order.products.through
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'category']
    list_filter = ['in_stock', 'category']
    search_fields = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'created_at']
    inlines = [ProductInline]