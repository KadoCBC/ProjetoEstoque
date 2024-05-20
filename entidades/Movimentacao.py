from datetime import datetime


class Movimentacao():

    def __init__(self, qt_mov, instituidor, motivo, codigo, brinde, responsavel):
        self.__qt_mov = qt_mov
        self.__instituidor = instituidor
        self.__motivo = motivo
        self.__data = datetime.today()
        self.__codigo = codigo
        self.__brinde = brinde
        self.__responsavel = responsavel
        if qt_mov >= 0: 
            self.__tipo_mov = 'Entrada'
        else:
            self.__tipo_mov = 'Saida'
    
    @property
    def qt_mov(self):
        return self.__qt_mov
    
    @property
    def instituidor(self):
        return self.__instituidor
    
    @property
    def motivo(self):
        return self.__motivo
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def brinde(self):
        return self.__brinde
    
    @property
    def tipo_mov(self):
        return self.__tipo_mov
    
    @property
    def data(self):
        return self.__data
    
    @property
    def responsavel(self):
        return self.__responsavel
