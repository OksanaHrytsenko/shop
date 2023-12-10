from config.settings.base import *  # NOQA

SECRET_KEY = "django-insecure-)811+4fn7&7y48%5#m@76sd!q373@pqi3n%agr&p%c5is@u9to"

DEBUG = False

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # NOQA
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
