from Connection import connect as c

#TB_CIDADE
#CLASSE RESPONSÁVEL PELA BUSCA DA CIDADE E DAS CIDADES NA BASE DE DADOS
class CidadeDAO():
    
    #BUSCA UMA CIDADE NA [TB_CIDADE]
    def getCidade(self, id_cidade):
        self.connect = c.Conexao()
        self.id_cidade = id_cidade
        self.query  = self.connect.bd

        try:
            sql = "SELECT ID_CIDADE, NOME_CIDADE FROM TB_CIDADE WHERE ID_CIDADE = %s"
            self.query.execute(sql, (id_cidade))

            cidade = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA A CIDADE
            return cidade

        except:
            return "Cidade não encontrada!!"


    #BUSCA TODAS AS CIDADES NA [TB_CIDADE]
    def getTodasCidades(self):
        self.connect = c.Conexao()
        self.query  = self.connect.bd

        try:
            self.query.execute(
                "SELECT ID_CIDADE, NOME_CIDADE FROM TB_CIDADE"
            )

            cidades = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODAS AS CIDADES
            return cidades

        except:
            return "Cidade não encontrada!!"
