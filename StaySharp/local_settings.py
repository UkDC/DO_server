import os
from pathlib import Path
import dj_database_url
import psycopg2
import django_heroku

USE_TZ = True

TIME_ZONE = "Europe/Kiev"


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mm7+ac%ujk@w#l_&j+zf5nmb^0ms(^k*&s)_y%bo6*ntwpm5*f"


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        'TIME_ZONE': TIME_ZONE,
    }
}


STATICFILES_DIRS = [
    BASE_DIR / 'static'
]