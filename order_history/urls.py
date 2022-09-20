from django.urls import include, path

from order_history.views import create, delete, index, update

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
    )
]
