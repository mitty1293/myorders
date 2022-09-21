from django.shortcuts import render
from django.urls import reverse
from django.views.generic import UpdateView
from order_history.models import (
    Category,
    Manufacturer,
    OrderHistory,
    ProducingArea,
    Product,
    Unit,
    Vendor,
)


class Update(UpdateView):
    template_name = "order_history/update.html"
    model_matrix = {
        "category": Category,
        "manufacturer": Manufacturer,
        "producingarea": ProducingArea,
        "product": Product,
        "unit": Unit,
        "vendor": Vendor,
        "order": OrderHistory,
    }

    def get_queryset(self):
        self.model_name_lower = self.kwargs.get("model_name_lower")
        self.model = self.model_matrix.get(self.model_name_lower)
        self.fields = [x.name for x in self.model.get_model_fields()]
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["model_name_lower"] = self.model_name_lower
        return context

    def get_success_url(self):
        return reverse(
            "order_history:index",
            kwargs={"model_name_lower": self.model_name_lower},
        )


class PopupUpdate(Update):
    def form_valid(self, form):
        _object = form.save()
        context = {
            "object_model": self.model_name_lower,
            "object_name": str(_object),
            "object_pk": _object.pk,
            "function_name": "update_select_option",
        }
        return render(self.request, "order_history/close.html", context)
