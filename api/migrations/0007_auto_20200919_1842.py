# Generated by Django 2.2 on 2020-09-19 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_headerbill_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('finalPrice', models.FloatField(default=0)),
                ('createdBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='headerbill',
            name='description',
        ),
        migrations.RemoveField(
            model_name='headerbill',
            name='requested_by',
        ),
        migrations.RemoveField(
            model_name='headerbill',
            name='type_of',
        ),
        migrations.RemoveField(
            model_name='product',
            name='active',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='DescriptionBill',
        ),
        migrations.DeleteModel(
            name='HeaderBill',
        ),
        migrations.DeleteModel(
            name='Type_Bill',
        ),
        migrations.AddField(
            model_name='orderdescription',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderDescription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.OrderDescription'),
        ),
    ]
