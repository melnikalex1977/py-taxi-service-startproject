# Generated by Django 4.2.8 on 2023-12-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("taxi", "0003_remove_driver_unique_driver_license_number_and_more"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="driver",
            name="unique_driver_license_number",
        ),
        migrations.AddField(
            model_name="driver",
            name="additional_info",
            field=models.CharField(db_index=True, default=0, max_length=255),
        ),
        migrations.AddConstraint(
            model_name="driver",
            constraint=models.UniqueConstraint(
                fields=("license_number", "password", "additional_info"),
                name="unique_driver_license_number",
            ),
        ),
    ]
