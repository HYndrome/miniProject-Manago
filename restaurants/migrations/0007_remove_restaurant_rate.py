# Generated by Django 3.2.18 on 2023-05-02 01:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurant_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='rate',
        ),
    ]
