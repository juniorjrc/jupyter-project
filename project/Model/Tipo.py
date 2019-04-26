from DAO import TipoDAO as t

class Tipo():
    def __init__(self, id_tipo):
        tipo = t.TipoDAO()
        self.idTipo, self.nomeTipo  = tipo.getTipo(id_tipo)
        self.tipos                  = tipo.getTodosTipos()