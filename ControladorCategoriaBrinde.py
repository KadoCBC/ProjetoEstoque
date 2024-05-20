from entidades.CategoriaBrinde import CategoriaBrinde
from telas.TelaCategoriaBrinde import TelaCategoriaBrinde


class ControladorCategoriaBrinde:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_categorias = []
        self.__tela__categoria_brinde = TelaCategoriaBrinde()

    @property
    def lista_categorias(self):
        return self.__lista_categorias
    
    def mostra_lista_categorias(self):
        if len(self.__lista_categorias) == 0:
            self.__tela__categoria_brinde.mostrar_mensagem('Lista de categorias está vazia')
            return None
        self.__tela__categoria_brinde.mostrar_mensagem('LISTA DE CATEGORIAS')        
        for categoria in self.__lista_categorias:
            self.__tela__categoria_brinde.mostrar_mensagem(categoria.nome)
        
    def procura_categoria(self, nome):
        if len(self.__lista_categorias) > 0:
            for categoria in self.__lista_categorias:
                if nome == categoria.nome:
                    return categoria
        else:
            return None
        
    def incluir_categoria(self):
        dados_categoria = self.__tela__categoria_brinde.pega_dados_categoria()
        categoria = CategoriaBrinde(dados_categoria["nome"])
        self.__lista_categorias.append(categoria)
        self.__tela__categoria_brinde.mostrar_mensagem('**Categoria Criado com Sucesso!**')


    def excluir_categoria(self):
        if len(self.__lista_categorias) == 0:
            self.__tela__categoria_brinde.mostrar_mensagem('Lista de categorias está vazia')
            return None
        self.__tela__categoria_brinde.mostrar_mensagem('Digite o nome da Categoria que deseja excluir')
        nome_categoria = self.__tela__categoria_brinde.seleciona_categoria()
        #Procura a categoria na lista de categorias
        categoria_excluir = self.procura_categoria(nome_categoria)
        if isinstance(categoria_excluir, CategoriaBrinde):
            self.__lista_categorias.remove(categoria_excluir)
            self.__tela__categoria_brinde.mostrar_mensagem('Categoria excluida com sucesso!')
        else:
            self.__tela__categoria_brinde.mostrar_mensagem('Categoria não encontrada')

    def alterar_categoria(self):
        if len(self.__lista_categorias) == 0:
            self.__tela__categoria_brinde.mostrar_mensagem('Lista de categorias está vazia')
            return None
        self.__tela__categoria_brinde.mostrar_mensagem('Alterar Categoria:')
        nome = self.__tela__categoria_brinde.seleciona_categoria()
        categoria_alterar = self.procura_categoria(nome)
        if isinstance(categoria_alterar, CategoriaBrinde):
            dados_categoria = self.__tela__categoria_brinde.pega_dados_categoria()
            categoria_alterar.nome = dados_categoria["nome"]
            self.__tela__categoria_brinde.mostrar_mensagem('**Categoria alterada com sucesso!**')

    '''
    def mostrar_categorias(self):
        if len(self.__lista_categorias) == 0:
            self.__tela__categoria_brinde.mostrar_mensagem('Lista de categorias está vazia')
            return None
        brindes = self.__controlador_sistema.self.controlador_brinde.lista_brindes
        self.__tela__categoria_brinde.mostrar_mensagem('CATEGORIAS E SEUS BRINDES:')
        for categoria in self.__lista_categorias:
            self.__tela__categoria_brinde.mostrar_mensagem(f'Categoria: {categoria.nome}')
            tem_brindes = False
            for brinde in brindes:
                if brinde.categoria_brinde == categoria:
                    self.__tela__categoria_brinde.mostrar_mensagem(f'  - Brinde: {brinde.nome}')
                    tem_brindes = True
            if not tem_brindes:
                self.__tela__categoria_brinde.mostrar_mensagem('Nenhum brinde cadastrado nessa categoria')'''

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_categoria, 2: self.mostra_lista_categorias, 
                        3: self.alterar_categoria, 4: self.excluir_categoria, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela__categoria_brinde.tela_opcoes()]()