from Connection import connect as c

#TB_NATUREZA
#CLASSE RESPONSÁVEL PELA BUSCA DAS NATUREZAS(TIPOS DE OCORRÊNCIAS) NA BASE DE DADOS
class NaturezaDAO():
    
    #BUSCA UMA NATUREZA NA [TB_NATUREZA]
    def getNatureza(self, id_natureza):
        self.connect = c.Conexao()
        self.id_natureza    = id_natureza
        self.query          = self.connect.bd

        try:
            sql = "SELECT ID_OCORRENCIA, NOME_NATUREZA, DESCRICAO_NATUREZA FROM TB_NATUREZA WHERE ID_OCORRENCIA = %s"
            self.query.execute(sql, (id_natureza))

            natureza = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA A NATUREZA
            return natureza

        except:
            return "Natureza não encontrada!!"

    #BUSCA TODAS AS NATUREZAS NA [TB_NATUREZA]
    def getTodasNaturezas(self):
        self.connect = c.Conexao()
        self.query          = self.connect.bd

        try:
            self.query.execute(
                "SELECT ID_OCORRENCIA, NOME_NATUREZA, DESCRICAO_NATUREZA FROM TB_NATUREZA"
            )

            naturezas = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODAS AS NATUREZAS
            return naturezas

        except:
            return "Naturezas não encontradas!!"

