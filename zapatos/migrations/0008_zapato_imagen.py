# Generated by Django 2.2.4 on 2019-10-08 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zapatos', '0007_remove_zapato_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapato',
            name='imagen',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
