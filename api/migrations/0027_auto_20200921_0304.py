# Generated by Django 2.2 on 2020-09-21 03:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20200921_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdescription',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
    ]
