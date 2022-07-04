from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import OrderHistory


class Index(ListView):
    template_name = "order_history/index.html"
    model = OrderHistory


class Detail(DetailView):
    template_name = "order_history/detail.html"
    model = OrderHistory


class Create(CreateView):
    template_name = "order_history/create.html"
    model = OrderHistory
    fields = {
        "purchase_date",
        "product",
        "quantity",
        "price",
        "vendor",
    }
    success_url = reverse_lazy("orderindex")
    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update:
    pass


class Delete:
    pass
