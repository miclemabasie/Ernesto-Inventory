# Generated by Django 4.2.5 on 2023-09-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0006_alter_category_name_alter_product_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated",
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]