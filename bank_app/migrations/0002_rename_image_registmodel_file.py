# Generated by Django 4.2.1 on 2023-07-02 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bank_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="registmodel", old_name="image", new_name="file",
        ),
    ]