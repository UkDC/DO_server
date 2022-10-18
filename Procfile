web: gunicorn StaySharp.wsgi --log-file -
celery: celery -A StaySharp worker -l info
celery_beat: celery -A StaySharp  beat -l info