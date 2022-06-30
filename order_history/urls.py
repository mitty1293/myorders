from django.urls import path

from order_history.views import order

urlpatterns = [
    # path("", order.Index.as_view(), name="orderindex"),
    # path("orderdetail/", order.Detail.as_view(), name="orderdetail"),
    path("ordercreate/", order.Create.as_view(), name="ordercreate"),
    # path("orderupdate/", order.Update.as_view(), name="orderupdate"),
    # path("orderdelete/", order.Delete.as_view(), name="orderdelete"),
]
