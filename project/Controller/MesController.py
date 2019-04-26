from Model import Mes as m

class MesController():

    # METODO QUE RETORNA A CONVERSÃO DA TUPLA VINDA DO BANCO EM UMA LISTA DE TODOS OS MESES
    def getTodosMeses(self):
        todosMeses = []
        months = m.Mes(1)
        meses = months.meses
        for i in range(len(meses)):
            todosMeses.append(meses[i][1])

        return todosMeses