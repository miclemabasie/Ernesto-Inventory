# Generated by Django 4.2.3 on 2023-10-03 23:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("settings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="settings",
            name="company_name",
            field=models.CharField(
                blank=True,
                default="SOLIX",
                max_length=255,
                null=True,
                verbose_name="Company Name",
            ),
        ),
        migrations.AlterField(
            model_name="settings",
            name="reoder_default",
            field=models.PositiveIntegerField(
                default=1,
                help_text="Set reorder level for products without reorder level",
                verbose_name="Re-Order Level",
            ),
        ),
        migrations.AlterField(
            model_name="settings",
            name="timezone",
            field=models.CharField(
                blank=True,
                choices=[("Africa/Douala", "Cameroon")],
                default="Africa/Douala",
                max_length=30,
                null=True,
                verbose_name="Timezone",
            ),
        ),
    ]