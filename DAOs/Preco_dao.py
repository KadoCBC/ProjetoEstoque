from DAOs.Dao import DAO
from entidades.Preco import Preco


class PrecoDAO(DAO):
    def __init__(self):
        super().__init__('preco.pkl')
    
    def add(self, preco: Preco):
        if((preco is not None) and isinstance(preco, Preco) and isinstance(preco.valor, int)):
            super().add(preco.valor, preco)
    
    def update(self, preco: Preco):
        if((preco is not None) and isinstance(preco, Preco) and isinstance(preco.valor, int)):
            super().update(preco.valor, preco)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)