# Generated by Django 4.2.1 on 2023-09-07 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0027_remove_wishlist_newsid_remove_wishlist_uid"),
    ]

    operations = [
        migrations.AddField(
            model_name="wishlist",
            name="newsid",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
