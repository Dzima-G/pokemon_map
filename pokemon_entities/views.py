import folium
import json

from django.shortcuts import render
from pokemon_entities.models import Pokemon, PokemonEntity
from django.utils import timezone
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    local_time = timezone.localtime(timezone.now())
    pokemons_entity = PokemonEntity.objects.filter(appeared_at__lt=local_time, disappeared_at__gt=local_time)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entity:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            image_url=request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons = Pokemon.objects.all()
    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.image:
            pokemons_on_page.append({
                'pokemon_id': pokemon.id,
                'img_url': pokemon.image.url,
                'title_ru': pokemon.title_ru,
            })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    requested_pokemon = get_object_or_404(PokemonEntity, id=pokemon_id)
    pokemon = {
        'title_en': requested_pokemon.pokemon.title_en,
        'title_ru': requested_pokemon.pokemon.title_ru,
        'title_jp': requested_pokemon.pokemon.title_jp,
        'pokemon_id': requested_pokemon.id,
        'img_url': request.build_absolute_uri(requested_pokemon.pokemon.image.url),
        'description': requested_pokemon.pokemon.description,
    }
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    add_pokemon(
        folium_map,
        requested_pokemon.lat,
        requested_pokemon.lon,
        image_url=request.build_absolute_uri(requested_pokemon.pokemon.image.url)
    )

    if requested_pokemon.pokemon.previous_evolution:
        from_evolved = requested_pokemon.pokemon.previous_evolution
        pokemon['previous_evolution'] = {
            "title_ru": from_evolved.title_ru,
            "pokemon_id": from_evolved.id,
            "img_url": request.build_absolute_uri(from_evolved.image.url),
        }

    from_evolved = requested_pokemon.pokemon.from_evolved.first()
    if from_evolved:
        pokemon['next_evolution'] = {
            "title_ru": from_evolved.title_ru,
            "pokemon_id": from_evolved.id,
            "img_url": request.build_absolute_uri(from_evolved.image.url),
        }

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
