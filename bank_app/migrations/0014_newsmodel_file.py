# Generated by Django 4.2.1 on 2023-07-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0013_withdrawmoney_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsmodel",
            name="file",
            field=models.FileField(default=1, upload_to="bank_app/static"),
            preserve_default=False,
        ),
    ]
