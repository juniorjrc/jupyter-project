#IGNORA OS WARNINGS ORIUNDOS DO JUPYTER
import warnings
warnings.filterwarnings('ignore')

#IMPORTA A BIBLIOTECA IPython
try:
    from IPython.core.display import display, HTML
except:
    import subprocess
    subprocess.call(["pip", "install", "IPython"])
    from IPython.core.display import display, HTML

# DAO
from DAO import OcorrenciaDAOBean as odb
ocorrenciaDaoBean = odb.Ocorrencia()

# CONTROLLERS
from Controller import AnoController as ac
from Controller import MesController as mc
from Controller import NaturezaController as nc
anoController = ac.AnoController()
mesController = mc.MesController()
naturezaController = nc.NaturezaController()

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
    # ESTE METODO MOSTRA O O GRÁFICO EM PIZZA DA CIDADE DE CRUZEIRO, VISANDO DE UMA FORMA GERAL, TODO O CENÁRIO DE OCORRÊNCIAS
    def exibeInformacoesCompletasOcorrencias(self, id_cidade, id_tipo):
        cidade = c.Cidade(id_cidade)
        tipo = t.Tipo(id_tipo)
        todasNaturezasProdutividade, todasNaturezasOcorrencias = naturezaController.getTodasNaturezas()

        todosRegistrosProdutividade = []
        todosRegistrosOcorrencias = []

        if tipo.idTipo == 1:
            #PERCORRE OS REGISTROS FILTRADOS POR PRODUTIVIDADE POLICIAL
            for i in range(12):
                naturezas = ocorrenciaDaoBean.getSomatorioUmaOcorrenciaPeriodo(cidade.idCidade, i + 1, tipo.idTipo)
                todosRegistrosProdutividade.append(int(naturezas))
            return grafico.plotPizzaGraph(
            todasNaturezasProdutividade,
            todosRegistrosProdutividade,
            "Visão geral do cenário de registros de ocorrências filtradas por <b>" + str(tipo.nomeTipo) + "</b>.",
            "exibeInformacoesCompletasOcorrencias_" + str(tipo.idTipo)
        )
        
        if tipo.idTipo == 2:
            #PERCORRE OS REGISTROS FILTRADOS POR OCORRÊNCIAS REGISTRADAS
            for i in range(23):
                naturezas = ocorrenciaDaoBean.getSomatorioUmaOcorrenciaPeriodo(cidade.idCidade, i + 13, tipo.idTipo)
                todosRegistrosOcorrencias.append(int(naturezas))
            return grafico.plotPizzaGraph(
            todasNaturezasOcorrencias,
            todosRegistrosOcorrencias,
            "Visão geral do cenário de registros de ocorrências filtradas por " + str(tipo.nomeTipo) + ".",
            "exibeInformacoesCompletasOcorrencias_" + str(tipo.idTipo)
        )
        
    #ESTE MÉTODO RETORNA O GRÁFICO COMPARATIVO DE TODAS AS OCORRÊNCIAS DE ACORDO COM O PERÍODO EX.: OCORRENCIAS DO ANO 2017, 2018 E 2019
    def consultaSomatorioTodasOcorrenciasPeriodo(self,id_cidade):
        cidade = c.Cidade(id_cidade)
        tipo1 = t.Tipo(1)
        tipo2 = t.Tipo(2)

        todosAnos = anoController.getTodosAnos()
        somatorioOcorrencias = []
        somatorioProdutividade = []

        #PERCORRE O SOMATÓRIO DE TODAS OCORRENCIAS FILTRADAS POR PRODUTIVIDADE POLICIAL NO PERIODO QUE CONSTA NO BANCO
        for i in range(len(todosAnos)):
            somatorioProdutividade.append(int(ocorrenciaDaoBean.getSomatorioTodasOcorrenciasPorAno(i + 1, cidade.idCidade, 1)))
        
        #PERCORRE O SOMATÓRIO DE TODAS AS OCORRENCIAS FILTRADAS POR OCORRENCIAS REGISTRADAS NO PERIODO QUE CONSTA NO BANCO NO BANCO
        for i in range(len(todosAnos)):
            somatorioOcorrencias.append(int(ocorrenciaDaoBean.getSomatorioTodasOcorrenciasPorAno(i + 1, cidade.idCidade, 2)))

        #PLOTA O GRÁFICO
        return grafico.plotComparativeGraph(
            "Somatório de todos registros de ocorrências na cidade de Cruzeiro<br>no período de 2017 à Março de 2019 para ambos os filtros",
                "Anos",
                todosAnos,
                somatorioProdutividade,
                str(tipo1.nomeTipo),
                "Registros",
                todosAnos,
                somatorioOcorrencias,
                str(tipo2.nomeTipo),
                "consultaSomatorioTodasOcorrenciasPeriodo"
        )
    
    #ESTE MÉTODO RETORNA O GRÁFICO COMPARATIVO DE TODAS OCORRÊNCIAS DURANTE UM MÊS ESPECÍFICO NO PERIODO DE 2017 A 2019
    def consultaSomatorioTodasOcorrenciasMes(self, id_mes, id_cidade):
        tipo1 = t.Tipo(1)
        tipo2 = t.Tipo(2)
        mes = m.Mes(id_mes)
        cidade = c.Cidade(id_cidade)

        todosAnos = anoController.getTodosAnos()
        ocorrenciasMesProdutividade = []
        ocorrenciasMesOcorrencias = []

        #PERCORRE O SOMATÓRIO DE TODAS OCORRÊNCIAS FILTRADAS POR PRODUTIVIDADE DURANTE UM DETERMINADO MÊS
        for i in range(len(todosAnos)):
            ocorrencias = ocorrenciaDaoBean.getSomatoriotOcorrenciasPorMes(mes.idMes, str(i + 1), cidade.idCidade, tipo1.idTipo)
            if ocorrencias != None:
                ocorrenciasMesProdutividade.append(int(ocorrencias))
            else:
                ocorrenciasMesProdutividade.append(0)
        
        #PERCORRE O SOMATÓRIO DE TODAS OCORRÊNCIAS FILTRADAS POR OCORRENCIAS REGISTRADAS DURANTE UM DETERMINADO MÊS
        for i in range(len(todosAnos)):
            ocorrencias = ocorrenciaDaoBean.getSomatoriotOcorrenciasPorMes(mes.idMes, str(i + 1), cidade.idCidade, tipo2.idTipo)
            if ocorrencias != None:
                ocorrenciasMesOcorrencias.append(int(ocorrencias))
            else:
                ocorrenciasMesOcorrencias.append(0)
        
        #PLOTA O GRÁFICO
        return grafico.plotComparativeGraph(
            "Gŕafico do número de ocorrências registradas na base da polícia no mês de <b>" + str(mes.mes) + 
            "</b><br>no período de 2017 à Março de 2019 para ambos os filtros.",
                "Anos",
                todosAnos,
                ocorrenciasMesProdutividade,
                str(tipo1.nomeTipo),
                "Registros",
                todosAnos,
                ocorrenciasMesOcorrencias,
                str(tipo2.nomeTipo),
                "consultaSomatorioTodasOcorrenciasMes"
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
        return grafico.plotNormalGraph(
            "Gráfico do somatório dos registros de <b>" + str(natureza.nomeNatureza) + 
            "</b><br>filtradas por " + str(tipo.nomeTipo) +
                "<br>no período de 2017 à Março de 2019",
                "Anos",
                "Registros",
                todosAnos,
                ocorrenciaAno,
                str(natureza.nomeNatureza),
                cor,
                "consultaSomatorioUmaOcorrenciaPeriodo_" + str(tipo.idTipo)
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
        return grafico.plotNormalGraph(
            "Número de registros de casos de <b>" + str(natureza.nomeNatureza) +
            "</b><br>no ano de " + str(ano.ano) +
                "<br>na cidade de " + str(cidade.cidade),
                "Meses",
                "Registros",
                todosMeses,
                ocorrenciaMes,
                str(natureza.nomeNatureza),
                cor,
                "consultaOcorrenciaMesAno_" + str(tipo.idTipo)
        )
    
    #ESTE MÉTODO MOSTRA O SOMATÓRIO DE TODAS OCORRÊNCIAS NO PERÍODO TODO
    def exibeSomatorioTodasOcorrenciasPeriodo(self, id_tipo):
        tipo = t.Tipo(id_tipo)
        somatorio = int(ocorrenciaDaoBean.getSomatorioTodasOcorrenciasPeriodo(tipo.idTipo))
        ocorrenciasMes = round((somatorio/26), 2)
        ocorrenciasDia = round((somatorio/789), 2)

        display(HTML("<i>Na cidade de Cruzeiro, no período de 2017 a 2019 foram registradas um total de <b>" + str(somatorio) + "</b> ocorrências filtradas por " + str(tipo.nomeTipo) +
        "<br>Considerando que esta análise esta baseada em dois anos e mais três meses, a média do número de ocorrências por mês é de <b>" + str(ocorrenciasMes) +
        "</b><br>Por fim a cidade de Cruzeiro, possui uma média de <b>" + str(ocorrenciasDia) + "</b> ocorrências filtradas por " + str(tipo.nomeTipo) + " por dia</i>"))
    
    #ESTE METODO MOSTRA OS DETALHES DE UMA DETERMINADA OCORRÊNCIA EM UM DETERMINADO ANO
    def consultaDetalheOcorrenciaMesaAno(self, id_natureza, id_cidade, id_mes, id_ano, id_tipo):
        natureza = n.Natureza(id_natureza)
        cidade = c.Cidade(id_cidade)
        mes = m.Mes(id_mes)
        ano = a.Ano(id_ano)
        tipo = t.Tipo(id_tipo)

        ocorrencias = ocorrenciaDaoBean.getDetalheOcorrenciaPorMes(natureza.idNatureza, cidade.idCidade, mes.idMes, ano.idAno, tipo.idTipo)

        print("Na cidade de " + str(cidade.cidade) + ", no mês de " + str(mes.mes) + " de " + str(ano.ano) + " obtiveram-se um total de " + str(ocorrencias[4]) + " registros de ocorrências de " + str(natureza.nomeNatureza) + " filtradas por " + str(tipo.nomeTipo) + ".")

    #ESTE METODO MOSTRA OS DETALHES DE TODAS NATUREZAS EM MÊS E ANO ESPECIFICADO
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
        
        return grafico.plotHorizontalGraph(
            "Registros de todas as ocorrências filtradas por <b>" + str(tipo.nomeTipo) +
            "</b><br>no mês de " + str(mes.mes) + " de " + str(ano.ano),
                "Registros",
                "Naturezas",
                registros,
                ocorrencias,
                cor,
                "consultaDetalheTodasOcorrenciasMesAno" + str(tipo.idTipo)
        )

    #ESTE MÉTODO RETORNA O COMPARATIVO DE TODAS AS NATUREZAS DURANTE MÊS ESPECIFICADO EM TODO O PERÍODO
    def consultaRegistroFinal(self, id_cidade, id_mes, id_tipo):
        if id_tipo == 1:
            paletaCores = ['rgba(38, 96, 220, 0.7)', 'rgba(1, 43, 133, 0.7)', 'rgba(2, 22, 65, 0.7)']
        if id_tipo == 2:
            paletaCores = ['rgba(195, 55, 64, 0.7)', 'rgba(130, 3, 11, 0.7)', 'rgba(78, 1, 6, 0.7)']

        cidade = c.Cidade(id_cidade)
        mes = m.Mes(id_mes)
        tipo = t.Tipo(id_tipo)

        ocorrencias = []
        registros2017 = []
        registros2018 = []
        registros2019 = []

        #2017
        detalhesOcorrencias = ocorrenciaDaoBean.getDetalheTodasOcorrenciasPorMes(cidade.idCidade, mes.idMes, 1, tipo.idTipo)
        for ocorrencia in range(len(detalhesOcorrencias)):
            ocorrencias.append(detalhesOcorrencias[ocorrencia][0])
            registros2017.append(int(detalhesOcorrencias[ocorrencia][4]))
        
        #2018
        detalhesOcorrencias = ocorrenciaDaoBean.getDetalheTodasOcorrenciasPorMes(cidade.idCidade, mes.idMes, 2, tipo.idTipo)
        for ocorrencia in range(len(detalhesOcorrencias)):
            registros2018.append(int(detalhesOcorrencias[ocorrencia][4]))
        
        #2019
        detalhesOcorrencias = ocorrenciaDaoBean.getDetalheTodasOcorrenciasPorMes(cidade.idCidade, mes.idMes, 3, tipo.idTipo)
        for ocorrencia in range(len(detalhesOcorrencias)):
            registros2019.append(int(detalhesOcorrencias[ocorrencia][4]))
        
        return grafico.plotHorizontalComparativeGraph(
            "Comparativo dos registros de todas as ocorrências registradas na cidade de " + str(cidade.cidade) + 
            "<br>filtradas por " + str(tipo.nomeTipo) + " no mês de <b>" + str(mes.mes) + "</b>",
                "Registros",
                "Naturezas",
                ocorrencias,
                registros2017,
                2017,
                paletaCores[0],
                ocorrencias,
                registros2018,
                2018,
                paletaCores[1],
                ocorrencias,
                registros2019,
                2019,
                paletaCores[2],
                "consultaRegistroFinal_" + str(tipo.idTipo)
        )

    # MÉTODO PARA MUDAR A COR DO GRÁFICO DE ACORDO COM O FILTRO SELECIONADO
    def verificaCor(self, id_tipo):
        cor = ""
        # VERIFICA A COR DO GRÁFICO DE ACORDO COM O FILTRO
        if id_tipo == 1:
            cor = 'rgba(38, 96, 220, 0.7)'
        if id_tipo == 2:
            cor = 'rgba(195, 55, 64, 0.7)'
        
        return cor