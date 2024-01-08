# Generated by Django 4.2.7 on 2024-01-08 13:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("birthdate", models.DateField(null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("М", "Мужской"),
                            ("Ж", "Женский"),
                            ("НД", "Нет данных"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "account_image",
                    models.ImageField(
                        default="account_images/default_user.jpg",
                        upload_to="account_images",
                    ),
                ),
            ],
        ),
    ]
