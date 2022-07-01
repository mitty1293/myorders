from django.urls import include, path

from order_history.views import order

urlpatterns = [
    path(
        "<str:test>/",
        include(
            [
                path("", order.Index.as_view(), name="orderindex"),
                path("detail/<int:pk>", order.Detail.as_view(), name="orderdetail"),
                path("create/", order.Create.as_view(), name="ordercreate"),
                # path("update/<int:pk>", order.Update.as_view(), name="orderupdate"),
                # path("delete/<int:pk>", order.Delete.as_view(), name="orderdelete"),
            ]
        ),
    ),
]
