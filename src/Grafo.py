# Implementação do Grafo e do Vêrtice com a utilização de POO  

class Graph:
    def __init__(self):
        self.professores = []
        self.escolas = []
        self.estavel = False
        
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
        self.escola = None

    def addEscola(self, escola):
        self.escola = escola

    def compEscola(self, escola):
        atual = preferencias.index(self.escola.id)
        nova  = preferencias.index(escola.id)
        if nova < atual:
            self.escola = escola
            self.escola.addProfessor(self)

class Escola:
    def __init__(self, id, vagas):
        self.id = id
        self.vagas = vagas
        self.professores = []
    
    def addProfessor(self, professor):
        self.professores.append(professor)
    
    def SubProfessor(self):
        self.professores = sorted(self.professores,  key=lambda professor: professor.competencias, reverse=True)
        self.professores.pop()

        