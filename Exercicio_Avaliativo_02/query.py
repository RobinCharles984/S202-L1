#Classe Database
from neo4j import GraphDatabase

class Database:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))
    
    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data
    
    def drop_all(self):
        with self.driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

#Classe para Query
class Questao_1:
    def __init__(self, database):
        self.db = database
    
    def questao_a(self):
        query = "MATCH (p:Professor {name: Renzo}) RETURN p.ano_nasc AND p.cpf"
        parameters = {"name": "Renzo"}
        self.db.execute_query(query, parameters)
    
    def questao_b(self):
        query = "MATCH (p:Professor) WHERE p STARTS WITH 'M' return p.name AND p.cpf" 
        self.db.execute_query(query, None)

    def questao_c(self):
        query = "MATCH (c:City) RETURN c.name"
        self.db.execute_query(query, None)

    def questao_d(self):
        query = "MATCH (s:School) WHERE s.number >= 150 OR s.number <= 550 RETURN s.name AND s.adress AND s.number"

class Questao_2:
    def __init__(self, database):
        self.db = database

    def questao_a(self):
        query = "MATCH (p:Professor) RETURN p.ano_nasc.max() AND p.ano_nasc.min()"
        self.db.execute_query(query, None)

    def questao_b(self):
        query = "MATCH (c:City) RETURN c.population.avg()"
        self.db.execute_query(query, None)

    def questao_c(self):
        query = "MATCH (c:City) WHERE c.cep = 37540-000 RETURN c.name"

    def questao_d(self):
        query = "MATCH (p:Professor) RETURN p.name"