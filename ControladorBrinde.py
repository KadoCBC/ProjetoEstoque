from entidades.Brinde import Brinde


class ControladorBrinde():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_brindes = []
    
    @property
    def lista_brindes(self):
        return self.__lista_brindes
    
    def incluir_brinde(self):
        pass

    def procura_brindes(self, nome_brinde):
        if len(self.lista_brindes) > 0:
            for brinde in self.lista_brindes:
                if nome_brinde == brinde.nome:
                    return brinde
        else:
            return #mensagem lis

