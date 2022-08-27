from django.contrib import admin

from .models import (
    Category,
    Manufacturer,
    OrderHistory,
    ProducingArea,
    Product,
    Unit,
    Vendor,
)

admin.site.register(Category)
admin.site.register(Unit)
admin.site.register(Vendor)
admin.site.register(Manufacturer)
admin.site.register(ProducingArea)
admin.site.register(Product)
admin.site.register(OrderHistory)
