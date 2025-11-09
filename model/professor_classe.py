import sqlite3
from banco.database import Banco

class Professor:
    def __init__(self, nome:str, id:int, avaliador:str):
        self.nome=nome
        self.id=id
        self.avaliador=avaliador.lower()
        
    def imprimirProfessor(self):
        print(f"Nome do avaliador: {self.nome}, id: {self.id}, avaliador: {self.avaliador}")
    
