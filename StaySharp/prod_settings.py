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

ALLOWED_HOSTS = ["127.0.0.1", "138.197.183.100", 'stay-sharp.co', ]

CSRF_TRUSTED_ORIGINS = ['https://stay-sharp.co', ]

#SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")

# Включить защищенные куки сессии
SESSION_COOKIE_SECURE = True

# Включить защищенные куки для CSRF-токена
CSRF_COOKIE_SECURE = True

# CORS_ALLOWED_ORIGINS = [ "https://stay-sharp.co",]

# CORS_ALLOW_CREDENTIALS = True

# Если вы хотите разрешить доступ к определенным методам (например, GET, POST, OPTIONS), то укажите их здесь.
# CORS_ALLOW_METHODS = ['GET', 'POST', 'OPTIONS',]

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
