# Generated by Django 5.1.4 on 2024-12-22 09:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_book_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.category'),
        ),
    ]
