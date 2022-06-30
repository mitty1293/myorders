from django.shortcuts import render
from django.views.generic import CreateView
from order_history.models import OrderHistory


class Index:
    pass


class Detail:
    pass


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
