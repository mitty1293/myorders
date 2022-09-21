#!/bin/bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | poetry run python manage.py shell
# poetry run python manage.py loaddata order_history/fixtures/fixture_category.json
# poetry run python manage.py loaddata order_history/fixtures/fixture_unit.json
# poetry run python manage.py loaddata order_history/fixtures/fixture_vendor.json
# poetry run python manage.py loaddata order_history/fixtures/fixture_manufacturer.json
# poetry run python manage.py loaddata order_history/fixtures/fixture_producingarea.json
# poetry run python manage.py loaddata order_history/fixtures/fixture_product.json
# poetry run python manage.py graph_models order_history -g -o erd.png