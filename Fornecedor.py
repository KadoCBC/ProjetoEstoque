from PessoaAbstract import Pessoa
from endereco import Endereco

class Fornecedor(Pessoa):
    def __init__(self, nome: str, id: int):
        super().__init__(nome, id)
        self.__endereco = ''
    
    @property
    def endereco(self):
        return self.__endereco
    
    @endereco.setter
    def endereco(self, endereco: Endereco):
        self.__endereco = endereco