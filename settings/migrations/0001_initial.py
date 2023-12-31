# Generated by Django 4.2.3 on 2023-07-14 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Settings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="settings",
                        verbose_name="Site Logo",
                    ),
                ),
                (
                    "company_name",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Company Name",
                    ),
                ),
                (
                    "timezone",
                    models.CharField(
                        blank=True, max_length=30, null=True, verbose_name="Timezone"
                    ),
                ),
                (
                    "reoder_default",
                    models.PositiveIntegerField(
                        help_text="Set reorder level for products without reorder level",
                        verbose_name="Re-Order Level",
                    ),
                ),
            ],
        ),
    ]
