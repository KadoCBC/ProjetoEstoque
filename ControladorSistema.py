from telas.TelaSistema import TelaSistema
from ControladorUsuarios import ControladorUsuario

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__tela_sistema = TelaSistema()

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    def inicialidor_sistema(self):
        self.abre_tela()
    
    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()
    
    def encerra_sistema(self):
        exit(0)


    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()


c1 = ControladorSistema()
c1.inicialidor_sistema()