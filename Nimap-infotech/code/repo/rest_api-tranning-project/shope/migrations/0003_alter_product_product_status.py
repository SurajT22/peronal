# Generated by Django 4.1 on 2022-08-20 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shope', '0002_productstatus_product_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('New', 'New'), ('Processed', 'Processed')], default='New', max_length=100),
        ),
    ]
