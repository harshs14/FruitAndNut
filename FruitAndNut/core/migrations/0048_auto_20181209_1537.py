# Generated by Django 2.1.1 on 2018-12-09 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0047_auto_20181209_1537'),
    ]

    operations = [
        migrations.RenameField(
            model_name='universityawards',
            old_name='univ_session',
            new_name='uni_session',
        ),
    ]
