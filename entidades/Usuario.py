from entidades.PessoaAbstract import Pessoa

class Usuario(Pessoa):
    def __init__(self, nome: str, id: int):
        super().__init__(nome, id)
