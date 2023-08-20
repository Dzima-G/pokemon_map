from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='Заголовок')
    title_en = models.TextField(max_length=200, default='title')
    title_jp = models.TextField(max_length=200, default='タイトル')
    image = models.ImageField(upload_to='pokemon', blank=True, null=True)
    description = models.TextField(max_length=500, default="Описание")
    evolution = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='from_evolved')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField(default=None)
    lon = models.FloatField(default=None)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(default=None)
    disappeared_at = models.DateTimeField(default=None)
    level = models.IntegerField(blank=True)
    health = models.IntegerField(blank=True)
    strength = models.IntegerField(blank=True)
    defence = models.IntegerField(blank=True)
    stamina = models.IntegerField(blank=True)
