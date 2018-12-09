# Generated by Django 2.1.1 on 2018-12-09 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20181209_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeAwards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('branch', models.CharField(max_length=255)),
                ('percentage_marks', models.DecimalField(decimal_places=3, max_digits=6)),
            ],
        ),
        migrations.AlterField(
            model_name='awards',
            name='uni_session',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='collegeawards',
            name='colg_session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Awards'),
        ),
    ]
