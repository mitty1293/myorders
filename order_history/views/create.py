from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from order_history.models import (
    Category,
    Manufacturer,
    ProducingArea,
    Product,
    Unit,
    Vendor,
)


class Create(CreateView):
    template_name = "order_history/create.html"
    model_matrix = {
        "category": Category,
        "manufacturer": Manufacturer,
        "producingarea": ProducingArea,
        "product": Product,
        "unit": Unit,
        "vendor": Vendor,
    }

    def test(self):
        pass
