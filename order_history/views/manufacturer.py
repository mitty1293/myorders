import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from order_history.models import Manufacturer


class Index(ListView):
    template_name = "order_history/index.html"
    model = Manufacturer
    model_class_name_lower = model.get_class_name().lower()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        context["urlname_create"] = f"{self.model_class_name_lower}_create"
        context["urlname_update"] = f"{self.model_class_name_lower}_update"
        return context


class Create(CreateView):
    template_name = "order_history/create.html"
    model = Manufacturer
    model_class_name_lower = model.get_class_name().lower()
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy(f"{model_class_name_lower}_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["urlname_index"] = f"{self.model_class_name_lower}_index"
        return context


class PopupCreate(Create):
    def form_valid(self, form):
        manufacturer = form.save()
        context = {
            "object_model": "manufacturer",
            "object_name": str(manufacturer),
            "object_pk": manufacturer.pk,
            "function_name": "add_select_option",
        }
        return render(self.request, "order_history/close.html", context)


class Update(UpdateView):
    template_name = "order_history/update.html"
    model = Manufacturer
    model_class_name_lower = model.get_class_name().lower()
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy(f"{model_class_name_lower}_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["urlname_index"] = f"{self.model_class_name_lower}_index"
        context["urlname_delete"] = f"{self.model_class_name_lower}_delete"
        return context


class PopupUpdate(Update):
    def form_valid(self, form):
        manufacturer = form.save()
        context = {
            "object_model": "manufacturer",
            "object_name": str(manufacturer),
            "object_pk": manufacturer.pk,
            "function_name": "update_select_option",
        }
        return render(self.request, "order_history/close.html", context)


class Delete(DeleteView):
    template_name = "order_history/delete.html"
    model = Manufacturer
    model_class_name_lower = model.get_class_name().lower()
    success_url = reverse_lazy(f"{model_class_name_lower}_index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["urlname_index"] = f"{self.model_class_name_lower}_index"
        return context
