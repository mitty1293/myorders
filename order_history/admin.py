from django.contrib import admin

from .models import Category, Item, OrderHistory, Unit, Vendor

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Vendor)
admin.site.register(Item)
admin.site.register(OrderHistory)
