from django.urls import include, path

from order_history.views import category, order, product, unit, vendor

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
                path("create/", product.Create.as_view(), name="product_create"),
                path(
                    "update/<int:pk>", product.Update.as_view(), name="product_update"
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
                path("create/", vendor.Create.as_view(), name="vendor_create"),
                path("update/<int:pk>", vendor.Update.as_view(), name="vendor_update"),
                path("delete/<int:pk>", vendor.Delete.as_view(), name="vendor_delete"),
            ]
        ),
    ),
    path(
        "unit/",
        include(
            [
                path("", unit.Index.as_view(), name="unit_index"),
                path("create/", unit.Create.as_view(), name="unit_create"),
                path("update/<int:pk>", unit.Update.as_view(), name="unit_update"),
                path("delete/<int:pk>", unit.Delete.as_view(), name="unit_delete"),
            ]
        ),
    ),
    path(
        "category/",
        include(
            [
                path("", category.Index.as_view(), name="category_index"),
                path("create/", category.Create.as_view(), name="category_create"),
                path(
                    "update/<int:pk>", category.Update.as_view(), name="category_update"
                ),
                path(
                    "delete/<int:pk>", category.Delete.as_view(), name="category_delete"
                ),
            ]
        ),
    ),
]
