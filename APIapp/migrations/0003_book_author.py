# Generated by Django 4.0.2 on 2022-02-20 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0002_alter_category_options_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
