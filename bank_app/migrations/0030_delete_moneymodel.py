# Generated by Django 4.2.1 on 2023-10-04 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0029_wishlist_uid"),
    ]

    operations = [
        migrations.DeleteModel(name="moneymodel",),
    ]