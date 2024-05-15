

class Movimentacao():

    def __init__(self, qt_mov, instituidor, motivo, data, codigo, brinde, tipo_mov):
        self.__qt_mov = qt_mov
        self.__instituidor = instituidor
        self.__motivo = motivo
        self.__data = data
        self.__codigo = codigo
        self.__brinde = brinde
        self.__tipo_mov = tipo_mov
    
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
    
    @qt_mov.setter
    def qt_mov(self, qt: int):
        self.__qt_mov = qt
    
    @motivo.setter
    def motivo(self, motivo: str):
        self.__motivo = motivo
    
    @instituidor.setter
    def instituidor(self, instituidor: str):
        self.__instituidor = instituidor
    

    

