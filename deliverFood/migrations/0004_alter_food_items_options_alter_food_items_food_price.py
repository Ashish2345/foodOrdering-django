# Generated by Django 4.0.1 on 2022-01-19 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverFood', '0003_food_items'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food_items',
            options={'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AlterField(
            model_name='food_items',
            name='food_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
