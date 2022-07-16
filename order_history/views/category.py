import logging

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from order_history.models import Category


class Index(ListView):
    template_name = "order_history/category/index.html"
    model = Category

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        context["header_row"] = self.model.get_model_fields()
        return context


class Create(CreateView):
    template_name = "order_history/category/create.html"
    model = Category
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("categoryindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context

    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update(UpdateView):
    template_name = "order_history/category/update.html"
    model = Category
    fields = [x.name for x in model.get_model_fields()]
    success_url = reverse_lazy("categoryindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context


class Delete(DeleteView):
    template_name = "order_history/category/delete.html"
    model = Category
    success_url = reverse_lazy("categoryindex")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.model.get_class_name()
        return context
