from Connection import connect as c

#TB_ANO
#CLASSE RESPONSÁVEL PELA BUSCA DO ANO E DOS ANOS NA BASE DE DADOS
class AnoDAO():

    #BUSCA O ANO NA [TB_ANO]
    def getAno(self, id_ano):
        self.connect = c.Conexao()
        self.id_ano = id_ano
        self.query  = self.connect.bd
        try:
            sql = "SELECT ID_ANO, ANO FROM TB_ANO WHERE ID_ANO = %s"
            self.query.execute(sql,(id_ano))

            ano = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA O ANO
            return ano

        except:
            return "Ano não encontrado!!"

    #BUSCA TODOS OS ANOS NA [TB_ANO]
    def getTodosAnos(self):
        self.connect = c.Conexao()
        self.query  = self.connect.bd
        try:
            self.query.execute(
                "SELECT ID_ANO, ANO FROM TB_ANO"
            )

            anos = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODOS OS ANOS
            return anos

        except:
            return "Anos não encontrado!!"

