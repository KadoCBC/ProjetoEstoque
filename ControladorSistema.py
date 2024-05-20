from telas.TelaSistema import TelaSistema
from ControladorUsuarios import ControladorUsuario
from ControladorBrinde import ControladorBrinde
from ControladorMov import ControladorMov
from ControladorPreco import ControladorPreco
from ControladorCategoriaBrinde import ControladorCategoriaBrinde
from ControladorFornecedor import ControladorFornecedor

class ControladorSistema():
    
    def __init__(self):
        self.__controlador_usuario = ControladorUsuario(self)
        self.__controlador_brinde = ControladorBrinde(self)
        self.__controlador_mov = ControladorMov(self)
        self.__tela_sistema = TelaSistema()
        self.__controlador_preco = ControladorPreco(self)
        self.__controlador_categoria_brinde = ControladorCategoriaBrinde(self)
        self.__controlador_fornecedor = ControladorFornecedor(self)

    @property
    def controlador_usuario(self):
        return self.__controlador_usuario
    
    @property
    def controlador_brinde(self):
        return self.__controlador_brinde
    
    @property
    def controlador_mov(self):
        return self.__controlador_mov
    
    @property
    def controlador_preco(self):
        return self.__controlador_preco

    @property
    def controlador_categoria_brinde(self):
        return self.__controlador_categoria_brinde
    
    @property
    def controlador_fornecedor(self):
        return self.__controlador_fornecedor
    
    def inicializador_sistema(self):
        self.abre_tela()
    
    def cadastra_usuario(self):
        self.__controlador_usuario.abre_tela()
    
    def cadastra_brinde(self):
        self.controlador_brinde.abre_tela()
    
    def cadastra_movimentacao(self):
        self.__controlador_mov.abre_tela()

    def cadastra_preco(self):
        self.__controlador_preco.abre_tela()

    def cadastra_categoria(self):
        self.__controlador_categoria_brinde.abre_tela()

    def cadastra_fornecedor(self):
        self.__controlador_fornecedor.abre_tela()
    
    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.cadastra_usuario, 2: self.cadastra_fornecedor, 
                        3: self.cadastra_brinde, 4:self.cadastra_movimentacao, 
                        5: self.cadastra_preco, 6: self.cadastra_categoria,
                        0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
   