from telas.TelaUsuario import TelaUsuario
from entidades.Usuario import Usuario
from DAOs.Usuario_dao import UsuarioDAO

class ControladorUsuario():

    def __init__(self, controlador_sistema):
        self.__usuario_DAO = UsuarioDAO()
        self.__tela_usuario = TelaUsuario()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def lista_usuario(self):
        return self.__usuario_DAO.get_all()
    
    def procura_usuario(self, id):
        if len(self.lista_usuario) > 0:
            for usuario in self.lista_usuario:
                if id == usuario.id:
                    print('tb')
                    return usuario
        else:
            return None

    def incluir_usuario(self):
        dados_usuario = self.__tela_usuario.pega_dados_usuario()
        nome = dados_usuario["nome"]
        try:
            if nome == '':
                raise KeyError
            else:
                cria_id = len(self.lista_usuario)
                while self.procura_usuario(cria_id) is not None:
                    cria_id = cria_id + 1
                usuario = Usuario(nome, cria_id)
                self.__usuario_DAO.add(usuario)
        except KeyError:
            self.__tela_usuario.mostrar_mensagem('Campo de Nome vazio, tente novamente!')

    def listar_usuarios(self):
        if len(self.lista_usuario) == 0:
            self.__tela_usuario.mostrar_mensagem('Lista de Usuarios está vazia')
            return None
        dados_usuario = []
        for usuario in self.lista_usuario:
            dados_usuario.append({"id": usuario.id, "nome": usuario.nome})
        self.__tela_usuario.mostrar_usuario(dados_usuario)

    def alterar_usuario(self):
        id_usuario = self.__tela_usuario.seleciona_usuario()
        if id_usuario == None:
            return
        usuario_alterar = self.procura_usuario(id_usuario)
        try:
            if usuario_alterar == None:
                raise KeyError
            else:
                dados_usuario = self.__tela_usuario.pega_dados_usuario()
                usuario_alterar.nome = dados_usuario["nome"]
                self.__usuario_DAO.update(usuario_alterar)

        except KeyError:
            self.__tela_usuario.mostrar_mensagem('Usuario não existe')
            
    def excluir_usuario(self):
        id_usuario = self.__tela_usuario.seleciona_usuario()
        if id_usuario == None:
            return
        usuario_excluir = self.procura_usuario(id_usuario)
        try:
            if usuario_excluir == None:
                raise KeyError
            else:
                self.__usuario_DAO.remove(usuario_excluir.id)

        except KeyError:
            self.__tela_usuario.mostrar_mensagem('Usuario não existe')
            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_usuario, 2: self.listar_usuarios, 
                        3: self.alterar_usuario, 4: self.excluir_usuario, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_usuario.tela_opcoes()]()
