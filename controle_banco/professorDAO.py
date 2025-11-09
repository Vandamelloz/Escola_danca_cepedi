import sqlite3
from model.professor_classe import Professor
from banco.database import Banco

class ManipularProfessor:
    def __inti__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def salvarProfessor(self, p: Professor,):
        cur = self.db.meuCursor()
        con = self.banco.con

        professor = ('''
        SELECT id FROM Professor;''')
        cur.execute(professor)

        lista = list(cur.fetchall(professor))
        if id in lista:
            print("Professor já cadastrado no banco de dados")
            cur.execute(f"""
            UPDATE Professor SET nome = {p.nome}, avaliador = {p.avaliador} WHERE id = {p.id};""")
            con.commit()
        else:
            cur.execute("""
            INSERT INTO Professor (nome, id, avaliador) VALUES (?, ?, ?);
            """, (p.nome, p.id, p.avaliador))
            con.commit()           

    def verProfessorPorId(self, p: Professor):
        cur = self.db.meuCursor()

        professor = (f'''
        SELECT * FROM Professor WHERE id = {p.id};''')
        cur.execute(professor)

        professor.imprimirProfessor()
    
    def listarProfessores(self):
        cur = self.db.meuCursor()

        professor = (f'''
        SELECT * FROM Professor;''')
        cur.execute(professor)

        for linha in cur.fetchall():
            print(linha)