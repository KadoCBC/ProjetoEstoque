from entidades.PessoaAbstract import Pessoa
from entidades.Endereco import Endereco

class Fornecedor(Pessoa):
    def __init__(self, nome: str, id: int):
        super().__init__(nome, id)
        self.__endereco = None 
    
    def adicionar_endereco(self, endereco):
        self.__endereco = endereco
    