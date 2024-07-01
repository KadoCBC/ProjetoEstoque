from DAOs.Dao import DAO
from entidades.CategoriaBrinde import CategoriaBrinde


class CategoriaDAO(DAO):
    def __init__(self):
        super().__init__('categoria.pkl')
    
    def add(self, categoria: CategoriaBrinde):
        if((categoria is not None) and isinstance(categoria, CategoriaBrinde) and isinstance(categoria.nome, str)):
            super().add(categoria.nome, categoria)
    
    def update(self, categoria: CategoriaBrinde):
        if((categoria is not None) and isinstance(categoria, CategoriaBrinde) and isinstance(categoria.nome, str)):
            super().update(categoria.nome, categoria)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)
        
    
    
