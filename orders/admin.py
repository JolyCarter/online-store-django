from django.contrib import admin

from orders.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_sum')


admin.site.register(Order, OrderAdmin)