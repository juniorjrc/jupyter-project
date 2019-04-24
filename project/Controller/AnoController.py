from Model import Ano as a

class AnoController():

    # METODO QUE RETORNA A CONVERSÃO DA TUPLA VINDA DO BANCO EM UMA LISTA DE TODOS OS ANOS
    def getTodosAnos(self):
        todosAnos = []
        years = a.Ano(1)
        anos = years.anos
        for i in range(len(anos)):
            todosAnos.append(anos[i][1])
        
        return todosAnos