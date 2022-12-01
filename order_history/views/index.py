from django.views.generic import ListView

from order_history.models import Category, Manufacturer, OrderHistory, ProducingArea, Product, Unit, Vendor


class Index(ListView):
    template_name = "order_history/index.html"
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
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        context["model_name_lower"] = self.model_name_lower
        context["urlname_update"] = f"order_history:{self.model_name_lower}_update"
        context["table_data"] = self.model.list_of_object_dict()
        return context
