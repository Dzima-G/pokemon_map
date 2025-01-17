# Generated by Django 3.1.14 on 2023-08-14 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0003_auto_20230814_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Appeared_at',
            new_name='appeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Disappeared_at',
            new_name='disappeared_at',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lat',
            new_name='lat',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Lon',
            new_name='lon',
        ),
        migrations.RenameField(
            model_name='pokemonentity',
            old_name='Pokemon',
            new_name='pokemon',
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(blank=True, default=1),
        ),
    ]
