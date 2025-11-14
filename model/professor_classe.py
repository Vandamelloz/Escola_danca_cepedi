class Professor:
    def __init__(self, id: int, nome: str, avaliador: str):
        self.id = id
        self.nome = nome
        self.avaliador = avaliador.lower()

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Avaliador: {self.avaliador}"

    
