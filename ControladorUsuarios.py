from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario

class ControladorUsuario():

    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema

    def incluir_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        usuario = Usuario(dados_usuario["nome"], dados_usuario["id"])
        self.__usuarios.append(usuario)

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_usuario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()








