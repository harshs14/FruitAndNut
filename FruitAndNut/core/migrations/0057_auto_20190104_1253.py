# Generated by Django 2.1.1 on 2019-01-04 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_remove_universityawards_branch'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='centerofexcellence',
            options={'verbose_name': 'Center Of Excellence', 'verbose_name_plural': 'Center Of Excellence'},
        ),
        migrations.RemoveField(
            model_name='trainingplacementdepartment',
            name='email',
        ),
    ]
