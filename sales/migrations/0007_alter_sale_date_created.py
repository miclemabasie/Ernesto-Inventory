# Generated by Django 4.2.5 on 2023-09-22 15:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sales", "0006_alter_sale_date_created"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="date_created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]