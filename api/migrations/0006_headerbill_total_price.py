# Generated by Django 2.2 on 2020-09-15 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20200914_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='headerbill',
            name='total_price',
            field=models.FloatField(default=0),
        ),
    ]
