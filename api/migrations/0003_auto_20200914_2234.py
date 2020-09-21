# Generated by Django 2.2 on 2020-09-14 22:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200913_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='DescriptionBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
        ),
        migrations.CreateModel(
            name='HeaderBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DescriptionBill')),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('type_of', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Type_Bill')),
            ],
        ),
        migrations.DeleteModel(
            name='Bill',
        ),
    ]
