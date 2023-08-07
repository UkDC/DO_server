import os
from pathlib import Path
import dj_database_url
import psycopg2
import django_heroku

USE_TZ = True

TIME_ZONE = "Europe/Kiev"


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "server-insecure-mm7+ac%ujk@w#l_&jhtytytm^0ms(^k*&s)_y%bo6*ntwpm5*f"

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "138.197.183.100", 'stay-sharp.co', 'www.stay-sharp.co', 'https://stay-sharp.co']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'staysharp',
        'USER': 'ip',
        'PASSWORD': 'Mynewdb_pw23',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

