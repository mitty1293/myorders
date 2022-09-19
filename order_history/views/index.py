from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from order_history.models import (
    Category,
    Manufacturer,
    ProducingArea,
    Product,
    Unit,
    Vendor,
)


class Index(ListView):
    template_name = "order_history/index.html"
    matrix = {
        "category": Category,
        "manufacturer": Manufacturer,
        "producingarea": ProducingArea,
        "product": Product,
        "unit": Unit,
        "vendor": Vendor,
    }

    def get(self, request, *args, **kwargs):
        self.model = self.matrix.get(self.kwargs.get("name"))
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        context["urlname_create"] = f"{self.model.get_class_name().lower()}_create"
        context["urlname_update"] = f"{self.model.get_class_name().lower()}_update"
        return context

    # CreateViewの場合はget_querysetでself.modelを得る感じか？
    # def get(self, request, *args, **kwargs):
    #     self.url_str = self.kwargs.get("name")
    #     return super().get(request, *args, **kwargs)

    # def get_queryset(self):
    #     self.model = self.matrix.get(self.url_str)
    #     return super().get_queryset()
