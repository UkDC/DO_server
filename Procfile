web: gunicorn StaySharp.wsgi --log-file -
celery: celery -A StaySharp worker --pool=gevent -l info
celery_beat: celery -A StaySharp  beat -l info
