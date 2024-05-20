class Preco:
    def __init__(self, valor, data, id):
        self.__valor = valor
        self.__data = data
        self.__id = id

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
        
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
