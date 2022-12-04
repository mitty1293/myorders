# myorders
Orders history
## Development setting
```
poetry env use 3.10
poetry install
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```
## Development server run
```
poetry run python manage.py runserver
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
## Dump fixture
```
poetry run python manage.py dumpdata order_history.category > order_history/fixtures/fixture_category.json
poetry run python manage.py dumpdata order_history.unit > order_history/fixtures/fixture_unit.json
poetry run python manage.py dumpdata order_history.vendor > order_history/fixtures/fixture_vendor.json
poetry run python manage.py dumpdata order_history.manufacturer > order_history/fixtures/fixture_manufacturer.json
poetry run python manage.py dumpdata order_history.producingarea > order_history/fixtures/fixture_producingarea.json
poetry run python manage.py dumpdata order_history.product > order_history/fixtures/fixture_product.json
```