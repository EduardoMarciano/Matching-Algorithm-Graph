# Implementação do Grafo e do Vêrtice com a utilização de POO  

class Graph:
    def __init__(self):
        self.professores = []
        self.escolas = []
        
    def addProfessor(self, id, comp, pref):
        newVertex = Professor(id, comp, pref)
        self.professores.append(newVertex)

    def addEscola(self, id, vagas):
        newVertex = Escola(id, vagas)
        self.escolas.append(newVertex)
        
class Professor:
    def __init__(self,id, comp, pref):
        self.id = id
        self.competencias = comp
        self.preferencias = pref

class Escola:
    def __init__(self, id, vagas):
        self.id = id
        self.vagas = vagas
        self.professores = []

        