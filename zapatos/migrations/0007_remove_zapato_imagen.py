# Generated by Django 2.2.4 on 2019-10-03 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zapatos', '0006_auto_20191003_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zapato',
            name='imagen',
        ),
    ]