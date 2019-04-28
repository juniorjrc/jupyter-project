from Model import Natureza as n

class NaturezaController:

    # METODO QUE RETORNA A CONVERSÃO DA TUPLA VINDA DO BANCO EM UMA LISTA DE TODOS OS NOMES DAS NATUREZAS
    def getTodasNaturezas(self):
        todasNaturezasProdutividade = []
        todasNaturezasOcorrencias = []
        natures = n.Natureza(1)
        naturezas = natures.naturezas

        #BUSCA TODAS AS NATUREZAS POR PRODUTIVIDADE
        for i in range(12):
            todasNaturezasProdutividade.append(naturezas[i][1])

        #BUSCA TODAS AS NATUREZAS POR OCORRENCIAS
        for i in range(23):
            todasNaturezasOcorrencias.append(naturezas[i+12][1])
        
        return todasNaturezasProdutividade, todasNaturezasOcorrencias
    