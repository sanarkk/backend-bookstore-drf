# Generated by Django 4.1.7 on 2023-06-01 02:25

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("mainpage", "0002_order_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=16,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must be "
                                "entered in the format '+123456789'"
                                ". Up to 15 digits allowed.",
                        regex="^\\+?1?\\d{9,15}$",
                    )
                ],
            ),
        ),
        migrations.CreateModel(
            name="MyUser",
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
                (
                    "language",
                    models.CharField(
                        choices=[("UA", "Ukrainian"), ("EN", "English")],
                        default="EN",
                        max_length=2,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]