# Generated by Django 2.1.1 on 2018-12-06 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20181206_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/infrastructure')),
                ('caption', models.CharField(max_length=250)),
            ],
        ),
    ]
