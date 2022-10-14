web: gunicorn StaySharp.wsgi --log-file -
celery: celery -A StaySharp worker --without-heartbeat --without-gossip --without-mingle
beat: celery -A StaySharp  beat
