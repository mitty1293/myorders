from django.urls import include, path

from order_history.views import (
    category,
    create,
    delete,
    index,
    manufacturer,
    order,
    producingarea,
    product,
    unit,
    update,
    vendor,
)

app_name = "order_history"

urlpatterns = [
    path(
        "<str:model_name_lower>/",
        include(
            [
                path("", index.Index.as_view(), name="index"),
                path(
                    "popup/create/", create.PopupCreate.as_view(), name="popup_create"
                ),
                path("create/", create.Create.as_view(), name="create"),
                path(
                    "popup/update/<int:pk>",
                    update.PopupUpdate.as_view(),
                    name="popup_update",
                ),
                path("update/<int:pk>", update.Update.as_view(), name="update"),
                path(
                    "popup/delete/<int:pk>",
                    delete.PopupUpDelete.as_view(),
                    name="popup_delete",
                ),
                path("delete/<int:pk>", delete.Delete.as_view(), name="delete"),
            ]
        ),
    ),
    path(
        "order/",
        include(
            [
                path("", order.Index.as_view(), name="orderindex"),
                path("create/", order.Create.as_view(), name="ordercreate"),
                # path("update/<int:pk>", order.Update.as_view(), name="orderupdate"),
                # path("delete/<int:pk>", order.Delete.as_view(), name="orderdelete"),
            ]
        ),
    ),
]
