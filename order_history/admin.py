from django.contrib import admin

from .models import Category, OrderHistory, Product, Unit, Vendor

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Vendor)
admin.site.register(Product)
admin.site.register(OrderHistory)
