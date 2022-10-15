from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab

# Задаем переменную окружения, содержащую название файла настроек нашего проекта.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StaySharp.settings')
app = Celery('StaySharp')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'report_of_week',
        'schedule': crontab(minute=30, hour=7, day_of_week='monday'),
    },
    # Executes every day at 6:00 a.m.
    'every-day': {
        'task': 'check_registration',
        'schedule': crontab(minute=30, hour=6),
    },
}

app.conf.timezone = "Europe/Kiev"


