from django.contrib import admin

from products.models import Product


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'amount', 'category', 'description', 'photo')


admin.site.register(Product, ProductsAdmin)
