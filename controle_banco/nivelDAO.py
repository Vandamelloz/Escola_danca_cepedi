import sqlite3
from banco.database import Banco
from model.niveis_classe import Niveis

class ManipularNivel:
    def __init__(self, db: Banco):
        self.db = db
    
    def salvarNivel(self, n: Niveis):
        cur = cur.db.meuCursor()
        con = self.db.con

        nivel = ('''
        SELECT id FROM Niveis;''')
        cur.execute(nivel)
        lista = list(cur.fetchall(nivel))
        nome = (f"""SELECT nome FROM Niveis WHERE id = {id};""")
        cur.execute(nome)
        lista_nome = list(cur.fetchall(nome))
        
        if id in lista or nome in lista_nome:
            print(f"Nível {nome} no banco de dados")
        else:
            cur.execute("""
            INSERT INTO Niveis (id, nome) VALUES (?, ?);
            """,(n.id, n.nome))
            con.commit()