class Endereco:
    def __init__(self, rua, complemento, bairro, cidade, cep):
        self.rua = rua
        self.__complemento = complemento
        self.__bairro = bairro
        self.__cidade = cidade
        self.__cep = cep

    def mostra_endereco(self):
        return f"{self.__rua}, {self.__complemento}, {self.__bairro}, {self.__cidade}, {self.__cep}"