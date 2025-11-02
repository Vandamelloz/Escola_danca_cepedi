import sqlite3


class banco():
    def __init__(self, banco: str = "escola_de_danca.db"):
        self.banco = banco
        self.con = None

    # Conecta o banco de dados
    def conectar(self):
        if self.con is None:
            self.con = sqlite3.connect(self.banco)
            self.con.row_factory = sqlite3.Row
            self.con.execute("PRAGMA foreign_keys = ON")
        return self.con

    # Desconecta o banco
    def deconectar(self):
        if self.con:
            self.con.close()
            self.con = None

    # Cria e retorna cursor
    def meuCursor(self):
        if self.con is None:
            self.conectar()
        return self.con.cursor()

    # Método para criar uma tabela dinâmica
    def criarTabela(self, nome: str, colunas: str):
        if self.con:
            cursor = self.con.cursor()
            comando = f"CREATE TABLE IF NOT EXISTS {nome} ({colunas});"
            try:
                cursor.execute(comando)
                self.con.commit()
                print(f"Tabela '{nome}' criada com sucesso!")
            except sqlite3.Error as e:
                print(f"Erro ao criar a tabela: {e}")
        else:
            print("Conexão não estabelecida. Chame primeiro conectar().")