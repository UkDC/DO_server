# Generated by Django 4.1 on 2022-09-13 17:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stay_sharp", "0022_alter_account_table_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account_table",
            name="CrMoV",
            field=models.FloatField(
                blank=True,
                default="",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(50),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="brend",
            field=models.CharField(blank=True, default="", max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="carbon",
            field=models.FloatField(
                blank=True,
                default="",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(6),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="comments",
            field=models.TextField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="grinding_angle",
            field=models.FloatField(
                blank=True,
                default="",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(40),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="honing_add",
            field=models.FloatField(blank=True, default="", null=True),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="length",
            field=models.FloatField(
                blank=True,
                default="",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(500),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="series",
            field=models.CharField(blank=True, default="", max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="steel",
            field=models.CharField(blank=True, default="", max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name="account_table",
            name="width",
            field=models.FloatField(
                blank=True,
                default="",
                null=True,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(60),
                ],
            ),
        ),
    ]