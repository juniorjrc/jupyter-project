from Connection import connect as c

#TB_MES
#CLASSE RESPONSÁVEL PELA BUSCA DO MÊS E TODOS OS MESES NA BASE DE DADOS
class MesDAO():

    #BUSCA O MÊS NA [TB_MES]
    def getMes(self, id_mes):
        self.connect = c.Conexao()
        self.id_mes = id_mes
        self.query  = self.connect.bd

        try:
            sql = "SELECT ID_MES, NOME_MES FROM TB_MES WHERE ID_MES = %s"
            self.query.execute(sql, (id_mes))

            mes = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA O MÊS
            return mes

        except:
            return "Mês não encontrado!!"

    #BUSCA TODOS OS MESES NA [TB_MES]
    def getTodosMeses(self):
        self.connect = c.Conexao()
        self.query  = self.connect.bd

        try:
            self.query.execute(
                "SELECT ID_MES, NOME_MES FROM TB_MES"
            )

            meses = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODOS OS MESES
            return meses

        except:
            return "Mêses não encontrados!!"
