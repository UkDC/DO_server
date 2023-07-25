import os
from pathlib import Path
import dj_database_url
import psycopg2
import django_heroku

USE_TZ = True

TIME_ZONE = "Europe/Kiev"


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "server-insecure-mm7+ac%ujk@w#l_&jhtytytm^0ms(^k*&s)_y%bo6*ntwpm5*f"

DEBUG = False

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'StaySharp',
        'USER': 'postgres',
        'PASSWORD': 'Mynewdb_pw23',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')