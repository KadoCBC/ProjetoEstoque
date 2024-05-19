class Preco:
    def __init__(self, valor, data):
        self.__valor = valor
        self.__data = data

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, valor):
        self.__valor = valor

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data = data