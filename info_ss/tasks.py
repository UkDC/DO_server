from django.contrib.auth.models import User
from datetime import date, timedelta, datetime
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from StaySharp.celery_tasks import app
from StaySharp.settings import EMAIL_HOST_USER
from .models import Info_table
from django.db.models import Max, Avg, Min, Sum
from django.utils import timezone


# отправка писем уведомлений
@app.task()
def send_email_to_user(message, email):
    email = EmailMessage('Notice', message, to=[email])
    email.send()


# проверка аккаунтов, предупреждение через сутки, удаление через 3 суток
@app.task(name='check_registration')
def check_registration():
    for user in User.objects.all():
        delta = timezone.now() - user.date_joined
        date_expired = user.date_joined + timedelta(days=3)
        if not user.is_active:
            context = {'username': user.username, 'date_registration': user.date_joined.date(),
                       'date_expired': date_expired}
            email = user.email
            if delta.days >= 3:
                message = render_to_string('email_to_user/email_del.html', context=context)
                send_email_to_user.delay(message, email)
                user.delete()
            else:
                message = render_to_string('email_to_user/emai_reminding.html', context=context)
                send_email_to_user.delay(message, email)


@app.task(name='report_of_week')
def report_of_week():

    visitors_num = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).count()
    most_visitor = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).aggregate(Max('visitor_name'))['visitor_name__max']
    visits_of_most_visitor = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).filter(visitor_name=most_visitor).count()
    choose_visits = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).filter(choose_visits=True).count()
    calculation_visits = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).filter(calculation_visits=True).count()
    account_table_visits = Info_table.objects.filter(date_of_visit__gt=timezone.now()-timedelta(days=7)).filter(account_table_visits=True).count()

    context = {
        'visitors_num': visitors_num,
        'most_visitor': most_visitor,
        'visits_of_most_visitor': visits_of_most_visitor,
        'choose_visits': choose_visits,
        'calculation_visits': calculation_visits,
        'account_table_visits': account_table_visits,
    }
    message = render_to_string('email_info/email_report_week.html', context=context)
    send_email_to_user.delay(message, email=EMAIL_HOST_USER)

