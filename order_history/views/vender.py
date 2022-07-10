from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import Vendor


class Index(ListView):
    template_name = "order_history/vender/index.html"
    model = Vendor


class Detail(DetailView):
    template_name = "order_history/vender/detail.html"
    model = Vendor


class Create(CreateView):
    template_name = "order_history/vender/create.html"
    model = Vendor
    fields = {
        "name",
        "location",
    }
    success_url = reverse_lazy("venderindex")
    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update:
    pass


class Delete:
    pass
