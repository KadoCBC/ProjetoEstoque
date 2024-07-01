from DAOs.Dao import DAO
from entidades.Brinde import Brinde


class BrindeDAO(DAO):
    def __init__(self):
        super().__init__('brindes.pkl')
    
    def add(self, brinde: Brinde):
        if((brinde is not None) and isinstance(brinde, Brinde) and isinstance(brinde.id, int)):
            super().add(brinde.id, brinde)
    
    def update(self, brinde: Brinde):
        if((brinde is not None) and isinstance(brinde, Brinde) and isinstance(brinde.id, int)):
            super().update(brinde.id, brinde)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)