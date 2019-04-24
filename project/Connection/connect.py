import pymysql

#INSTÂNCIA DA CONEXÃO COM O BANCO
class Conexao():
    def __init__(self):
        self.conexao = pymysql.connect(
            host='localhost',
            port=3307,
            database='PROJREDES',
            user='root',
            password='root'
        )

        self.bd = self.conexao.cursor()

