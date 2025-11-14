import hashlib
from model.admin import Admin
from db.database import Banco

class ManipularAdmin:
    def __init__(self, db: Banco):
        self.db = db
        self.db.conectar()
    
    def criarSenha(self, senha: str) -> str:
        """Criptografa uma senha em SHA-256."""
        return hashlib.sha256(senha.encode('utf-8')).hexdigest()

    def adicionarAdmin(self, admin: Admin) -> bool:
        """Adiciona um novo admin ao banco de dados."""
        cur = self.db.meuCursor()
        con = self.db.con
        
        try:
            # Verifica se admin já existe
            cur.execute("SELECT usuario FROM Admin WHERE usuario = ?", (admin.usuario,))
            if cur.fetchone() is not None:
                print(f"Erro: Admin '{admin.usuario}' já existe!")
                return False
            
            # Criptografa a senha
            senha_hash = self.criarSenha(admin.senha)
            
            # Insere no banco
            sql = "INSERT INTO Admin (usuario, senha) VALUES (?, ?)"
            cur.execute(sql, (admin.usuario, senha_hash))
            con.commit()
            
            print(f"Admin '{admin.usuario}' adicionado com sucesso!")
            return True
        except Exception as e:
            con.rollback()
            print(f"Erro ao adicionar admin: {e}")
            return False

    def login(self, usuario: str, senha: str) -> bool:
        """Valida login do admin."""
        cur = self.db.meuCursor()
        
        try:
            cur.execute("SELECT usuario, senha FROM Admin WHERE usuario = ?", (usuario,))
            resultado = cur.fetchone()
            
            if resultado is None:
                print(f"Erro: Usuário '{usuario}' não encontrado!")
                return False
            
            usuario_db, senha_hash = resultado
            senha_fornecida_hash = self.criarSenha(senha)
            
            if senha_fornecida_hash == senha_hash:
                print(f"Login bem-sucedido! Bem-vindo, {usuario}!")
                return True
            else:
                print("Erro: Senha incorreta!")
                return False
        except Exception as e:
            print(f"Erro ao realizar login: {e}")
            return False

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
            print("Tabela 'Admin' criada/verificada com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao criar tabela Admin: {e}")
            return False