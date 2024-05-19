from entidades.PessoaAbstract import Pessoa
from entidades.Endereco import Endereco

class Fornecedor(Pessoa):
    def __init__(self, nome: str, id: int):
        super().__init__(nome, id)
        self.__endereco = None
    
    def adicionar_endereco(self, rua, complemento, bairro, cidade, cep):
        self.__endereco = Endereco(rua, complemento, bairro, cidade, cep)

    def deletar_endereco(self):
        self.__endereco = None
        print("Endereço deletado com sucesso.")

    def exibir_fornecedor(self):
        print(f"Fornecedor: {self.__nome}")
        print(f"ID: {self.__id}")
        if self.__endereco:
            print(f"Endereço: {self.__endereco.mostra_endereco()}")
        else:
            print("Endereço: Não cadastrado")