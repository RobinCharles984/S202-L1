# Código escrito por Tales Machado Prudente
#Estou usando um dataset diferente do disponibilizado, este está com uma pokedex com todas as gerações

from database import Database
from pokedex import Pokedex
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

pokemons = Pokedex.getPokemonByGeneration(1, 151) #Getting first generation of pokemons
writeAJson(pokemons, "pokemons_by_id")

pokemons = Pokedex.getPokemonByName("Charizard")
writeAJson(pokemons, "pokemons_by_name")

pokemons = Pokedex.getPokemonsByHp(80)
writeAJson(pokemons, "pokemons_by_hp")

pokemons = Pokedex.getPokemonsByType(["Grass", "Poison"])
writeAJson(pokemons, "pokemons_by_type")

db.resetDatabase()