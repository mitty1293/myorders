from django.urls import include, path

from order_history.views import (
    category,
    manufacturer,
    order,
    producingarea,
    product,
    unit,
    vendor,
)

urlpatterns = [
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
    path(
        "product/",
        include(
            [
                path("", product.Index.as_view(), name="product_index"),
                path(
                    "popup/create/",
                    product.PopupCreate.as_view(),
                    name="product_popup_create",
                ),
                path("create/", product.Create.as_view(), name="product_create"),
                path(
                    "popup/update/<int:pk>",
                    product.PopupUpdate.as_view(),
                    name="product_popup_update",
                ),
                path(
                    "update/<int:pk>", product.Update.as_view(), name="product_update"
                ),
                path(
                    "popup/delete/<int:pk>",
                    product.PopupDelete.as_view(),
                    name="product_popup_delete",
                ),
                path(
                    "delete/<int:pk>", product.Delete.as_view(), name="product_delete"
                ),
            ]
        ),
    ),
    path(
        "vendor/",
        include(
            [
                path("", vendor.Index.as_view(), name="vendor_index"),
                path(
                    "popup/create/",
                    vendor.PopupCreate.as_view(),
                    name="vendor_popup_create",
                ),
                path("create/", vendor.Create.as_view(), name="vendor_create"),
                path(
                    "popup/update/<int:pk>",
                    vendor.PopupUpdate.as_view(),
                    name="vendor_popup_update",
                ),
                path("update/<int:pk>", vendor.Update.as_view(), name="vendor_update"),
                path(
                    "popup/delete/<int:pk>",
                    vendor.PopupDelete.as_view(),
                    name="vendor_popup_delete",
                ),
                path("delete/<int:pk>", vendor.Delete.as_view(), name="vendor_delete"),
            ]
        ),
    ),
    path(
        "unit/",
        include(
            [
                path("", unit.Index.as_view(), name="unit_index"),
                path(
                    "popup/create/",
                    unit.PopupCreate.as_view(),
                    name="unit_popup_create",
                ),
                path("create/", unit.Create.as_view(), name="unit_create"),
                path(
                    "popup/update/<int:pk>",
                    unit.PopupUpdate.as_view(),
                    name="unit_popup_update",
                ),
                path("update/<int:pk>", unit.Update.as_view(), name="unit_update"),
                path(
                    "popup/delete/<int:pk>",
                    unit.PopupDelete.as_view(),
                    name="unit_popup_delete",
                ),
                path("delete/<int:pk>", unit.Delete.as_view(), name="unit_delete"),
            ]
        ),
    ),
    path(
        "category/",
        include(
            [
                path("", category.Index.as_view(), name="category_index"),
                path(
                    "popup/create/",
                    category.PopupCreate.as_view(),
                    name="category_popup_create",
                ),
                path("create/", category.Create.as_view(), name="category_create"),
                path(
                    "popup/update/<int:pk>",
                    category.PopupUpdate.as_view(),
                    name="category_popup_update",
                ),
                path(
                    "update/<int:pk>", category.Update.as_view(), name="category_update"
                ),
                path(
                    "popup/delete/<int:pk>",
                    category.PopupDelete.as_view(),
                    name="category_popup_delete",
                ),
                path(
                    "delete/<int:pk>", category.Delete.as_view(), name="category_delete"
                ),
            ]
        ),
    ),
    path(
        "manufacturer/",
        include(
            [
                path("", manufacturer.Index.as_view(), name="manufacturer_index"),
                path(
                    "popup/create/",
                    manufacturer.PopupCreate.as_view(),
                    name="manufacturer_popup_create",
                ),
                path(
                    "create/", manufacturer.Create.as_view(), name="manufacturer_create"
                ),
                path(
                    "popup/update/<int:pk>",
                    manufacturer.PopupUpdate.as_view(),
                    name="manufacturer_popup_update",
                ),
                path(
                    "update/<int:pk>",
                    manufacturer.Update.as_view(),
                    name="manufacturer_update",
                ),
                path(
                    "popup/delete/<int:pk>",
                    manufacturer.PopupDelete.as_view(),
                    name="manufacturer_popup_delete",
                ),
                path(
                    "delete/<int:pk>",
                    manufacturer.Delete.as_view(),
                    name="manufacturer_delete",
                ),
            ]
        ),
    ),
    path(
        "producingarea/",
        include(
            [
                path("", producingarea.Index.as_view(), name="producingarea_index"),
                path(
                    "popup/create/",
                    producingarea.PopupCreate.as_view(),
                    name="producingarea_popup_create",
                ),
                path(
                    "create/",
                    producingarea.Create.as_view(),
                    name="producingarea_create",
                ),
                path(
                    "popup/update/<int:pk>",
                    producingarea.PopupUpdate.as_view(),
                    name="producingarea_popup_update",
                ),
                path(
                    "update/<int:pk>",
                    producingarea.Update.as_view(),
                    name="producingarea_update",
                ),
                path(
                    "popup/delete/<int:pk>",
                    producingarea.PopupDelete.as_view(),
                    name="producingarea_popup_delete",
                ),
                path(
                    "delete/<int:pk>",
                    producingarea.Delete.as_view(),
                    name="producingarea_delete",
                ),
            ]
        ),
    ),
]
