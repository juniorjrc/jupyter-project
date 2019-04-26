# DAO
from DAO import OcorrenciaDAOBean as odb
ocorrenciaDaoBean = odb.Ocorrencia()

# CONTROLLERS
from Controller import AnoController as ac
from Controller import MesController as mc
anoController = ac.AnoController()
mesController = mc.MesController()

# MODELS
from Model import Ano as a
from Model import Mes as m
from Model import Tipo as t
from Model import Cidade as c
from Model import Natureza as n

# GRÁFICO
from Graphic import Graph as g
grafico = g.Graph()

class OcorrenciaController():

    #ESTE MÉTODO RETORNA O GRÁFICO COMPARATIVO DE TODAS AS OCORRÊNCIAS DE ACORDO COM O PERÍODO EX.: OCORRENCIAS DO ANO 2017, 2018 E 2019
    def consultaSomatorioTodasOcorrenciasPeriodo(self,id_cidade, id_tipo):
        tipo = t.Tipo(id_tipo)
        cor = self.verificaCor(id_tipo)
        cidade = c.Cidade(id_cidade)

        todosAnos = anoController.getTodosAnos()
        somatorioOcorrencias = []

        #PERCORRE O SOMATÓRIO DE TODAS OCORRENCIAS NO PERIODO QUE CONSTA NO BANCO
        for i in range(len(todosAnos)):
            somatorioOcorrencias.append(int(ocorrenciaDaoBean.getSomatorioTodasOcorrenciasPorAno(i + 1, cidade.idCidade, tipo.idTipo)))

        #PLOTA O GRÁFICO
        grafico.plotGraph(
            "Gráfico do número de ocorrências filtradas por " + str(tipo.nomeTipo) + "\nno período de 2017 a Fevereiro de 2019",
            "Anos",
            "Somatório dos registros",
            todosAnos,
            somatorioOcorrencias,
            cor,
            "bar",
            "Images/consultaSomatorioTodasOcorrenciasPeriodo_" + str(tipo.nomeTipo) + ".png"
            )
    
    #ESTE MÉTODO RETORNA O GRÁFICO COMPARATIVO DE TODAS OCORRÊNCIAS DURANTE UM MÊS ESPECÍFICO NO PERIODO DE 2017 A 2019
    def consultaSomatorioTodasOcorrenciasMes(self, id_mes, id_cidade, id_tipo):
        cor = self.verificaCor(id_tipo)

        tipo = t.Tipo(id_tipo)
        mes = m.Mes(id_mes)
        cidade = c.Cidade(id_cidade)

        todosAnos = anoController.getTodosAnos()
        ocorrenciasMes = []

        #PERCORRE O SOMATÓRIO DE TODAS OCORRÊNCIAS DURANTE UM DETERMINADO MÊS
        for i in range(len(todosAnos)):
            ocorrencias = ocorrenciaDaoBean.getSomatoriotOcorrenciasPorMes(mes.idMes, str(i + 1), cidade.idCidade, tipo.idTipo)
            if ocorrencias != None:
                ocorrenciasMes.append(int(ocorrencias))
            else:
                ocorrenciasMes.append(0)
                
        
        #PLOTA O GRÁFICO
        grafico.plotGraph(
            "Gŕafico do número de ocorrências filtradas por " + str(tipo.nomeTipo) + "\nno mês de " + str(mes.mes) + " no período de 2017 a Fevereiro de 2019",
            "Anos",
            "Somatório dos registros",
            todosAnos,
            ocorrenciasMes,
            cor,
            "bar",
            "Images/consultaSomatorioTodasOcorrenciasMes_" + str(tipo.nomeTipo) + ".png"
        )

    #ESTE METÓDO CONSULTA O SOMATÓRIO DE UMA DETERMINADA OCORRÊNCIA NO PERÍODO DE 2017 A 2019
    def consultaSomatorioUmaOcorrenciaPeriodo(self, id_natureza, id_cidade, id_tipo):
        cor = self.verificaCor(id_tipo)

        tipo = t.Tipo(id_tipo)
        natureza = n.Natureza(id_natureza)
        cidade = c.Cidade(id_cidade)

        todosAnos = anoController.getTodosAnos()
        ocorrenciaAno = []

        #PERCORRE O SOMATÓRIO DE UMA DETERMINADA OCORRÊNCIA DURANTE O PERÍODO DE 2017 A 2019
        for i in range(len(todosAnos)):
            ocorrencias = ocorrenciaDaoBean.getSomatorioOcorrenciaPorAno(natureza.idNatureza, i + 1, cidade.idCidade, tipo.idTipo)
            if ocorrencias != None:
                ocorrenciaAno.append(int(ocorrencias))
            else:
                ocorrenciaAno.append(0)
        
        #PLOTA O GRÁFICO
        grafico.plotGraph(
            "Gŕafico do somatório dos registros de \n" + str(natureza.nomeNatureza) + " filtrada por " + str(tipo.nomeTipo) + "\nno período de 2017 a Fevereiro de 2019",
                "Anos",
                "Somatório dos registros de \n" + str(natureza.nomeNatureza),
                todosAnos,
                ocorrenciaAno,
                cor,
                "bar",
                "Images/consultaSomatorioUmaOcorrenciaPeriodo_" + str(tipo.nomeTipo) + ".png"
        )

    #ESTE MÉTODO MOSTRA OS REGISTROS DE UMA OCORRÊNCIA DURANTE TODOS OS MESES DE UM DETERMINADO ANO
    def consultaOcorrenciaMesAno(self, id_natureza, id_cidade, id_ano, id_tipo):
        cor = self.verificaCor(id_tipo)
        
        tipo = t.Tipo(id_tipo)
        natureza = n.Natureza(id_natureza)
        cidade = c.Cidade(id_cidade)
        ano = a.Ano(id_ano)

        todosMeses = mesController.getTodosMeses()
        ocorrenciaMes = []

        for i in range(len(todosMeses)):
            ocorrencias = ocorrenciaDaoBean.getDetalheOcorrenciaPorMes(natureza.idNatureza, cidade.idCidade, i + 1, ano.idAno, tipo.idTipo)
            if ocorrencias[4] != None:
                ocorrenciaMes.append(int(ocorrencias[4]))
            else:
                ocorrenciaMes.append(0)

        #PLOTA O GRÁFICO
        grafico.plotGraph("Número de registros de casos de " + str(natureza.nomeNatureza) +
         "\nno ano de " + str(ano.ano) + 
             "\nna cidade de " + str(cidade.cidade),
            "Meses",
            "Registros",
            todosMeses,
            ocorrenciaMes,
            cor,
            "bar",
            "Images/consultaOcorrenciaMesAno_" + str(tipo.nomeTipo) + ".png")
    
    #ESTE MÉTODO MOSTRA O SOMATÓRIO DE TODAS OCORRÊNCIAS NO PERÍODO TODO
    def exibeSomatorioTodasOcorrenciasPeriodo(self, id_tipo):
        tipo = t.Tipo(id_tipo)
        somatorio = int(ocorrenciaDaoBean.getSomatorioTodasOcorrenciasPeriodo(tipo.idTipo))
        ocorrenciasMes = round((somatorio/26), 2)
        ocorrenciasDia = round((somatorio/789), 2)

        print("Na cidade de Cruzeiro, no período de 2017 a 2019 foram registradas um total de " + str(somatorio) + " ocorrências filtradas por " + str(tipo.nomeTipo) +
        "\nConsiderando que esta análise esta baseada em dois anos e mais dois meses, a média do número de ocorrências por mês é de " + str(ocorrenciasMes) +
            "\nPor fim a cidade de Cruzeiro, possui uma média de " + str(ocorrenciasDia) + " ocorrências filtradas por " + str(tipo.nomeTipo) + " por dia")
    
    #ESTE METODO MOSTRA OS DETALHES DE UMA DETERMINADA OCORRÊNCIA EM UM DETERMINADO ANO
    def consultaDetalheOcorrenciaMesaAno(self, id_natureza, id_cidade, id_mes, id_ano, id_tipo):
        natureza = n.Natureza(id_natureza)
        cidade = c.Cidade(id_cidade)
        mes = m.Mes(id_mes)
        ano = a.Ano(id_ano)
        tipo = t.Tipo(id_tipo)

        ocorrencias = ocorrenciaDaoBean.getDetalheOcorrenciaPorMes(natureza.idNatureza, cidade.idCidade, mes.idMes, ano.idAno, tipo.idTipo)

        print("Na cidade de " + str(cidade.cidade) + ", no mês de " + str(mes.mes) + " de " + str(ano.ano) + " obtiveram-se um total de " + str(ocorrencias[4]) + " registros de ocorrências filtradas por " + str(tipo.nomeTipo) + ".")

    def consultaDetalheTodasOcorrenciasMesAno(self, id_cidade, id_mes, id_ano, id_tipo):
        cor = self.verificaCor(id_tipo)
        cidade = c.Cidade(id_cidade)
        mes = m.Mes(id_mes)
        ano = a.Ano(id_ano)
        tipo = t.Tipo(id_tipo)

        ocorrencias = []
        registros = []

        detalhesOcorrencias = ocorrenciaDaoBean.getDetalheTodasOcorrenciasPorMes(cidade.idCidade, mes.idMes, ano.idAno, tipo.idTipo)

        for ocorrencia in range(len(detalhesOcorrencias)):
            ocorrencias.append(detalhesOcorrencias[ocorrencia][0])
            registros.append(int(detalhesOcorrencias[ocorrencia][4]))
        
        grafico.plotGraph("Registros de todas as ocorrências filtradas por " + str(tipo.nomeTipo) +
        "\nno mês de " + str(mes.mes) + " de " + str(ano.ano),
            "Nome da ocorrência",
            "Registros",
            ocorrencias,
            registros,
            cor,
            "plot",
            "Images/consultaDetalheTodasOcorrenciasMesAno_" + str(tipo.nomeTipo) + ".png")

    # MÉTODO PARA MUDAR A COR DO GRÁFICO DE ACORDO COM O FILTRO SELECIONADO
    def verificaCor(self, id_tipo):
        cor = ""
        # VERIFICA A COR DO GRÁFICO DE ACORDO COM O FILTRO
        if id_tipo == 1:
            cor = "blue"
        if id_tipo == 2:
            cor = "red"
        
        return cor