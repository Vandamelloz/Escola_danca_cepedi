import sqlite3
from db.database import Banco
from model.exame_classe import Exame


class ManipularExame:
    def __init__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def salvarExame(self, exame: Exame, id_aluno: int, id_professor: int):
        """Salva um novo exame no banco de dados."""
        cur = self.db.meuCursor()
        con = self.db.con

        # Verifica se aluno existe
        cur.execute("SELECT id FROM Aluno WHERE id = ?", (id_aluno,))
        if cur.fetchone() is None:
            print("Erro: Aluno não cadastrado no banco!")
            return False

        # Verifica se professor existe
        cur.execute("SELECT id FROM Professor WHERE id = ?", (id_professor,))
        if cur.fetchone() is None:
            print("Erro: Professor não cadastrado no banco!")
            return False

        try:
            sql = """INSERT INTO Exame (id_aluno, id_professor, ConducaoResposta, Abraco, Mecanica, Ritmo, Marcacao, data_exame)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?);"""
            
            cur.execute(sql, (
                id_aluno,
                id_professor,
                exame.conducao_resposta,
                exame.abraco,
                exame.mecanica,
                exame.ritmo,
                exame.marcacao,
                exame.data_exame
            ))
            
            con.commit()
            print("Exame salvo com sucesso!")
            return True
        except sqlite3.IntegrityError as e:
            con.rollback()
            print(f"Erro de integridade ao salvar exame: {e}")
            return False
        except Exception as e:
            con.rollback()
            print(f"Erro ao salvar exame: {e}")
            return False

    def listarExames(self):
        """Lista todos os exames cadastrados."""
        cur = self.db.meuCursor()
        
        try:
            sql = """SELECT id, id_aluno, id_professor, ConducaoResposta, Abraco, Mecanica, Ritmo, Marcacao, data_exame
                     FROM Exame ORDER BY data_exame DESC;"""
            
            cur.execute(sql)
            resultados = cur.fetchall()
            
            if not resultados:
                print("Nenhum exame cadastrado.")
                return
            
            print("\n=== LISTA DE EXAMES ===")
            for row in resultados:
                print(f"ID: {row[0]} | Aluno ID: {row[1]} | Professor ID: {row[2]} | "
                      f"Condução: {row[3]} | Abraço: {row[4]} | Mecânica: {row[5]} | "
                      f"Ritmo: {row[6]} | Marcação: {row[7]} | Data: {row[8]}")
        except Exception as e:
            print(f"Erro ao listar exames: {e}")

    def atualizarExame(self, id_exame: int, exame: Exame):
        """Atualiza um exame existente."""
        cur = self.db.meuCursor()
        con = self.db.con

        # Verifica se exame existe
        cur.execute("SELECT id FROM Exame WHERE id = ?", (id_exame,))
        if cur.fetchone() is None:
            print("Erro: Exame não encontrado!")
            return False

        try:
            sql = """UPDATE Exame
                     SET ConducaoResposta = ?, Abraco = ?, Mecanica = ?, Ritmo = ?, Marcacao = ?, data_exame = ?
                     WHERE id = ?;"""
            
            cur.execute(sql, (
                exame.conducao_resposta,
                exame.abraco,
                exame.mecanica,
                exame.ritmo,
                exame.marcacao,
                exame.data_exame,
                id_exame
            ))
            
            con.commit()
            print("Exame atualizado com sucesso!")
            return True
        except Exception as e:
            con.rollback()
            print(f"Erro ao atualizar exame: {e}")
            return False

    def excluirExame(self, id_exame: int):
        """Exclui um exame do banco de dados."""
        cur = self.db.meuCursor()
        con = self.db.con

        # Verifica se exame existe
        cur.execute("SELECT id FROM Exame WHERE id = ?", (id_exame,))
        if cur.fetchone() is None:
            print("Erro: Exame não encontrado!")
            return False

        try:
            sql = "DELETE FROM Exame WHERE id = ?;"
            cur.execute(sql, (id_exame,))
            con.commit()
            print("Exame excluído com sucesso!")
            return True
        except Exception as e:
            con.rollback()
            print(f"Erro ao excluir exame: {e}")
            return False

    def listarExamesPorAluno(self, id_aluno: int):
        """Lista todos os exames de um aluno específico."""
        cur = self.db.meuCursor()
        
        try:
            sql = """SELECT id, id_aluno, id_professor, ConducaoResposta, Abraco, Mecanica, Ritmo, Marcacao, data_exame
                     FROM Exame WHERE id_aluno = ? ORDER BY data_exame DESC;"""
            
            cur.execute(sql, (id_aluno,))
            resultados = cur.fetchall()
            
            if not resultados:
                print(f"Nenhum exame cadastrado para o aluno ID {id_aluno}.")
                return
            
            print(f"\n=== EXAMES DO ALUNO ID {id_aluno} ===")
            for row in resultados:
                print(f"ID: {row[0]} | Professor ID: {row[2]} | "
                      f"Condução: {row[3]} | Abraço: {row[4]} | Mecânica: {row[5]} | "
                      f"Ritmo: {row[6]} | Marcação: {row[7]} | Data: {row[8]}")
        except Exception as e:
            print(f"Erro ao listar exames por aluno: {e}")