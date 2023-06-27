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
    id = professor[0].strip("() ").split(",")[0]
    com = professor[0].strip("() ").split(",")[1]
    pref = []
    for n in professor[1].strip("() ").split(","):
        pref.append(n.strip(" "))

    grafo.addProfessor(id, int(com.strip(" ")), pref)


#(E24):(3):(1)
for escola in lista_escolas:
    id = escola[0]
    id = id.strip("() ")
    vagas = []
    for n in escola[1:]:
        vagas.append(int(n.strip("() ")))

    grafo.addEscola(id, vagas)
"""
for x in grafo.professores:
    print(f'{x.id} | {x.competencias} | {x.preferencias}')

for x in grafo.escolas:
    print(f"{x.id} | {x.vagas}")
"""

for escola in grafo.escolas:
    for professor in grafo.professores:
       #Professor aceita a escola?
        if escola.id in professor.preferencias:          
            
            for vaga in escola.vagas:
                #Escola aceita o professor?
                if professor.competencias >= vaga:

                    #A escola não tem professores?
                    if len(escola.professores) == 0:
                        escola.addProfessor(professor)


                    #O professor é mais capacitado que o atual?
                    elif professor.competencias > vaga:
                        escola.SubProfessor(professor)
                        
                    #O professor quer mais a escola?
                    elif professor.competencias == vaga:
                        



for escola in grafo.escolas:
    print(escola.professores)