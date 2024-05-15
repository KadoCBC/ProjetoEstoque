from entidades.Brinde import Brinde
from telas.TelaBrinde import TelaBrinde


class ControladorBrinde():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_brinde = TelaBrinde()
        self.__lista_brindes = []
    
    @property
    def lista_brindes(self):
        return self.__lista_brindes
    
    #Pega os dados do Brinde, instancia e inclui na lista
    def incluir_brinde(self):
        dados_brinde = self.__tela_brinde.pega_dados_brinde()
        categoria_brinde = dados_brinde["categoria_brinde"]
        """ if categoria_brinde in self.__controlador_sistema.controlador_categoria.lista_categorias:
                brinde.categoria_brinde = categoria_brinde
        """
        brinde = Brinde(dados_brinde["nome"], dados_brinde["quantidade"])
        self.lista_brindes.append(brinde)

    #Se a lista não tiver vazia, procura o brinde pelo atributo nome e retorna
    def procura_brindes(self, nome_brinde):
        if len(self.lista_brindes) > 0:
            for brinde in self.lista_brindes:
                if nome_brinde == brinde.nome:
                    return brinde
        else:
            return #mensagem lis
    
    #Retorna na tela as informações de um Brinde
    def informa_brinde(self):
        nome_brinde = self.__tela_brinde.seleciona_brinde()
        brinde = self.procura_brindes(nome_brinde)
        self.__tela_brinde.mostrar_brinde({"nome": brinde.nome, "quantidade": self.calcula_estoque(brinde),
                                            "preco": brinde.preco_atual()})

    #Envia os dados para a tela Printar a Lista de brindes
    def listar_brindes(self):
        #Verifica se a lista ta vazia
        if len(self.lista_brindes) == 0:
            return None   #criar mensagem de lista vazia
        for brinde in self.lista_brindes:
            self.__tela_brinde.mostrar_brinde({"nome": brinde.nome, "quantidade": self.calcula_estoque(brinde),
                                               "preco": brinde.preco_atual()})

    # Altera os atributos de um Brinde
    def alterar_brinde(self):
        #Mensagem de alterar brinde
        #Procura o brinde na lista de brindes
        nome_brinde = self.__tela_brinde.seleciona_brinde()
        brinde_alterar = self.procura_brindes(nome_brinde)
        #Verifica se o retorno da função é um Brinde  e instancia
        if isinstance(brinde_alterar, Brinde):
            dados_brinde = self.__tela_brinde.pega_dados_brinde()
            brinde_alterar.nome = dados_brinde["nome"]
            brinde_alterar.quantidade = dados_brinde["quantidade"]
            categoria_brinde = dados_brinde["categoria_brinde"]
            """if categoria_brinde in self.__controlador_sistema.controlador_categoria.lista_categorias:
                brinde.categoria_brinde = categoria_brinde"""
        else:
            pass #Brinde não encontrado, procure na lista

    def excluir_brinde(self):
        #Mensagem de excluir brinde
        nome_brinde = self.__tela_brinde.seleciona_brinde()
        #Procura o brinde na lista de brindes
        brinde_excluir = self.procura_brindes(nome_brinde)
        if isinstance(brinde_excluir, Brinde):
            self.lista_brindes.remove(brinde_excluir)
        else:
            pass #Brinde não encontrado, procure na lista
    
    #Calcula o estoque de um brinde a partir da lista de movimentações
    def calcula_estoque(self, brinde):
        #Recebe a lista de movimentações
        lista_mov = self.__controlador_sistema.controlador_mov.lista_mov
        #Pega o estoque inicial e soma com as movimentações e retorna
        estoque = brinde.quantidade
        for mov in lista_mov:
            if mov.brinde == brinde:
                estoque = mov.qt_mov + estoque
        return estoque

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_brinde, 2: self.listar_brindes, 3: self.alterar_brinde, 
                        4: self.excluir_brinde, 5: self.informa_brinde, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_brinde.tela_opcoes()]()


