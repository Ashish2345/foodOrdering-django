# Generated by Django 4.0.1 on 2022-03-07 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_note',
            field=models.TextField(blank=True),
        ),
    ]
