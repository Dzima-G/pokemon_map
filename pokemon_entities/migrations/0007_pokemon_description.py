# Generated by Django 3.1.14 on 2023-08-16 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0006_auto_20230815_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(default='Описание', max_length=1000),
        ),
    ]
