# Generated by Django 4.2.7 on 2023-12-02 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brands",
            name="desc_brand",
            field=models.TextField(max_length=2000, verbose_name="Описание бренда"),
        ),
    ]