# Generated by Django 2.1.1 on 2018-12-09 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/calendar/%Y-%m-%d')),
            ],
            options={
                'verbose_name': 'AcademicCalendar',
                'verbose_name_plural': 'AcademicCalendar',
            },
        ),
        migrations.DeleteModel(
            name='AcademicCalender',
        ),
    ]
