# Generated by Django 4.2.7 on 2023-11-30 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0007_alter_game_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='published_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
