# Generated by Django 2.1.1 on 2018-10-09 01:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20181009_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='importantfunctionary',
            name='phone_number',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number without zero and having 10 numbers', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='importantfunctionary',
            name='telephone',
            field=models.CharField(blank=True, max_length=12, null=True, validators=[django.core.validators.RegexValidator(message='Format:XXXX-XXXXXXX', regex='^d{4}([-]*)\\d{7}$')]),
        ),
    ]
