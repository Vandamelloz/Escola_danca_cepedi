#Importação da classe aluno para uso de chave estrangeira
from model.aluno_classe import Aluno

class Niveis():
    def __init__(self, id: int, nivel: str, aluno: Aluno):
        self.id = id
        self.nivel = nivel
        self.aluno = aluno
    
    def __str__(self):
        return f"id: {self.id}, nivel: {self.nivel}, aluno: {self.aluno.nome}"