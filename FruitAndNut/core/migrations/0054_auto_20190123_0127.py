# Generated by Django 2.1.1 on 2019-01-23 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0053_auto_20190122_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegeawards',
            name='session',
            field=models.CharField(choices=[(2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2019, max_length=9),
        ),
        migrations.DeleteModel(
            name='AcademicSession',
        ),
    ]
