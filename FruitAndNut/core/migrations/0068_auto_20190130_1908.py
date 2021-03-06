# Generated by Django 2.1.1 on 2019-01-30 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0067_auto_20190128_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='file',
            field=models.FileField(default='FruitAndNut/media/files/aicte_approval_letter/2019-01-27/two-scoops-of-django-1-11.pdf', upload_to='files/notification//%Y-%m-%d'),
        ),
        migrations.AlterField(
            model_name='universityawards',
            name='session',
            field=models.CharField(choices=[('2011-2012', '2011-2012'), ('2012-2013', '2012-2013'), ('2013-2014', '2013-2014'), ('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017'), ('2017-2018', '2017-2018'), ('2018-2019', '2018-2019'), ('2019-2020', '2019-2020'), ('2020-2021', '2020-2021'), ('2021-2022', '2021-2022'), ('2022-2023', '2022-2023'), ('2023-2024', '2023-2024')], default=2019, max_length=10, verbose_name='year'),
        ),
    ]
