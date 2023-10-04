#Imports
import pymongo
from database import Database
from motoristaCli import MotoristaCRUD
from motoristaDao import MotoristaDAO

db = Database.connect(database="relatorio_avaliativo_01", collection="motorista")

#Classes
class Passageiro:
    def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = Passageiro

class Motorista:
    def __init__(self, corridas: [Corrida], nota: int):
        self.corridas = Corrida
        self.nota = nota

motoristaDAO = MotoristaDAO(database=db)

motoristaCLI = MotoristaCRUD(motoristaDAO)
motoristaCLI.run()