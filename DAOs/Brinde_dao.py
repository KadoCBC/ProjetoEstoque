from DAOs.Dao import DAO
from entidades.Brinde import Brinde

class BrindeDAO(DAO):
    def __init__(self):
        super().__init__('brindes.pkl')
    
    def add(self, brinde: Brinde):
        if((brinde is not None) and isinstance(brinde, Brinde) and isinstance(brinde.nome, str)):
            super().add(brinde.nome, brinde)
    
    def update(self, brinde: Brinde):
        if((brinde is not None) and isinstance(brinde, Brinde) and isinstance(brinde.nome, str)):
            super().update(brinde.nome, brinde)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)