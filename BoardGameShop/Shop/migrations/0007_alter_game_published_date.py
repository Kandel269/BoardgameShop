# Generated by Django 4.2.7 on 2023-11-30 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0006_remove_game_category_category_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
