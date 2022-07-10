from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import Category


class Index(ListView):
    template_name = "order_history/category/index.html"
    model = Category


class Detail(DetailView):
    template_name = "order_history/category/detail.html"
    model = Category


class Create(CreateView):
    template_name = "order_history/category/create.html"
    model = Category
    fields = {
        "name",
    }
    success_url = reverse_lazy("categoryindex")
    # htmlには、modelで設定した「def __str__」の返り値が表示される
    # ファンクションビューで受け取って、urlのパターンによって適切なクラスベースドビューに振り分ける？ができるか？


class Update:
    pass


class Delete:
    pass
