# Generated by Django 4.1 on 2022-08-23 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stay_sharp", "0007_alter_all_knifes_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="all_knifes",
            name="brend",
            field=models.CharField(
                blank=True, default="unknown", max_length=15, null=True
            ),
        ),
        migrations.AlterField(
            model_name="all_knifes",
            name="series",
            field=models.CharField(
                blank=True, default="unknown", max_length=15, null=True
            ),
        ),
        migrations.AlterField(
            model_name="all_knifes",
            name="steel",
            field=models.CharField(
                blank=True, default="unknown", max_length=10, null=True
            ),
        ),
    ]
