# Generated by Django 4.2.1 on 2023-09-07 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0026_moneymodel"),
    ]

    operations = [
        migrations.RemoveField(model_name="wishlist", name="newsid",),
        migrations.RemoveField(model_name="wishlist", name="uid",),
    ]
