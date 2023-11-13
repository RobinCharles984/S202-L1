#Imports
from database import Database
from game import Game

#Connecting to database
db = Database("bolt://44.211.230.114:7687", "neo4j", "requirements-thickness-balloon")
db.drop_all()

#Creating game CRUD
game = Game(db)

#Messing with the database
game.create_player("xX_Lory_Xx")
game.create_player("CharlesGod")
game.create_player("__kingslayer")
game.create_player("MeTa123")

game.create_match("TDM", "CharlesGod")

game.update_player("MeTa123", "Shrekota")

game.insert_player_in_match("__kingslayer", "TDM")
game.insert_player_in_match("Shrekota", "TDM")
game.insert_player_in_match("xX_Lory_Xx", "TDM")

game.delete_player("xX_Lory_Xx")

#Closing database
db.close()