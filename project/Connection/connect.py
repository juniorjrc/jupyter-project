try:
    import pymysql
except:
    import subprocess
    subprocess.call(["pip", "install", "pymysql"])
    import pymysql

#INSTÂNCIA DA CONEXÃO COM O BANCO
class Conexao():
    def __init__(self):
        self.conexao = pymysql.connect(
            host='172.17.0.1',
            port=3307,
            database='PROJREDES',
            user='MainUser',
            password='MainPassword'
        )

        self.bd = self.conexao.cursor()

