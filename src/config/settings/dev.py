import os

import mongoengine

from config.settings.base import *  # NOQA

SECRET_KEY = "django-secret-key"

DEBUG = True


INSTALLED_APPS += [  # NOQA
    "django_extensions",
]

mongoengine.connect(host="mongodb://admin:admin@mongodb:27017/mongodb_content?authSource=admin")

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
if os.environ.get("GITHUB_WORKFLOW"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "postgres",
            "HOST": "0.0.0.0",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        # "default_postgres_local": {
        # "ENGINE": "django.db.backends.postgresql",
        # "NAME": "my_database",
        # "USER": "Oksana",
        # "PASSWORD": "admin",
        # "HOST": "localhost",
        # "PORT": 5432,
        # },
         "default": {
             "ENGINE": "django.db.backends.postgresql",
             "NAME": os.environ.get("POSTGRES_DB"),
             "USER": os.environ.get("POSTGRES_USER"),
             "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
             "HOST": os.environ.get("POSTGRES_HOST"),
             "PORT": os.environ.get("POSTGRES_PORT"),
         },
        #"default": {
            #"ENGINE": "django.db.backends.sqlite3",
           # "NAME": BASE_DIR / "db.sqlite3",  # NOQA
        #},
    }
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = (BASE_DIR / "static",)  # NOQA
