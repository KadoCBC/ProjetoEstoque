from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario

class ControladorUsuario():

    def __init__(self, controlador_sistema):
        self.__usuarios = []
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def lista_usuario(self):
        return self.__usuarios
    
    def procura_usuario(self, id):
        if len(self.lista_usuario) > 0:
            for usuario in self.lista_usuario:
                if id == usuario.id:
                    return usuario
        else:
            return None

    def incluir_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        cria_id = len(self.lista_usuario)
        while self.procura_usuario(cria_id) is not None:
            cria_id = cria_id + 1
        usuario = Usuario(dados_usuario["nome"], cria_id)
        self.__usuarios.append(usuario)
    
    def listar_usuarios(self):
        if len(self.lista_usuario) == 0:
            self.__tela_usuario.mostrar_mensagem('Lista de Usuarios está vazia')
            return None  
        for usuario in self.lista_usuario:
            self.__tela_usuario.mostrar_usuario({"id": usuario.id, "nome": usuario.nome})

    def alterar_usuario(self):
        self.__tela_usuario.mostrar_mensagem('Alterar Usuario:')
        id_usuario = self.__tela_usuario.seleciona_usuario()
        #Fazer codigo para verificar se é inteiro
        usuario_alterar = self.procura_usuario(id_usuario)
        if isinstance(usuario_alterar, Usuario):
            dados_usuario = self.__tela_usuario.pega_dados_usuario()
            usuario_alterar.nome = dados_usuario["nome"]
        else:
            self.__tela_usuario.mostrar_mensagem('Usuario não encontrado!')
            
    
    def excluir_usuario(self):
        self.__tela_usuario.mostrar_mensagem('Excluir Usuario: ')
        id_usuario = self.__tela_usuario.seleciona_usuario()
        #Fazer codigo para verificar se é inteiro
        usuario_excluir = self.procura_usuario(id_usuario)
        if isinstance(usuario_excluir, Usuario):
            self.lista_usuario.remove(usuario_excluir)
        else:
            self.__tela_usuario.mostrar_mensagem('Usuario não encontrado!')
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_usuario, 2: self.listar_usuarios, 
                        3: self.alterar_usuario, 4: self.excluir_usuario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
