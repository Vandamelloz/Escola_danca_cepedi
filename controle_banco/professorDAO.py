import sqlite3
from model.professor_classe import Professor
from db.database import Banco

class ManipularProfessor:
    def __inti__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def adicionarProfessor(self, p: Professor):
        cur = self.db.meuCursor()
        con = self.banco.con

        if id is None:
            cur.execute("""
            INSERT INTO Professor (nome, id, avaliador) VALUES (?, ?, ?);
            """, (p.nome, p.id, p.avaliador))
            con.commit() #Mudar depois para autocommit?

        else:
            cur.execute(f"""
            UPDATE Professor SET nome = {p.nome}, avaliador = {p.avaliador} WHERE id = {p.id};""")


         
    
        
        



        
        