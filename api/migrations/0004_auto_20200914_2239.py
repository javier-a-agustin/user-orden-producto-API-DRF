# Generated by Django 2.2 on 2020-09-14 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200914_2234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='headerbill',
            name='description',
        ),
        migrations.AddField(
            model_name='headerbill',
            name='description',
            field=models.ManyToManyField(to='api.DescriptionBill'),
        ),
    ]
