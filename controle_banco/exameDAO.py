import sqlite3
from banco.database import Banco
from model.exame_classe import Exame
from model.aluno_classe import Aluno
from model.professor_classe import Professor

class ManipularExame:
    def __init__(self, db: Banco, a: Aluno, p: Professor):
        self.banco = db
        self.banco.conectar()
        self.a = a
        self.p = p
    
    def salvarExame(self, e: Exame):
        cur = self.banco.meuCursor()
        con = self.banco.con

        exame = '''
        INSERT INTO Exame (id_aluno, id_professor, ConducaoResposta, Abraco, Mecanica, Ritmo, Marcacao, data_exame)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);'''(self.a.id, self.p.id_professor, e.conducao_resposta, 
                                           e.abraco, e.mecanica, e.ritmo, e.marcacao,e.data_exame)
        print(exame)
        cur.execute(exame)
        con.commit()
        print("Exame salvo com sucesso!")

if __name__ == "__main__":
    meu_banco = Banco()
    aluno = Aluno(nome = "sla", matricula = 22)
    professor = Professor(nome = "prof", id= 1, avaliador = "sim")
    exame = ManipularExame(meu_banco, aluno, professor)
    exame.salvarExame(exame)