import logging

from django.db import models

logger = logging.getLogger(__name__)


class Common(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def get_model_fields(cls):
        meta_fields = cls._meta.get_fields()
        reject_ManyToOneRel_fields = (x for x in meta_fields if not isinstance(x, models.ManyToOneRel))
        return reject_ManyToOneRel_fields

    @classmethod
    def get_class_name(cls):
        return cls.__name__

    @classmethod
    def list_of_object_dict(cls):
        """各モデルのフィールドと値を辞書で返す.

        Returns:
            モデルオブジェクトの各フィールドと値を要素とする辞書のリスト.
            例:
                [
                    {
                        'id': 1,
                        'name': 'milk',
                        'category': <Category: Drink>,
                        'unit': <Unit: ml>,
                        'manufacturer': <Manufacturer: megmilk>,
                    },
                    {
                        'id': 2,
                        'name': 'Orange',
                        ...
                    },
                ]
        """
        list_of_model_obj_dict = []
        for object in cls.objects.all():
            model_obj_dict = {field.name: getattr(object, field.name) for field in object.get_model_fields()}
            list_of_model_obj_dict.append(model_obj_dict)
        return list_of_model_obj_dict


class Category(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="カテゴリ",
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
        default="",
    )

    class Meta:
        db_table = "vendor"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.location})"


class Manufacturer(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="製造者",
        max_length=64,
        blank=True,
    )

    class Meta:
        db_table = "manufacturer"

    def __str__(self):
        return self.name


class ProducingArea(Common):
    name = models.CharField(
        db_column="name",
        verbose_name="生産地",
        max_length=64,
        blank=True,
    )

    class Meta:
        db_table = "producingarea"

    def __str__(self):
        return self.name


def get_or_create_default(sender, **kwargs):
    Category.objects.get_or_create(id=1, name="--")
    Unit.objects.get_or_create(id=1, name="--")
    Vendor.objects.get_or_create(id=1, name="--", location="--")
    Manufacturer.objects.get_or_create(id=1, name="--")
    ProducingArea.objects.get_or_create(id=1, name="--")
    Product.objects.get_or_create(id=1, name="--")


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
        default=1,
    )

    unit = models.ForeignKey(
        Unit,
        db_column="unit",
        verbose_name="単位",
        on_delete=models.SET_DEFAULT,
        default=1,
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        db_column="manufacturer",
        verbose_name="製造者",
        on_delete=models.SET_DEFAULT,
        default=1,
    )

    producingarea = models.ForeignKey(
        ProducingArea,
        db_column="producingarea",
        verbose_name="生産地",
        on_delete=models.SET_DEFAULT,
        default=1,
    )

    class Meta:
        db_table = "product"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.category}, {self.unit}, {self.manufacturer}, {self.producingarea})"


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
        default=1,
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
        default=1,
    )

    class Meta:
        db_table = "order_history"

    def __str__(self):
        return f"{self.__class__.__name__}({self.purchase_date}, {self.product.name}, {self.quantity}, {self.price}, {self.vendor.name})"
