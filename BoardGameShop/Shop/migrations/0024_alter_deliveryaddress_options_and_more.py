# Generated by Django 4.2.7 on 2024-01-21 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0023_personaldata_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deliveryaddress',
            options={'verbose_name': 'Delivery Address', 'verbose_name_plural': 'Delivery Address'},
        ),
        migrations.AlterModelOptions(
            name='personaldata',
            options={'verbose_name': 'Personal Data', 'verbose_name_plural': 'Personal Data'},
        ),
        migrations.AddField(
            model_name='deliveryaddress',
            name='city',
            field=models.CharField(default='a', max_length=255),
            preserve_default=False,
        ),
    ]
