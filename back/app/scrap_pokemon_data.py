import requests
from bs4 import BeautifulSoup

def retrieve_pokemon_names_from_pokebip():
  URL = "https://www.pokebip.com/pokedex/or-argent"
  page = requests.get(URL)
  soup = BeautifulSoup(page.content, "html.parser")
  tbody = soup.tbody
  pokemon_data = []
  for tr in tbody.find_all("tr"):
    pokemon_name = tr.find_all("td")[1].strong.a.string
    pokemon_data.append(pokemon_name)
  return pokemon_data
