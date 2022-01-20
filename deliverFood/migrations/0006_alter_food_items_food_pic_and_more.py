# Generated by Django 4.0.1 on 2022-01-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliverFood', '0005_alter_food_items_food_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_items',
            name='food_pic',
            field=models.ImageField(height_field='200', upload_to='the_uploaded_images', width_field='200'),
        ),
        migrations.AlterField(
            model_name='food_items',
            name='food_price',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
