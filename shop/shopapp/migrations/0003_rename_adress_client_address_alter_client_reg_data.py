# Generated by Django 5.0.3 on 2024-03-28 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_alter_item_price_alter_order_date_remove_order_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='adress',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='client',
            name='reg_data',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]