# Generated by Django 2.1.1 on 2018-12-09 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20181209_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_awards_session', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Academic Award',
                'verbose_name_plural': 'Academic Awards',
            },
        ),
        migrations.CreateModel(
            name='UniversityAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('univ_position', models.IntegerField()),
                ('branch', models.CharField(max_length=255)),
                ('percentage_marks', models.DecimalField(decimal_places=3, max_digits=6)),
                ('medal', models.CharField(max_length=255)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Awards')),
            ],
        ),
    ]
