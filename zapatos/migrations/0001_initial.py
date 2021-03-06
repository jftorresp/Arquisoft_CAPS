# Generated by Django 2.2.4 on 2019-10-10 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tallas', '0001_initial'),
        ('fabricantes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zapato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.CharField(max_length=100, null=True)),
                ('tipo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=50)),
                ('tipo_tacon', models.CharField(max_length=50)),
                ('altura_tacon', models.DecimalField(decimal_places=1, max_digits=3)),
                ('altura_suela', models.DecimalField(decimal_places=1, max_digits=3)),
                ('capellada', models.CharField(max_length=50)),
                ('forro', models.CharField(max_length=50)),
                ('plantilla', models.CharField(max_length=50)),
                ('suela', models.CharField(max_length=50)),
                ('ocasion', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('accesorios', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fabricantes.Fabricante')),
                ('talla', models.ManyToManyField(to='tallas.Talla')),
            ],
        ),
    ]
