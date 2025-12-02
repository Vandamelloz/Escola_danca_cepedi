import hashlib
from model.admin import Admin
from db.database import Banco
import sqlite3 

class ManipularAdmin:
    def __init__(self, db: Banco):
        self.db = db
     
        self.db.conectar()
    
    def _hash_senha(self, senha: str) -> str:
        """Função PRIVADA para criptografar uma senha usando SHA-256."""
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()

    # -------------------------------------------------------------------
    #CRUD BÁSICO
    # -------------------------------------------------------------------

    def criarTabelaAdmin(self) -> bool:
        """Cria a tabela Admin se não existir."""
        cur = self.db.meuCursor()
        con = self.db.con
        
        try:
            sql = """CREATE TABLE IF NOT EXISTS Admin (
                usuario TEXT PRIMARY KEY,
                senha TEXT NOT NULL
            );"""
            cur.execute(sql)
            con.commit()
            return True
        except sqlite3.Error as e:
            print(f"❌ Erro ao criar tabela Admin: {e}")
            return False

    def adicionarAdmin(self, admin: Admin) -> bool:
        """Adiciona um novo admin ao banco de dados."""
        cur = self.db.meuCursor()
        con = self.db.con
        
        try:
            # 1. Verifica se admin já existe
            cur.execute("SELECT usuario FROM Admin WHERE usuario = ?", (admin.usuario,))
            if cur.fetchone() is not None:
                print(f"⚠️ Erro: Admin '{admin.usuario}' já existe!")
                return False
            
            # 2. Criptografa a senha antes de salvar
            senha_hash = self._hash_senha(admin.senha)
            
            # 3. Insere no banco
            sql = "INSERT INTO Admin (usuario, senha) VALUES (?, ?)"
            cur.execute(sql, (admin.usuario, senha_hash))
            con.commit()
            
            return True
        except sqlite3.Error as e:
            con.rollback()
            print(f"❌ Erro ao adicionar admin: {e}")
            return False

    # -------------------------------------------------------------------
    ## 🔐 AUTENTICAÇÃO E ATUALIZAÇÃO SEGURA
    # -------------------------------------------------------------------

    def login(self, usuario: str, senha_pura: str) -> bool:
        """Valida login do admin."""
        cur = self.db.meuCursor()
        
        try:
            cur.execute("SELECT senha FROM Admin WHERE usuario = ?", (usuario,))
            resultado = cur.fetchone()
            
            if resultado is None:
                print(f"⚠️ Erro de login: Usuário '{usuario}' não encontrado!")
                return False
            
            senha_hash_db = resultado[0]
            senha_fornecida_hash = self._hash_senha(senha_pura)
            
            if senha_fornecida_hash == senha_hash_db:
                return True
            else:
                print("⚠️ Erro de login: Senha incorreta!")
                return False
        except sqlite3.Error as e:
            print(f"❌ Erro ao realizar login: {e}")
            return False

    def atualizarSenhaAdmin(self, usuario: str, senha_antiga_pura: str, senha_nova_pura: str) -> bool:
        """
        Atualiza a senha do admin após verificar a senha antiga.
        Este método implementa a lógica de segurança necessária para o Menu Admin.
        """
        cur = self.db.meuCursor()
        con = self.db.con
        
        # 1. Verifica se a senha antiga está correta (reutiliza a lógica de login)
        if not self.login(usuario, senha_antiga_pura):
            return False
            
        # 2. Criptografa a nova senha
        nova_senha_hash = self._hash_senha(senha_nova_pura)
        
        try:
            # 3. Atualiza a senha no banco
            sql = "UPDATE Admin SET senha = ? WHERE usuario = ?"
            cur.execute(sql, (nova_senha_hash, usuario))
            con.commit()
            
          
            if cur.rowcount == 0:
                print("⚠️ Aviso: Usuário não encontrado para atualização, apesar do login.")
                return False
            
            return True
        except sqlite3.Error as e:
            con.rollback()
            print(f"❌ Erro ao atualizar senha no banco: {e}")
            return False

    def listarAdmins(self):
        """Lista todos os admins (Método para o Menu Admin)."""
        cur = self.db.meuCursor()
        
        try:
            cur.execute("SELECT usuario FROM Admin")
            admins = cur.fetchall()

            if not admins:
                print("Nenhum admin cadastrado.")
                return

            print("\n--- Lista de Administradores ---")
            for admin in admins:
                print(f" • Usuário: {admin[0]}")
        except sqlite3.Error as e:
            print(f"❌ Erro ao listar admins: {e}")
            
