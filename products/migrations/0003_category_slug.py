# Generated by Django 4.2.3 on 2023-07-14 21:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_category_updated"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(blank=True, null=True, verbose_name="Category Slug"),
        ),
    ]
