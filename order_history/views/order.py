from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from order_history.models import OrderHistory


class Index(ListView):
    template_name = "order_history/index.html"
    model = OrderHistory


class Detail(DetailView):
    template_name = "order_history/detail.html"
    model = OrderHistory
    # modelはOrderHistoryにしておいて、htmlでobject.product.name等で各モデルのカラムにアクセスできるか。
    # 上記のように、別モデルのインスタンスをフィールドの値として使えるのがforeignkeyの役割かも。
    # https://teratail.com/questions/202236
    # https://codor.co.jp/django/how-to-use-urlpattern
    # https://noauto-nolife.com/post/django-args-kwargs-view-recycle/
    # このmodel内でも、product.nameとかできるかな？


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
    # 7/1
    # listとdetailはhtmlで各モデルのカラムにアクセスで何とかなることはわかった。
    # createやupdateが可能か調べること


class Update:
    pass


class Delete:
    pass
