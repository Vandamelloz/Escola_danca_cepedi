import sqlite3
from model.professor_classe import Professor

from db.database import Banco

class ManipularProfessor:
    def __init__(self, db: Banco):  # <-- CORRIGIDO AQUI
        self.db = db
        self.db.conectar()

    def adicionarProfessor(self, p: Professor):
        cur = self.db.meuCursor()
        con = self.db.con

        # Verifica se já existe professor com esse ID
        cur.execute("SELECT id FROM Professor WHERE id = ?", (p.id,))
        existe = cur.fetchone()

        if existe is None:
            cur.execute("""
                INSERT INTO Professor (id, nome, avaliador) 
                VALUES (?, ?, ?)
            """, (p.id, p.nome, p.avaliador))
            con.commit()
            print(f"Professor '{p.nome}' adicionado com sucesso!")
        else:
            cur.execute("""
                UPDATE Professor 
                SET nome = ?, avaliador = ?
                WHERE id = ?
            """, (p.nome, p.avaliador, p.id))
            con.commit()
            print(f" Professor '{p.nome}' atualizado com sucesso!")

    def listarProfessores(self):
        cur = self.db.meuCursor()
        cur.execute("SELECT * FROM Professor")
        resultados = cur.fetchall()
        professores = [Professor(id=r[0], nome=r[1], avaliador=r[2]) for r in resultados]
        return professores

    def excluirProfessor(self, id: int):
        cur = self.db.meuCursor()
        cur.execute("DELETE FROM Professor WHERE id = ?", (id,))
        self.db.con.commit()
        print(f" Professor com ID {id} removido com sucesso!")
