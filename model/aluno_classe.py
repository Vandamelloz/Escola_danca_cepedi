
class Aluno:
    def __init__(self, id, matricula, nome, idade, nivelCondutor, nivelConduzido, dataNivelCondutor=None, dataNivelConduzido=None):
        self.id = id
        self.matricula = matricula
        self.nome = nome
        self.idade = idade
        self.nivelCondutor = nivelCondutor
        self.nivelConduzido = nivelConduzido
        self.dataNivelCondutor = dataNivelCondutor
        self.dataNivelConduzido = dataNivelConduzido

    def __str__(self):
        return f"ID: {self.id} | Matrícula: {self.matricula} | Nome: {self.nome} | Idade: {self.idade} | Nível Condutor: {self.nivelCondutor} | Nível Conduzido: {self.nivelConduzido}"

    def __repr__(self):
        return self.__str__()