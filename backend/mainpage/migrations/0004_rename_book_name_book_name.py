# Generated by Django 4.1.7 on 2023-03-16 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mainpage", "0003_rename_name_book_book_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="book_name",
            new_name="name",
        ),
    ]