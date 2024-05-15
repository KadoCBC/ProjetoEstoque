

class TipoMovimentacao():
    
    def __init__(self, tipo_de_mov: int):
        if tipo_de_mov >= 0:
            self.__tipo_de_mov = 'Saida'
        else:
            self.__tipo_de_mov = 'Entrada'
    
    @property
    def tipo_de_mov(self):
        return self.__tipo_de_mov