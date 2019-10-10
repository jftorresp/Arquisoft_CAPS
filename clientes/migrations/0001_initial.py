# Generated by Django 2.2.4 on 2019-10-07 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('correo', models.CharField(max_length=100)),
                ('contrasena', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100, null=True)),
                ('ciudad', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]