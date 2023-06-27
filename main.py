import copy
import random
from Grafo import Graph, Escola, Professor
#Lê o arquivo com todas as Escolas
arquivo_escolas = open("Escolas.txt")
escolas = arquivo_escolas.read().split("\n")
lista_escolas = []

for linha in escolas:
    linha = linha.split(":")
    lista_escolas.append(linha)

#Lê o arquivo com todos os Profesores
arquivo_professores = open("Professores.txt")
professores = arquivo_professores.read().split("\n")

lista_professores = []

for linha in professores:
    linha = linha.split(":")
    lista_professores.append(linha)

#Montando o Grafo
grafo = Graph()
#['(P98, 2)', ' (E4, E48, E1)']
for professor in lista_professores:
    id = professor[0][0]
    com = professor[0][1]
    pref = professor[1]
    grafo.addProfessor(id, com, pref)

for professor in grafo.professores:
    print(professor)
    print(professor.id, professor.competencias, professor.preferencia)
