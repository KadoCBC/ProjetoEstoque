from DAOs.Dao import DAO
from entidades.Movimentacao import Movimentacao

class MovimentacaoDAO(DAO):
    def __init__(self):
        super().__init__('movimentacao.pkl')
    
    def add(self, movimentacao: Movimentacao):
        if((movimentacao is not None) and isinstance(movimentacao, Movimentacao) and isinstance(movimentacao.codigo, int)):
            super().add(movimentacao.codigo, movimentacao)
    
    def update(self, movimentacao: Movimentacao):
        if((movimentacao is not None) and isinstance(movimentacao, Movimentacao) and isinstance(movimentacao.codigo, int)):
            super().update(movimentacao.codigo, movimentacao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(self, key:int):
        if(isinstance(key, int)):
            return super().remove(key)