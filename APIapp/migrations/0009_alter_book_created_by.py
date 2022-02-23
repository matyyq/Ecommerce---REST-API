# Generated by Django 4.0.2 on 2022-02-23 22:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APIapp', '0008_alter_product_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
