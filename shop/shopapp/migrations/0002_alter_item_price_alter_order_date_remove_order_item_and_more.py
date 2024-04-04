# Generated by Django 5.0.3 on 2024-03-28 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.RemoveField(
            model_name='order',
            name='item',
        ),
        migrations.AlterField(
            model_name='order',
            name='total_sum',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='shopapp.item'),
        ),
    ]