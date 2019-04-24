from DAO import CidadeDAO as c

class Cidade():
    def __init__(self, id_cidade):
        cidade = c.CidadeDAO()
        self.idCidade, self.cidade  = cidade.getCidade(id_cidade)
        self.cidades                = cidade.getTodasCidades()