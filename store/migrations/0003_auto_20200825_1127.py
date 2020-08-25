# Generated by Django 3.1 on 2020-08-25 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
