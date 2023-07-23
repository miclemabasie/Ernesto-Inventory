# Generated by Django 4.2.3 on 2023-07-23 22:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_product_description_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(
                max_length=250, unique=True, verbose_name="Category"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                max_length=250, unique=True, verbose_name="Product Name"
            ),
        ),
    ]
