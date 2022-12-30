import pytest
import app.scrap_pokemon_data as scrap
import app.constants as cst

def test_pokemon_names_are_retrieved():
    pokemon_data = scrap.retrieve_pokemon_names_from_pokebip()
    assert len(pokemon_data) == cst.NB_POKEMON_2G
    assert pokemon_data[0] == 'Bulbizarre'
    assert pokemon_data[cst.NB_POKEMON_2G - 1] == 'Celebi'
    assert pokemon_data[129] == 'Léviator'
