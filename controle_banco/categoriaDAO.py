import sqlite3
from db.database import Banco
from model.

class ManipularCategoria:
    def __init__(self, db: Banco):
        self.db = db
    
    def adicionar
