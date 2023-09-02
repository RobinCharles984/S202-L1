from database import Database

db = Database(database="pokedex", collection="pokemons")

class Pokedex:
    def __init__(self, database: Database):
        _database = Database

    def getPokemonByGeneration(start: int, end: int):
        return db.collection.find({"id": {"$gte": start, "$lte": end}})
    
    def getPokemonByName(name: str):
        return db.collection.find({"name.english": name})
    
    def getPokemonsByType(types: list):
        return db.collection.find({"type": {"$in": types}})
    
    def getPokemonsByHp(hp: int):
        return db.collection.find({"base.HP": hp})
    
