# Generated by Django 2.1.1 on 2018-12-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_merge_20181207_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='principal',
            name='image',
            field=models.ImageField(upload_to='images/principal'),
        ),
    ]
