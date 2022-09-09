# Generated by Django 3.2.6 on 2022-09-09 06:35

import Inventory.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0002_rename_issue_to_inventory_medicine_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Net_price',
            field=models.FloatField(blank=True, default='0.0', null=True, verbose_name='Net Price(Rs.)'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='Product_ID',
            field=models.CharField(blank=True, default=Inventory.utils.create_new_ref_number, max_length=12),
        ),
    ]