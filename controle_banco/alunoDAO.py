import sqlite3
from banco.database import Banco
from model.aluno_classe import Aluno

class ManipularAluno:
    def __init__(self, db: Banco):
        self.banco = db
        self.banco.conectar()
    
    def salvarAluno(self, a: Aluno):
        cur = self.banco.meuCursor()
        con = self.banco.con

        aluno = ('''
            SELECT matricula FROM Aluno;
        ''')
        cur.execute(aluno)

        lista = list(cur.fetchall(aluno))
        if a.matricula in lista:
            print("Aluno já cadastrado no banco de dados")
        else:
            cur.execute("""
            INSERT INTO Aluno (nome, matricula, idade, 
            nivelCondutor, nivelConduzido, dataNivelConduzido, dataNivelCondutor) 
            VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (a.nome, a.matricula, a.idade, a.nivelCondutor, 
                  a.nivelConduzido, a.dataNivelConduzido, a.dataNivelCondutor))
            con.commit()

    def atualizarDadosPessoaisAluno(self, a : Aluno):
        cur = self.banco.meuCursor()
        con = self.banco.con

        dado = ('''
            SELECT matricula FROM Aluno;
            ''')
        cur.execute(dado)
        lista = list(cur.fetchall(dado))
        if a.matricula not in lista:
            print("Aluno não cadastrado no banco de dados")
        else:

            cur.execute(f"""
            UPDATE Aluno SET idade = {a.idade},
            WHERE matricula = {a.matricula};
            """)
            con.commit()