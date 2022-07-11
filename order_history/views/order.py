from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import OrderHistory


class Index(ListView):
    template_name = "order_history/order/index.html"
    model = OrderHistory

    def get_context_data(self):
        context = super().get_context_data()
        context["page_title"] = "OrderHistory"
        return context


class Detail(DetailView):
    template_name = "order_history/order/detail.html"
    model = OrderHistory


class Create(CreateView):
    template_name = "order_history/order/create.html"
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
