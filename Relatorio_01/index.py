#Relatório 1
import os
import sys

class Professor:
    def __init__(self, nome):
        self.nome = nome
    
    def ministrar_aula(self, aula):
        print(f'O professor {self.nome} está ministrando uma aula sobre {aula}.')

class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def presenca(self):
        print(f'O aluno {self.nome} está presente.')

class Aula:
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, alunos):
        self.alunos = []
        self.alunos.append(alunos.nome)

    def listar_presenca(self):
        print(f'Presençana aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}.')

#Processamento
professor = Professor("Lucas")
professor1 = Professor("Renzo")
professor2 = Professor("Jonas")

professor.ministrar_aula("Computação Gráfica")
professor1.ministrar_aula("Programação Orientada a Objetos")
professor2.ministrar_aula("Banco de Dados II")

aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aluno3 = Aluno("Henrique")
aluno4 = Aluno("Julia")
aluno1.presenca()
aluno2.presenca()

aula = Aula(professor, "Computação Gráfica", aluno1)
aula = Aula(professor1, "Programação Orientada a Objetos", aluno2)
aula = Aula(professor2, "Banco de Dados II", aluno3)
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

print(aula.listar_presenca())