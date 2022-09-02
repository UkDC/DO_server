from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

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
    C5_C6= models.FloatField(default=51.4)
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
    comments = models.CharField(max_length=100)

    def __str__(self):
        return f'Date - {self.date}'


