
from django.db import models


class Info_table(models.Model):

    date_of_visit = models.DateTimeField()
    visitor_id = models.CharField(max_length=20)
    visitor_name = models.CharField(max_length=20, default=None)
    visitor_IP = models.GenericIPAddressField()
    visitor_email = models.EmailField()
    visitor_tz = models.CharField(max_length=10, default='')
    choose_visits = models.BooleanField(default=False)
    calculation_visits = models.BooleanField(default=False)
    account_table_visits = models.BooleanField(default=False)


