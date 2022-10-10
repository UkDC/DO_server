import os
from celery import Celery

# Задаем переменную окружения, содержащую название файла настроек нашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StaySharp.settings')
app = Celery('StaySharp')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


