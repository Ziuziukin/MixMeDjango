# Generated by Django 4.2.7 on 2024-01-08 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_tastes_brand_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tastes",
            name="taste_image",
            field=models.ImageField(
                default="tastes_images/default_taste.jpg", upload_to="tastes_images"
            ),
        ),
    ]