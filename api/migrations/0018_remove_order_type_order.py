# Generated by Django 2.2 on 2020-09-21 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200920_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='type_order',
        ),
    ]
