# Generated by Django 4.1.1 on 2022-10-23 01:33

import Inventory.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_merge_20221012_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='Product_ID',
            field=models.CharField(blank=True, default=Inventory.utils.create_new_ref_number, max_length=13),
        ),
    ]
