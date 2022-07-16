import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from order_history.models import Unit


class Index(ListView):
    template_name = "order_history/unit/index.html"
    model = Unit

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        return context


class Create(CreateView):
    template_name = "order_history/unit/create.html"
    model = Unit
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("unitindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Update(UpdateView):
    template_name = "order_history/unit/update.html"
    model = Unit
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("unitindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Delete(DeleteView):
    template_name = "order_history/unit/delete.html"
    model = Unit
    success_url = reverse_lazy("unitindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context
