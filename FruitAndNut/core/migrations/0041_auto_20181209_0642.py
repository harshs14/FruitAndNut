# Generated by Django 2.1.1 on 2018-12-09 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_auto_20181209_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='universityawards',
            name='percentage_marks',
            field=models.DecimalField(decimal_places=3, max_digits=6),
        ),
    ]
