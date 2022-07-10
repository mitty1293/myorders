from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import Unit


class Index(ListView):
    template_name = "order_history/unit/index.html"
    model = Unit


class Detail(DetailView):
    template_name = "order_history/unit/detail.html"
    model = Unit


class Create(CreateView):
    template_name = "order_history/unit/create.html"
    model = Unit
    fields = {
        "name",
    }
    success_url = reverse_lazy("unitindex")
    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update:
    pass


class Delete:
    pass
