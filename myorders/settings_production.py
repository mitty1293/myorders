SECRET_KEY = ""

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "myorders_db",
        "USER": "myorders_user",
        "PASSWORD": "password",
        "HOST": "myorders_db",
        "PORT": "3306",
        "OPTIONS": {
            "charset": "utf8mb4",
        },
    }
}
