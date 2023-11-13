#Imports
from query import Database
from teacher import TeacherCRUD

#Connecting database
db = Database("bolt://44.211.230.114:7687", "neo4j", "requirements-thickness-balloon")
db.drop_all()

teacher = TeacherCRUD(db) #Creating teacher crud

##Exercicio 3##
#Questao B
teacher.create_teacher("Chris Lima", 1956, '189.052.396-66')

#Questao C
teacher.read_teacher("Chris Lima")

#Questao D
teacher.update_teacher("Chris Lima", '162.052.777-77')

#Close database
db.close()