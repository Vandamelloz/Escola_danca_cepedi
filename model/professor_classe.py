class Professor:
    def __init__(self, id: int, nome: str, avaliador: str):
        self.__id = id
        self.__nome = nome
        self.__avaliador = avaliador.lower()

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Avaliador: {self.avaliador}"

    
    @property
    def id(self) -> int:
        return self.__id
    @property
    def nome(self) -> str:
        return self.__nome
    @property
    def avaliador(self) -> str:
        return self.__avaliador

    @id.setter
    def id(self, id: int):
        self.__id = id
    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    @avaliador.setter
    def avaliador(self, avaliador: str):
        self.__avaliador = avaliador.lower()
