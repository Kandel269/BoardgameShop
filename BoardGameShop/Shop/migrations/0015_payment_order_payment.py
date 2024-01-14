# Generated by Django 4.2.7 on 2024-01-14 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0014_deliveryaddress_order_delivery_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='game_images/')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='Shop.payment'),
        ),
    ]