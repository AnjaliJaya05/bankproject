# Generated by Django 4.2.1 on 2023-09-07 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0028_wishlist_newsid"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="uid",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
