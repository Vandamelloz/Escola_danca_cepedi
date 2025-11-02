#Necessário a importação do sqlite3
import sqlite3

#Classe que gerencia a conexão e a criação de tabelas no banco

class banco():
    def __init__(self, banco: str = "escola_de_danca.db"):
        self.banco = banco
        self.con = None
    
    #conecta o banco de dados e envia a função con para o resto do programa
    def conectar(self):
        if self.con is None:
            #não vou usar a função "isolation_level=None" para não deixar o autocommit ativado
            self.con = sqlite3.connect(self.banco)
            self.con.row_factory = sqlite3.Row
            self.con.execute("PRAGMA foreign_keys = ON")
        return self.con
    
    #desconecta o banco de dados
    def deconectar(self):
        if self.con:
            self.con.close()
            self.con = None
    
    #cria o cursor e envia para ser usado no resto do programa
    def meuCursor(self):
        if self.con is None:
            self.conectar()
            return self.con.cursor()
    
    #vai criar as tabelas quando estiver pronta
    def criarTabelas(self):
        print("Por enquanto não fiz nada aqui")