# Generated by Django 4.2.8 on 2023-12-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0004_remove_driver_unique_driver_license_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="driver",
            name="additional_info",
            field=models.CharField(db_index=True, default="", max_length=255),
        ),
    ]
