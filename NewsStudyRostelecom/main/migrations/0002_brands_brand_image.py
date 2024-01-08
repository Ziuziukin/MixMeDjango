# Generated by Django 4.2.7 on 2024-01-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="brands",
            name="brand_image",
            field=models.ImageField(
                default="brands_images/default_brand.jpg", upload_to="brands_images"
            ),
        ),
    ]