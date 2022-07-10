from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import Product


class Index(ListView):
    template_name = "order_history/product/index.html"
    model = Product


class Detail(DetailView):
    template_name = "order_history/product/detail.html"
    model = Product


class Create(CreateView):
    template_name = "order_history/product/create.html"
    model = Product
    fields = {
        "name",
        "category",
        "unit",
        "manufacturer",
        "producing_area",
    }
    success_url = reverse_lazy("productindex")
    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update:
    pass


class Delete:
    pass
