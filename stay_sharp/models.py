from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Create your models here.
def get_superuser():
    su_user = User.objects.filter(
        is_superuser=True).first()  # if you have more than 1 superuser, this get the first in list.
    if su_user:
        return su_user.id
    # raise DoesNotExist('Please add Super User')


class All_knifes(models.Model):
    category = [
        ('low_quality', 'low_quality'),
        ('medium_quality', "medium_quality"),
        ('high_quality', 'high_quality'),
        ('premium_quality', 'premium_quality')
    ]
    brend = models.CharField(max_length=30, blank=True, null=True)
    series = models.CharField(max_length=30, blank=True, null=True)
    steel = models.CharField(max_length=20, blank=True, null=True)
    carbon = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6)], blank=True, null=True)
    CrMoV = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(50)], blank=True, null=True)
    angle = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)], blank=True, null=True)
    honing_add = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=category, default='low_quality')

    class Meta:
        ordering = ['brend']

    def __str__(self):
        if self.brend and self.steel:
            return f'Brend -{self.brend}, steel - {self.steel}'
        elif self.brend and not self.steel:
            return f'Brend -{self.brend}, category - {self.category}'
        else:
            return f'Brend -unknown, steel - {self.steel}'


class Grinding_data(models.Model):
    KJ = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    GA = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)])
    RW = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    C1 = models.FloatField(default=50.0)
    C2 = models.FloatField(default=28.6)
    USH = models.FloatField()


class Honing_data(models.Model):
    KJ = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(200)])
    GA = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)])
    honing_add = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)])
    RW = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    FVB_S = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(130)])
    C3_C4 = models.FloatField(default=128.1)
    C5_C6 = models.FloatField(default=51.4)
    FVB_H = models.FloatField()


class Account_table(models.Model):
    date = models.DateField()
    brend = models.CharField(max_length=30, blank=True, null=True)
    series = models.CharField(max_length=30, blank=True, null=True)
    steel = models.CharField(max_length=20, blank=True, null=True)
    carbon = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(6)], blank=True, null=True)
    CrMoV = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(50)], blank=True, null=True)
    length = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(500)], blank=True, null=True)
    width = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(60)], blank=True, null=True)
    grinding_angle = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(40)], blank=True, null=True)
    honing_add = models.FloatField(blank=True, null=True)
    comments = models.CharField(max_length=200, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_superuser)

    def __str__(self):
        return f'Date - {self.date}'
