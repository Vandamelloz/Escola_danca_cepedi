#Importação da classe aluno para uso de chave estrangeira
from model.aluno_classe import Aluno

class Niveis():
    def __init__(self, id: int, nivel: str, aluno: Aluno, data_modificacao: str="dd-mm-aaaa"):
        self.id = id
        self.nivel = nivel
        self.aluno = aluno
        self.data_modificacao= data_modificacao
    
    def __str__(self):
        return f"id: {self.id}, nivel: {self.nivel}, aluno: {self.aluno.nome}, data de mudança de nivel:{self.data_modificacao}"