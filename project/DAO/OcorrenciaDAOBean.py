from Connection import connect as c

#TB_OCORRENCIA
#CLASSE RESPONSÁVEL PELA BUSCA DAS OCORRENCIAS OU DE UMA OCORRÊNCIA NA BASE DE DADOS
class Ocorrencia():

    def getQtdOcorrenciaMesAno(self, id_natureza, id_cidade, id_ano, id_mes, id_tipo):
        self.connect = c.Conexao()
        self.query = self.connect.bd

        try:
            sql = (
                "SELECT QTD_OCORRENCIAS FROM TB_OCORRENCIA WHERE ID_NATUREZA = %s AND ID_CIDADE = %s AND ID_ANO = %s AND ID_MES = %s AND ID_TIPO = %s;"
            )
            self.query.execute(sql, (id_natureza, id_cidade, id_ano, id_mes, id_tipo))

            ocorrenciaMesAno = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA A QUANTIDADE DE UMA DETERMINADA OCORRÊNCIA E UM ANO E UM MÊS
            return ocorrenciaMesAno[0]
        
        except Exception as e:
            print(str(e))
            return "Ocorrências não encontradas!!"


    
    #BUSCA O SOMATÓRIO DE TODAS AS OCORRÊNCIAS EM UM DETERMINADO MÊS E UM DETERMINADO ANO
    def getSomatoriotOcorrenciasPorMes(self, id_mes, id_ano, id_cidade, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = (
                "SELECT SUM(QTD_OCORRENCIAS) FROM TB_OCORRENCIA WHERE ID_MES = %s" + 
                " AND ID_ANO = %s" + 
                " AND ID_CIDADE = %s" +
                " AND ID_TIPO =  %s"
                )
            self.query.execute(sql, (id_mes, id_ano, id_cidade, id_tipo))

            ocorrenciaPorMes = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODAS AS OCORRÊNCIAS DE ACORDO COM O MÊS E COM O ANO INFORMADO
            return ocorrenciaPorMes[0]

        except:
            return "Ocorrências não encontradas!!"
    

    #BUSCA O SOMATÓRIO DE UMA DETERMINADA OCORRÊNCIA DURANTE O ANO
    def getSomatorioOcorrenciaPorAno(self, id_natureza, id_ano, id_cidade, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = (
                "SELECT SUM(QTD_OCORRENCIAS) FROM TB_OCORRENCIA WHERE ID_NATUREZA = %s" +
                " AND ID_ANO = %s" +
                " AND ID_CIDADE = %s" +
                " AND ID_TIPO = %s"
            )
            self.query.execute(sql, (id_natureza, id_ano, id_cidade, id_tipo))

            ocorrenciaPorAno = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA O SOMATORIO DE UMA DETERMINADA OCORRENCIA DURANTE UM ANO ESPECÍFICO
            return ocorrenciaPorAno[0]

        except:
            return "Ocorrências não encontradas!!"
    

    #BUSCA O SOMATÓRIO DE TODAS AS OCORRÊNCIAS DURANTE O ANO ESPECÍFICO
    def getSomatorioTodasOcorrenciasPorAno(self, id_ano, id_cidade, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = (
                "SELECT SUM(QTD_OCORRENCIAS) FROM TB_OCORRENCIA WHERE ID_ANO = %s" +
                " AND ID_CIDADE= %s" + 
                " AND ID_TIPO = %s"
                )
            self.query.execute(sql, (id_ano, id_cidade, id_tipo))

            todasOcorrenciasPorAno = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODAS AS OCORRÊNCIAS DURANTE O ANO ESPECÍFICO
            return todasOcorrenciasPorAno[0]

        except:
            return "Ocorrências não encontradas!!"



    #BUSCA O SOMATÓRIO DE TODAS AS OCORRÊNCIAS DURANTE O PERÍODO DE 2017 A FEVEREIRO DE 2019
    def getSomatorioTodasOcorrenciasPeriodo(self, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = "SELECT SUM(QTD_OCORRENCIAS) FROM TB_OCORRENCIA WHERE ID_TIPO = %s;"
            self.query.execute(sql, (id_tipo))

            todasOcorrenciasPeriodo = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODAS AS OCORRÊNCIAS DURANTE O PERÍODO DE 2017 A FEVEREIRO DE 2019
            return todasOcorrenciasPeriodo[0]

        except:
            return "Ocorrências não encontradas!!"

    
    #BUSCA OS DETALHES DE UMA OCORRENCIA ESPECÍFICA DE ACORDO COM UM MÊS ESPECÍFICO E UM ANO ESPECÍFICO
    def getDetalheOcorrenciaPorMes(self, id_natureza, id_cidade, id_mes, id_ano, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = (
                "SELECT NAT.NOME_NATUREZA, CID.NOME_CIDADE, ANO.ANO, M.NOME_MES, OCO.QTD_OCORRENCIAS, TIPO.NOME_TIPO" + 
                " FROM TB_NATUREZA NAT," +
                " TB_CIDADE CID," +
                " TB_ANO ANO," +
                " TB_MES M,"
                " TB_OCORRENCIA OCO," +
                " TB_TIPO TIPO" +
                " WHERE" +
                " OCO.ID_NATUREZA = %s AND" +
                " OCO.ID_NATUREZA = NAT.ID_OCORRENCIA AND" +
                " CID.ID_CIDADE = %s AND" +
                " OCO.ID_CIDADE = CID.ID_CIDADE AND" +
                " M.ID_MES = %s AND" +
                " OCO.ID_MES = M.ID_MES AND" +
                " ANO.ID_ANO = %s AND" +
                " OCO.ID_ANO = ANO.ID_ANO AND" +
                " TIPO.ID_TIPO = %s AND" +
                " OCO.ID_TIPO = TIPO.ID_TIPO;"
            )
            self.query.execute(sql, (id_natureza, id_cidade, id_mes, id_ano, id_tipo))

            detalheOcorrenciaPorMes = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA OS DETALHES DE UMA OCORRÊNCIA DURANTE UM MÊS E UM ANO ESPECIFICADO
            return detalheOcorrenciaPorMes

        except:
            return "Ocorrências não encontradas!!"


    #BUSCA OS DETALHES DE TODAS AS OCORRENCIAS DE ACORDO COM O MÊS E COM O ANO
    def getDetalheTodasOcorrenciasPorMes(self, id_cidade, id_mes, id_ano, id_tipo):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            sql = (
                "SELECT NAT.NOME_NATUREZA, CID.NOME_CIDADE, ANO.ANO, M.NOME_MES, OCO.QTD_OCORRENCIAS, TIPO.NOME_TIPO" +
                " FROM TB_NATUREZA NAT," +
                " TB_CIDADE CID," + 
                " TB_ANO ANO," +
                " TB_MES M," +
                " TB_OCORRENCIA OCO," + 
                " TB_TIPO TIPO" +
                " WHERE" +
                " OCO.ID_NATUREZA = NAT.ID_OCORRENCIA AND" +
                " CID.ID_CIDADE = %s AND"
                " OCO.ID_CIDADE = CID.ID_CIDADE AND" +
                " M.ID_MES = %s AND" +
                " OCO.ID_MES = M.ID_MES AND" +
                " ANO.ID_ANO = %s AND" +
                " OCO.ID_ANO = ANO.ID_ANO AND" +
                " TIPO.ID_TIPO = %s AND" +
                " OCO.ID_TIPO = TIPO.ID_TIPO"
            )
            self.query.execute(sql, (id_cidade, id_mes, id_ano, id_tipo))

            detalheTodasOcorrenciasPorMes = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA O DETALHE DE TODAS AS OCORRENCIAS DURANTE UM MÊS ESPECÍFICO
            return detalheTodasOcorrenciasPorMes

        except Exception as e:
            print(str(e))
            return "Ocorrências não encontradas!!"