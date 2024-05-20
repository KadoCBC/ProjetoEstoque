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
            self.__tela__categoria_brinde.mostrar_mensagem('Lista está Vazia')
            return None
        self.__tela__categoria_brinde.mostrar_mensagem('LISTA DE CATEGORIAS')        
        for categoria in self.__lista_categorias:
            return categoria
        
        for categoria in self.__lista_categorias:
            return categoria
        
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
        pass

    def mostrar_categorias(self):
        pass

    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_categoria, 2: self.mostra_lista_categorias, 
                        3: self.excluir_categoria, 4: self.alterar_categoria, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_preco.tela_opcoes()]()