

class Brinde():
    def __init__(self, nome: str, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        self.__nome = nome
        self.__precos = []

    @property
    def nome(self):
        return self.__nome
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade    

