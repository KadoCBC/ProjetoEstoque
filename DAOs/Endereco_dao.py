from DAOs.Dao import DAO
from entidades.Endereco import Endereco

class EnderecoDAO(DAO):
    def __init__(self):
        super().__init__('enderecos.pkl')

    def add(self, endereco: Endereco):
        if endereco is not None and isinstance(endereco, Endereco):
            super().add(endereco.rua, endereco)

    def update(self, endereco: Endereco):
        if endereco is not None and isinstance(endereco, Endereco):
            super().update(endereco.rua, endereco)

    def get(self, key: str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key: str):
        if isinstance(key, str):
            return super().remove(key)
