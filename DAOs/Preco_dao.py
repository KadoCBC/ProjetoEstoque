from DAOs.Dao import DAO
from entidades.Preco import Preco


class PrecoDAO(DAO):
    def __init__(self):
        super().__init__('preco.pkl')
    
    def add(self, preco: Preco):
        if((preco is not None) and isinstance(preco, Preco) and isinstance(preco.id, str)):
            super().add(preco.id, preco)
    
    def update(self, preco: Preco):
        if((preco is not None) and isinstance(preco, Preco) and isinstance(preco.id, str)):
            super().update(preco.id, preco)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)