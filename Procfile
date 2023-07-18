web: gunicorn StaySharp.wsgi --log-file -
celery: celery -A StaySharp worker --pool=gevent -l
beat: celery -A StaySharp  beat -l
