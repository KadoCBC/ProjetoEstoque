class Endereco:
    def __init__(self, rua, complemento, bairro, cidade, cep):
        self.__rua = rua
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep

    @property
    def rua(self):
        return self.__rua
    
    @property
    def complemento(self):
        return self.__complemento
    
    @property
    def bairro(self):
        return self.__bairro
    
    @property
    def cidade(self):
        return self.__cidade
    
    @property
    def cep(self):
        return self.__cep