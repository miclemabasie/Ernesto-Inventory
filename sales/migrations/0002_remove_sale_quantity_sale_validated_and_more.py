# Generated by Django 4.2.3 on 2023-07-14 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sale",
            name="quantity",
        ),
        migrations.AddField(
            model_name="sale",
            name="validated",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="sale",
            name="total_sale_price",
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
