source /home/ip/venv/bin/activate
exec gunicorn StaySharp.wsgi:application --bind 127.0.0.1:8000 2>> /home/ip/DO_server/logs/gunicorn.log