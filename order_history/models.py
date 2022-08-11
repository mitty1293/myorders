from django.db import models


class Common(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def get_model_fields(cls):
        meta_fields = cls._meta.get_fields()
        reject_ManyToOneRel_fields = (
            x for x in meta_fields if not isinstance(x, models.ManyToOneRel)
        )
        return reject_ManyToOneRel_fields

    @classmethod
    def get_class_name(cls):
        return cls.__name__


class Category(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="カテゴリ名",
        max_length=64,
    )

    class Meta:
        db_table = "category"

    def __str__(self):
        return self.name


class Unit(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="単位",
        max_length=32,
    )

    class Meta:
        db_table = "unit"

    def __str__(self):
        return self.name


class Vendor(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="購入元名",
        max_length=64,
    )

    location = models.CharField(
        db_column="location",
        verbose_name="場所",
        max_length=64,
    )

    class Meta:
        db_table = "vendor"

    def __str__(self):
        return f"{self.name}:{self.location}"


def get_or_create_undefined_category():
    """
    Categoryモデルに'未分類'が存在しなければ作成、存在すれば'未分類'を返す
    """
    category, _ = Category.objects.get_or_create(id=1, name="未分類")
    return category


def get_or_create_undefined_unit():
    """
    Unitモデルに'未定義'が存在しなければ作成、存在すれば'未定義'を返す
    """
    unit, _ = Unit.objects.get_or_create(id=1, name="未定義")
    return unit


def get_or_create_undefined_vendor():
    """
    Vendorモデルに'未定義'が存在しなければ作成、存在すれば'未定義'を返す
    """
    vendor, _ = Vendor.objects.get_or_create(id=1, name="未定義", location="未定義")
    return vendor


class Product(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="商品名",
        max_length=64,
    )

    category = models.ForeignKey(
        Category,
        db_column="category",
        verbose_name="カテゴリ",
        on_delete=models.SET_DEFAULT,
        default=get_or_create_undefined_category,
    )

    unit = models.ForeignKey(
        Unit,
        db_column="unit",
        verbose_name="単位",
        on_delete=models.SET_DEFAULT,
        default=get_or_create_undefined_unit,
    )

    manufacturer = models.CharField(
        db_column="manufacturer",
        verbose_name="製造者",
        max_length=64,
        blank=True,
    )

    producing_area = models.CharField(
        db_column="producing_area",
        verbose_name="生産地",
        max_length=64,
        blank=True,
    )

    class Meta:
        db_table = "product"

    # def __str__(self):
    #     return f"{self.name}:{self.producing_area}:{self.manufacturer}"


class OrderHistory(Common):
    purchase_date = models.DateField(
        db_column="purchase_date",
        verbose_name="購入日",
    )

    product = models.ForeignKey(
        Product,
        db_column="product",
        verbose_name="商品",
        on_delete=models.CASCADE,
    )

    quantity = models.DecimalField(
        db_column="quantity",
        verbose_name="内容量",
        max_digits=8,
        decimal_places=3,
    )

    price = models.IntegerField(
        db_column="price",
        verbose_name="価格",
    )

    vendor = models.ForeignKey(
        Vendor,
        db_column="vendor",
        verbose_name="購入元",
        on_delete=models.SET_DEFAULT,
        default=get_or_create_undefined_vendor,
    )

    class Meta:
        db_table = "order_history"

    def __str__(self):
        return f"{self.id}:{self.product.name}:{self.vendor.name}"
