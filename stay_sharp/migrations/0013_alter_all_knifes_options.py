# Generated by Django 4.1 on 2022-09-01 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("stay_sharp", "0012_alter_all_knifes_brend_alter_all_knifes_series_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="all_knifes", options={"ordering": ["brend"]},
        ),
    ]
