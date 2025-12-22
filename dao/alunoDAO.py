# ...existing code...
import sqlite3
from model.aluno_classe import Aluno
from db.database import Banco


class ManipularAluno:
    def __init__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def adicionarAluno(self, a: Aluno):
        cur = self.db.meuCursor()
        con = self.db.con
        cur.execute("SELECT id FROM Aluno WHERE id = ?", (a.id,))
        existe = cur.fetchone()  # VERIFICA SE O ITEM EXISTE
        if existe is None:
            sql = """INSERT INTO Aluno (id, Matricula, Nome, Idade, Nivel_Condutor, Nivel_Conduzido, dataNivelCondutor, dataNivelConduzido)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
            cur.execute(sql, (a.id, a.matricula, a.nome, a.idade, a.nivelCondutor, a.nivelConduzido, a.dataNivelCondutor, a.dataNivelConduzido))
            con.commit()
            print(f"Aluno {a.nome} adicionado com sucesso!")
        else:
            print("\nId já sendo utilizado")

    def atualizarDadosPessoasAluno(self, a: Aluno):
        cur = self.db.meuCursor()
        con = self.db.con

        cur.execute("SELECT id FROM Aluno WHERE id = ?", (a.id,))
        existe = cur.fetchone()
        if existe is None:
            print("Usuário não cadastrado no banco!")
        else:
            sql = """UPDATE Aluno
                     SET Idade = ?, Nivel_Condutor = ?, Nivel_Conduzido = ?, dataNivelCondutor = ?, dataNivelConduzido = ?
                     WHERE id = ?;"""
            cur.execute(sql, (a.idade, a.nivelCondutor, a.nivelConduzido, a.dataNivelCondutor, a.dataNivelConduzido, a.id))
            con.commit()
    # ...existing code...
    def listar_alunos(self):
        cur = self.db.meuCursor()
        cur.execute("SELECT id, Matricula, Nome, Idade, Nivel_Condutor, Nivel_Conduzido FROM Aluno")
        resultados = cur.fetchall()
        print("Lista de Alunos:")
        for row in resultados:
            aluno = Aluno(id=row[0], matricula=row[1], nome=row[2], idade=row[3], nivelCondutor=row[4], nivelConduzido=row[5])
            print(aluno)
     