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

    def get(self, request, *args, **kwargs):
        self.model = self.model_matrix.get(self.kwargs.get("name"))
        return super().get(request, *args, **kwargs)

    # getでもpostでもget_form -> get_form_class でmodelを定義しているが、
    # get_form も get_form_class もrequestを引数に持たないので
    # get と post を両方オーバーライドして
    # self.model = self.model_matrix.get(self.kwargs.get("name")) とするのが良いと思う。
