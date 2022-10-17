# Generated by Django 4.0.8 on 2022-10-16 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_ss', '0005_alter_info_table_date_of_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_table',
            name='visitor_IP',
            field=models.GenericIPAddressField(default='unknown'),
        ),
        migrations.AlterField(
            model_name='info_table',
            name='visitor_email',
            field=models.EmailField(default='unknown', max_length=254),
        ),
        migrations.AlterField(
            model_name='info_table',
            name='visitor_id',
            field=models.CharField(default='AnonymousUser', max_length=20),
        ),
        migrations.AlterField(
            model_name='info_table',
            name='visitor_name',
            field=models.CharField(default='AnonymousUser', max_length=20),
        ),
    ]