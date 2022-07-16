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
                path("", product.Index.as_view(), name="productindex"),
                path("detail/<int:pk>", product.Detail.as_view(), name="productdetail"),
                path("create/", product.Create.as_view(), name="productcreate"),
                # path("update/<int:pk>", product.Update.as_view(), name="productupdate"),
                # path("delete/<int:pk>", product.Delete.as_view(), name="productdelete"),
            ]
        ),
    ),
    path(
        "vendor/",
        include(
            [
                path("", vendor.Index.as_view(), name="vendorindex"),
                path("detail/<int:pk>", vendor.Detail.as_view(), name="vendordetail"),
                path("create/", vendor.Create.as_view(), name="vendorcreate"),
                # path("update/<int:pk>", vendor.Update.as_view(), name="vendorupdate"),
                # path("delete/<int:pk>", vendor.Delete.as_view(), name="vendordelete"),
            ]
        ),
    ),
    path(
        "unit/",
        include(
            [
                path("", unit.Index.as_view(), name="unitindex"),
                path("detail/<int:pk>", unit.Detail.as_view(), name="unitdetail"),
                path("create/", unit.Create.as_view(), name="unitcreate"),
                # path("update/<int:pk>", unit.Update.as_view(), name="unitupdate"),
                # path("delete/<int:pk>", unit.Delete.as_view(), name="unitdelete"),
            ]
        ),
    ),
    path(
        "category/",
        include(
            [
                path("", category.Index.as_view(), name="categoryindex"),
                path("create/", category.Create.as_view(), name="categorycreate"),
                path(
                    "update/<int:pk>", category.Update.as_view(), name="categoryupdate"
                ),
                path(
                    "delete/<int:pk>", category.Delete.as_view(), name="categorydelete"
                ),
            ]
        ),
    ),
]
