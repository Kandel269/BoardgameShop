# Generated by Django 4.2.7 on 2023-11-30 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0005_remove_game_categories_game_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='games',
            field=models.ManyToManyField(related_name='categories', to='Shop.game'),
        ),
    ]
