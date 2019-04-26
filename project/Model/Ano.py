from DAO import AnoDAO as a

class Ano():
    def __init__(self, id_ano):
        ano = a.AnoDAO()
        self.idAno, self.ano    = ano.getAno(id_ano)
        self.anos               = ano.getTodosAnos()