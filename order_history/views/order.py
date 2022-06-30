from django.shortcuts import render
from django.views.generic import CreateView, DetailView
from order_history.models import OrderHistory


class Index:
    pass


class Detail(DetailView):
    template_name = "order_history/detail.html"
    model = OrderHistory
    # modelはOrderHistoryにしておいて、htmlでobject.product.name等で各モデルのカラムにアクセスできるか。


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


class Update:
    pass


class Delete:
    pass
