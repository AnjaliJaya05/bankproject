# Generated by Django 4.2.1 on 2023-07-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0002_rename_image_registmodel_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="registmodel",
            name="file",
            field=models.FileField(upload_to="bank_app/static"),
        ),
    ]
