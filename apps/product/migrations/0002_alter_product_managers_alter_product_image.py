# Generated by Django 4.2.1 on 2023-05-15 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="product",
            managers=[],
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/product_images/"
            ),
        ),
    ]