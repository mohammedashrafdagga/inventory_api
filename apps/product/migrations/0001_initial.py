# Generated by Django 4.2.1 on 2023-05-15 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255)),
                ("bio", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="media/product_images/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=4)),
                ("quantity", models.PositiveIntegerField(default=1)),
                ("is_active", models.BooleanField(default=True)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="products",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ("-create_at",),
            },
            managers=[
                ("items", django.db.models.manager.Manager()),
            ],
        ),
    ]
