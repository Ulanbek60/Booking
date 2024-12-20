# Generated by Django 5.1.4 on 2024-12-16 16:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0002_country_hotel_address_en_hotel_address_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hotel',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='country_hotel', to='booking_app.country'),
        ),
        migrations.AlterField(
            model_name='hotelimage',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hotel_image', to='booking_app.hotel'),
        ),
    ]
