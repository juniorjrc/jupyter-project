from DAO import MesDAO as m

class Mes():
    def __init__(self, id_mes):
        mes = m.MesDAO()
        self.idMes, self.mes    = mes.getMes(id_mes)
        self.meses              = mes.getTodosMeses()