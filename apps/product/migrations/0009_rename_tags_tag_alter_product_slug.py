# Generated by Django 4.2.1 on 2023-05-16 13:51

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("product", "0008_alter_category_slug_alter_product_slug_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Tags",
            new_name="Tag",
        ),
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(
                default=uuid.UUID("c3976c75-f682-471d-954b-b2f2fcd50f24"), unique=True
            ),
        ),
    ]