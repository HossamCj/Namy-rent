# Generated by Django 3.2.6 on 2021-09-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertybook',
            name='children_numbers',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2),
        ),
        migrations.AlterField(
            model_name='propertybook',
            name='guest_numbers',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], max_length=2),
        ),
    ]
