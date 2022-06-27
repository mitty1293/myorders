from django.db import models


class OrderHistory(models.Model):
    class Meta:
        db_table = "order_history"

    created_at = models.DateTimeField(
        db_column="created_at",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        db_column="updated_at",
        auto_now=True,
    )

    category = models.CharField(
        db_column="category",
        verbose_name="分類",
        max_length=64,
        # choices="",
    )

    purchase_date = models.DateField(
        db_column="purchase_date",
        verbose_name="購入日",
    )

    item_description = models.CharField(
        db_column="item_description",
        verbose_name="商品名",
        max_length=64,
    )

    quantity = models.DecimalField(
        db_column="quantity",
        verbose_name="内容量",
    )

    price = models.IntegerField(
        db_column="price",
        verbose_name="価格",
    )

    vendor = models.CharField(
        db_column="vendor",
        verbose_name="購入元",
        max_length=64,
        # choices="",
    )
