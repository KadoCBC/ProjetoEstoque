from entidades.Preco import Preco
from telas.TelaPreco import TelaPreco

class ControladorPreco:
    def __init__(self):
        self.__lista_precos = []
        self.__tela_preco = TelaPreco()
    
    @property
    def lista_precos(self):
        return self.__lista_precos
    
    def incluir_preco(self, preco):
        self.__lista_precos.append(preco)

    def excluir_preco(self, valor):
        for preco in self.__lista_precos:
            if valor == preco.valor:
                self.__lista_precos.remove(preco)

    def listar_precos(self):
        pass
    
    