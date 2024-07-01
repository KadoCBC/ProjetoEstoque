from DAOs.Dao import DAO
from entidades.Endereco import Endereco

class EnderecoDAO(DAO):
    def __init__(self):
        super().__init__('endereco.pkl')
    
    def add(self, endereco: Endereco):
        if((endereco is not None) and isinstance(endereco, Endereco) and isinstance(endereco.nome, str)):
            super().add(endereco.nome, endereco)
    
    def update(self, endereco: Endereco):
        if((endereco is not None) and isinstance(endereco, Endereco) and isinstance(endereco.nome, str)):
            super().update(endereco.nome, endereco)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)