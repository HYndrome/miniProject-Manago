# Generated by Django 3.2.18 on 2023-05-03 01:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
        ('restaurants', '0004_restaurant_first_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='first_review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_set', to='reviews.review'),
        ),
    ]