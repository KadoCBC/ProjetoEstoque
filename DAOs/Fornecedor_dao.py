from DAOs.Dao import DAO
from entidades.Fornecedor import Fornecedor


class FornecedorDAO(DAO):
    def __init__(self):
        super().__init__('fornecedor.pkl')
    
    def add(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.id, int)):
            super().add(fornecedor.id, fornecedor)
    
    def update(self, fornecedor: Fornecedor):
        if((fornecedor is not None) and isinstance(fornecedor, Fornecedor) and isinstance(fornecedor.id, int)):
            super().update(fornecedor.id, fornecedor)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
        
    
    
