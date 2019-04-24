from DAO import NaturezaDAO as n

#OBJETO NATUREZA
class Natureza():
    def __init__(self, id_natureza):
        #INSTÂNCIA DA BUSCA NA BASE DE DADOS
        naturezaDAO = n.NaturezaDAO()
        self.idNatureza, self.nomeNatureza, self.descricaoNatureza  = naturezaDAO.getNatureza(id_natureza) #ID DA NATUREZA, NOME NATUREZA E DESCRIÇÃO NATUREZA
        self.naturezas                                              = naturezaDAO.getTodasNaturezas() #TODAS AS NATUREZAS

