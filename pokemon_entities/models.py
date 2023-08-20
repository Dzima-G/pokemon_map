from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, default='Заголовок', verbose_name='Название на русском')
    title_en = models.TextField(max_length=200, default='title', verbose_name='Название на английском')
    title_jp = models.TextField(max_length=200, default='タイトル', verbose_name='Название на японском')
    image = models.ImageField(upload_to='pokemon', null=True, verbose_name='Изображение покемона')
    description = models.TextField(max_length=500, default="Описание", verbose_name='Описание покемона')
    evolution = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='from_evolved',
                                  verbose_name='Эволюция покемона')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    lat = models.FloatField(default=None, verbose_name='Широта')
    lon = models.FloatField(default=None, verbose_name='Долгота')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    appeared_at = models.DateTimeField(default=None, verbose_name='Когда появится')
    disappeared_at = models.DateTimeField(default=None, verbose_name='Когда исчезнет')
    level = models.IntegerField(blank=True, verbose_name='Уровень')
    health = models.IntegerField(blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(blank=True, verbose_name='Сила')
    defence = models.IntegerField(blank=True, verbose_name='Защита')
    stamina = models.IntegerField(blank=True, verbose_name='Выносливость')
