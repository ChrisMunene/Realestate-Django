# Generated by Django 3.0.7 on 2020-06-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20200613_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
