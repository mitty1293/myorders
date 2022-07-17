import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from order_history.models import Product


class Index(ListView):
    template_name = "order_history/product/index.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        return context


class Create(CreateView):
    template_name = "order_history/product/create.html"
    model = Product
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("productindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Update(UpdateView):
    template_name = "order_history/product/update.html"
    model = Product
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("productindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Delete(DeleteView):
    template_name = "order_history/product/delete.html"
    model = Product
    success_url = reverse_lazy("productindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context
