from django.contrib import admin

from .models import Brand, Category, Product, Basket


class ProductAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "category", "brand", "price"]


class BrandAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "slug"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "slug"]


class BasketAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "product", "quantity"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Basket, BasketAdmin)
