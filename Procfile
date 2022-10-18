gunicorn StaySharp.wsgi --log-file -
celery -A StaySharp worker --pool=gevent -l info
celery -A StaySharp  beat -l info
