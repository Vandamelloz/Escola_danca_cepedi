
class Aluno():

    def __init__(self, nome: str, matricula: int, idade: int, 
                 nivelCondutor: str = "Branco", nivelConduzido: str = "Branco", 
                 dataNivelConduzido: str = "dd-mm-aaaa", dataNivelCondutor: str = "dd-mm-aaaa"):
        
        self.nome = nome
        self.matricula = matricula
        self.idade = idade
        self.nivelConduzido = nivelConduzido
        self.nivelCondutor = nivelCondutor
        self.dataNivelConduzido = dataNivelConduzido
        self.dataNivelCondutor = dataNivelCondutor
    
    def __str__(self):
        return (f"(nome: {self.nome}, matricula: {self.matricula}, )",
                f"idade: {self.idade}, nivel conduzido: {self.nivelConduzido}",
                f"nivel condutor: {self.nivelCondutor}, data que conduz: {self.dataNivelCondutor}",
                f"data que é conduzido {self.dataNivelConduzido}")