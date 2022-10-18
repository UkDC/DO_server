web: gunicorn StaySharp.wsgi --log-file -
celery: celery -A StaySharp worker --pool=gevent -l info
django-celery-beat: celery -A StaySharp  beat -l info
