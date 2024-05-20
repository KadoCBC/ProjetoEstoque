

class Brinde():
    def __init__(self, nome: str, quantidade: int):
        if isinstance(quantidade, int):
            self.__quantidade = quantidade
        else:
            self.__quantidade = 0
        self.__nome = nome
        self.__precos = []
        self.__categoria_brinde = "Geral"

    @property
    def nome(self):
        return self.__nome
    
    @property
    def quantidade(self):
        return self.__quantidade
    
    @property
    def categoria_brinde(self):
        return self.__categoria_brinde
    
    @property
    def lista_precos(self):
        return self.__precos
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    
    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @categoria_brinde.setter
    def categoria_brinde(self, categoria_brinde):
        self.__categoria_brinde = categoria_brinde
    
    def add_preco(self, preco):
        self.lista_precos.append(preco)
    
    def preco_atual(self):
        tamanho_lista = len(self.__precos)
        if tamanho_lista > 0:
            return self.lista_precos[tamanho_lista - 1]
        else:
            return None
