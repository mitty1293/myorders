# myorders
Orders history
## Dump fixture
```
poetry run python manage.py dumpdata order_history.category > order_history/fixtures/fixture_category.json
poetry run python manage.py dumpdata order_history.unit > order_history/fixtures/fixture_unit.json
poetry run python manage.py dumpdata order_history.vendor > order_history/fixtures/fixture_vendor.json
poetry run python manage.py dumpdata order_history.manufacturer > order_history/fixtures/fixture_manufacturer.json
poetry run python manage.py dumpdata order_history.producingarea > order_history/fixtures/fixture_producingarea.json
poetry run python manage.py dumpdata order_history.product > order_history/fixtures/fixture_product.json
```
## Load fixture
```
poetry run python manage.py loaddata order_history/fixtures/fixture_category.json
poetry run python manage.py loaddata order_history/fixtures/fixture_unit.json
poetry run python manage.py loaddata order_history/fixtures/fixture_vendor.json
poetry run python manage.py loaddata order_history/fixtures/fixture_manufacturer.json
poetry run python manage.py loaddata order_history/fixtures/fixture_producingarea.json
poetry run python manage.py loaddata order_history/fixtures/fixture_product.json
```