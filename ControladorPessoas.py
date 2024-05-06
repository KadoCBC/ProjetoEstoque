from TelaPessoas import TelaPessoas
from Usuario import Usuario
from Fornecedor import Fornecedor

class ControladorPessoas():

    def __init__(self):
        self.__usuarios = []
        self.__fornecedores = []
        self.__tela_pessoa = TelaPessoas()

    def incluir_usuario(self):
        dados_usuario = self.__tela_pessoa.pega_dados_usuario()
        usuario = Usuario(dados_usuario["nome"], dados_usuario["id"])
        self.__usuarios.append(usuario)

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_usuario}

        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()




c1 = ControladorPessoas()

c1.abre_tela()

