from entidades.CategoriaBrinde import CategoriaBrinde
from DAOs.Categoria_dao import CategoriaDAO
from telas.TelaCategoriaBrinde import TelaCategoriaBrinde

class ControladorCategoriaBrinde():

    def __init__(self, controlador_sistema):
        self.__categoria_DAO = CategoriaDAO()
        self.__tela_categoria_brinde = TelaCategoriaBrinde()
        self.__controlador_sistema = controlador_sistema
    
    @property
    def lista_categoria(self):
        return self.__categoria_DAO.get_all()
    
    def procura_categoria(self, nome):
        if len(self.lista_categoria) > 0:
            for categoria in self.lista_categoria:
                if nome == categoria.nome:
                    print(categoria)
                    return categoria
        else:
            return None

    def incluir_categoria(self):
        dados_categoria = self.__tela_categoria_brinde.pega_dados_categoria()
        nome = dados_categoria["nome"]
        try:
            if nome == '':
                raise KeyError
            else:
                categoria = CategoriaBrinde(nome)
                self.__categoria_DAO.add(categoria)
        except KeyError:
            self.__tela_categoria_brinde.mostrar_mensagem('Campo de Nome vazio, tente novamente!')

    def excluir_categoria(self):
        if len(self.lista_categoria) == 0:
            self.__tela_categoria_brinde.mostrar_mensagem('Lista de Categorias está vazia')
            return None
        self.__tela_categoria_brinde.mostrar_mensagem('Digite o nome da Categoria que deseja excluir')
        nome_categoria = self.__tela_categoria_brinde.seleciona_categoria()
        categoria_excluir = self.procura_categoria(nome_categoria)
        if isinstance(categoria_excluir, CategoriaBrinde):
            self.__categoria_DAO.remove(categoria_excluir)
            self.__tela_categoria_brinde.mostrar_mensagem('Categoria excluida com sucesso!')
        else:
            self.__tela_categoria_brinde.mostrar_mensagem('Categoria não encontrada')

    def listar_categorias(self):
        if len(self.lista_categoria) == 0:
            self.__tela_categoria_brinde.mostrar_mensagem('Lista de Categorias está vazia')
            return None
        dados_categoria = []
        for categoria in self.lista_categoria:
            dados_categoria.append({"nome": categoria.nome})
        self.__tela_categoria_brinde.mostrar_categorias(dados_categoria)

    def alterar_categoria(self):
        if len(self.lista_categoria) == 0:
            self.__tela_categoria_brinde.mostrar_mensagem('Lista de Categorias está vazia')
            return None
        self.__tela_categoria_brinde.mostrar_mensagem('Alterar Categoria:')
        nome_categoria = self.__tela_categoria_brinde.seleciona_categoria()
        categoria_alterar = self.procura_categoria(nome_categoria)
        if isinstance(categoria_alterar, CategoriaBrinde):
            dados_categoria = self.__tela_categoria_brinde.pega_dados_categoria()
            categoria_alterar.nome = dados_categoria["nome"]
            self.__tela_categoria_brinde.mostrar_mensagem('**Categoria alterada com sucesso!**')
        else:
            self.__tela_categoria_brinde.mostrar_mensagem('Categoria não encontrada!')

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_categoria, 2: self.listar_categorias, 
                        3: self.alterar_categoria, 4: self.excluir_categoria, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_categoria_brinde.tela_opcoes()]()
