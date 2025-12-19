import sqlite3
from model.niveis_classe import Niveis
from model.aluno_classe import Aluno
from db.database import Banco


class ManipularNiveis:
    def __init__(self, db: Banco):
        self.db = db
        self.db.conectar()

    def criarTabela(self):
        """Cria a tabela Niveis se não existir."""
        cur = self.db.meuCursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Niveis (
            id INTEGER PRIMARY KEY,
            nivel TEXT NOT NULL,
            aluno_id INTEGER NOT NULL,
            data_modificacao TEXT,
            FOREIGN KEY(aluno_id) REFERENCES Aluno(id)
        );
        """)
        self.db.con.commit()
        print("Tabela 'Niveis' criada (ou já existente).")

    def adicionarNivel(self, n: Niveis):
        """Adiciona um novo nível ou atualiza caso já exista."""
        cur = self.db.meuCursor()
        con = self.db.con

        cur.execute("SELECT id FROM Niveis WHERE id = ?", (n.id,))
        existe = cur.fetchone()

        if existe is None:
            cur.execute("""
                INSERT INTO Niveis (id, nivel, aluno_id, data_modificacao)
                VALUES (?, ?, ?, ?)
            """, (n.id, n.nivel, n.aluno.id, n.data_modificacao))
            con.commit()
            print(f"Nível '{n.nivel}' adicionado para o aluno '{n.aluno.nome}'.")
        else:
            cur.execute("""
                UPDATE Niveis
                SET nivel = ?, aluno_id = ?, data_modificacao = ?
                WHERE id = ?
            """, (n.nivel, n.aluno.id, n.data_modificacao, n.id))
            con.commit()
            print(f"Nível do aluno '{n.aluno.nome}' atualizado para '{n.nivel}'.")

    def listarNiveis(self):
        """Lista todos os níveis cadastrados."""
        cur = self.db.meuCursor()
        cur.execute("""
        SELECT N.id, N.nivel, N.data_modificacao, A.id, A.nome
        FROM Niveis N
        JOIN Aluno A ON N.aluno_id = A.id;
        """)
        resultados = cur.fetchall()

        niveis = []
        for r in resultados:
            aluno = Aluno(id=r[3], nome=r[4], nivel=None)
            n = Niveis(id=r[0], nivel=r[1], aluno=aluno, data_modificacao=r[2])
            niveis.append(n)

        return niveis

    def excluirNivel(self, id: int):
        """Exclui um registro de nível pelo ID."""
        cur = self.db.meuCursor()
        cur.execute("DELETE FROM Niveis WHERE id = ?", (id,))
        self.db.con.commit()
        print(f"Registro de nível com ID {id} removido com sucesso.")
