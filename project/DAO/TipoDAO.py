from Connection import connect as c

#TB_TIPO
#CLASSE RESPONSÁVEL PELA BUSCA DO TIPO DO FILTRO
class TipoDAO():
    
    #BUSCA UM TIPO NA [TB_TIPO]
    def getTipo(self, id_tipo):
        self.connect = c.Conexao()
        self.id_tipo = id_tipo
        self.query  = self.connect.bd

        try:
            sql = "SELECT ID_TIPO, NOME_TIPO FROM TB_TIPO WHERE ID_TIPO = %s"
            self.query.execute(sql, (id_tipo))

            tipo = self.query.fetchone()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA O TIPO
            return tipo

        except:
            return "Tipo não encontrado!!"


    #BUSCA TODOS OS TIPOS NA [TB_TIPO]
    def getTodosTipos(self):
        self.connect = c.Conexao()
        self.query  = self.connect.bd

        try:
            self.query.execute(
                "SELECT ID_TIPO, NOME_TIPO FROM TB_TIPO"
            )

            tipos = self.query.fetchall()

            self.connect.conexao.commit()
            self.connect.conexao.close()

            #RETORNA TODOS OS TIPOS
            return tipos

        except:
            return "Tipos não encontrados!!"
