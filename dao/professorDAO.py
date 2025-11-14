import sqlite3
from model.professor_classe import Professor
from db.database import Banco

class ManipularProfessor:
    def __init__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def adicionarProfessor(self, p: Professor):
        cur = self.db.meuCursor()
        con = self.db.con

        # Verifica se já existe professor com esse ID
        cur.execute("SELECT id FROM Professor WHERE id = ?", (p.id,))
        existe = cur.fetchone()

        if existe is None:
            try:
                cur.execute("""
                    INSERT INTO Professor (id, nome, avaliador) 
                    VALUES (?, ?, ?)
                """, (p.id, p.nome, p.avaliador))
                con.commit()
                print(f"Professor '{p.nome}' adicionado com sucesso!")
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao adicionar professor: {e}")
                return False
        else:
            try:
                cur.execute("""
                    UPDATE Professor 
                    SET nome = ?, avaliador = ?
                    WHERE id = ?
                """, (p.nome, p.avaliador, p.id))
                con.commit()
                print(f"Professor '{p.nome}' atualizado com sucesso!")
                return True
            except Exception as e:
                con.rollback()
                print(f"Erro ao atualizar professor: {e}")
                return False
    def listarProfessores(self):
        cur = self.db.meuCursor()
        try:
            cur.execute("SELECT id, nome, avaliador FROM Professor")
            resultados = cur.fetchall()
            
            if not resultados:
                print("Nenhum professor cadastrado.")
                return []
            
            print("\n=== LISTA DE PROFESSORES ===")
            professores = []
            for r in resultados:
                prof = Professor(id=r[0], nome=r[1], avaliador=r[2])
                print(prof)
                professores.append(prof)
            return professores
        except Exception as e:
            print(f"Erro ao listar professores: {e}")
            return []
  

    def excluirProfessor(self, id: int):
        cur = self.db.meuCursor()
        con = self.db.con
        
        # Verifica se professor existe
        cur.execute("SELECT id FROM Professor WHERE id = ?", (id,))
        if cur.fetchone() is None:
            print(f"Erro: Professor com ID {id} não encontrado!")
            return False
        
        try:
            cur.execute("DELETE FROM Professor WHERE id = ?", (id,))
            con.commit()
            print(f"Professor com ID {id} removido com sucesso!")
            return True
        except Exception as e:
            con.rollback()
            print(f"Erro ao excluir professor: {e}")
            return False

    def obterProfessorPorId(self, id: int):
        """Obtém um professor específico pelo ID."""
        cur = self.db.meuCursor()
        try:
            cur.execute("SELECT * FROM Professor WHERE id = ?", (id,))
            resultado = cur.fetchone()
            
            if resultado is None:
                print(f"Professor com ID {id} não encontrado.")
                return None
            
            return Professor(id=resultado[0], nome=resultado[1], avaliador=resultado[2])
        except Exception as e:
            print(f"Erro ao obter professor: {e}")
            return None
