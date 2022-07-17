import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from order_history.models import Vendor


class Index(ListView):
    template_name = "order_history/vendor/index.html"
    model = Vendor

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        return context


class Create(CreateView):
    template_name = "order_history/vendor/create.html"
    model = Vendor
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("vendorindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Update(UpdateView):
    template_name = "order_history/vendor/update.html"
    model = Vendor
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("vendorindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Delete(DeleteView):
    template_name = "order_history/vendor/delete.html"
    model = Vendor
    success_url = reverse_lazy("vendorindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context
