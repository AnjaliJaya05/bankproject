# Generated by Django 4.2.1 on 2023-07-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0007_rename_ac_no_registmodel_ac"),
    ]

    operations = [
        migrations.CreateModel(
            name="amountwithdraw",
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
                ("amount", models.IntegerField()),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]