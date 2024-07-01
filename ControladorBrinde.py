from entidades.Brinde import Brinde
from telas.TelaBrinde import TelaBrinde
from DAOs.Brinde_dao import BrindeDAO
from Exceptions.brinde_repetido_exception import BrindeRepetidoException


class ControladorBrinde():

    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__brinde_DAO = BrindeDAO()
        self.__tela_brinde = TelaBrinde()
        self.__id_unico = len(self.lista_brindes)
    
    @property
    def lista_brindes(self):
        return self.__brinde_DAO.get_all()
    
    @property
    def id_unico(self):
        return self.__id_unico
    
    @id_unico.setter
    def id_unico(self, valor):
        self.__id_unico = valor
    
    #Se a lista não tiver vazia, procura o brinde pelo atributo nome e retorna
    def procura_brindes(self, nome_brinde):
        if len(self.lista_brindes) > 0:
            for brinde in self.lista_brindes:
                if nome_brinde == brinde.nome:
                    return brinde
            return None
    #PROCURA POR ID
    def procura_brindes_id(self, id):
        if len(self.lista_brindes) > 0:
            for brinde in self.lista_brindes:
                if id == brinde.id:
                    return brinde
            return None
    
    #Pega os dados do Brinde, instancia e inclui na lista
    def incluir_brinde(self):
        dados_brinde = self.__tela_brinde.pega_dados_brinde()
        nome = dados_brinde["nome"]
        quantidade = dados_brinde["quantidade"]
        brinde = self.procura_brindes(nome)
        #Tratamento de dados NOME BRINDE
        try:
            if brinde == None and quantidade != None:
                #Cria um id unico para cada brinde
                id = self.__id_unico + 1
                brinde = Brinde(nome, quantidade, id)
                self.__id_unico = id
            elif quantidade == None:
                return
            else:
                raise BrindeRepetidoException(nome)
        except BrindeRepetidoException as e:
            self.__tela_brinde.mostrar_mensagem(e)
            return
        categoria_nome = dados_brinde["categoria_brinde"]
        categoria_brinde = self.__controlador_sistema.controlador_categoria_brinde.procura_categoria(categoria_nome)
        #tratamento de dados categoria de brinde
        try:
            if categoria_brinde == None:
                raise KeyError
            else:
                brinde.categoria_brinde = categoria_brinde.nome
        except KeyError:
            self.__tela_brinde.mostrar_mensagem('Categoria não existe, valor :Geral: foi adicionado')
        self.__brinde_DAO.add(brinde)
        self.__tela_brinde.mostrar_mensagem('Brinde Criado com Sucesso!')

    #Retorna na tela as informações de um Brinde
    def informa_brinde(self):
        self.__tela_brinde.mostrar_mensagem('INFORMAÇÕES DO BRINDE')
        nome_brinde = self.__tela_brinde.seleciona_brinde()
        brinde = self.procura_brindes(nome_brinde)
        dados_brinde = []
        #tratamento de dados
        try:
            if brinde == None:
                raise KeyError
            else:
                dados_brinde.append({"nome": brinde.nome, "quantidade": self.calcula_estoque(brinde),
                                        "preco": brinde.preco_atual(), "id": brinde.id, "categoria": brinde.categoria_brinde})
            self.__tela_brinde.mostrar_brinde(dados_brinde)
        except KeyError:
            self.__tela_brinde.mostrar_mensagem('Brinde não encontrado!')
            return
 
    #Envia os dados para a tela Printar a Lista de brindes
    def listar_brindes(self):
        #Verifica se a lista ta vazia
        if len(self.lista_brindes) == 0:
            self.__tela_brinde.mostrar_mensagem('Lista está Vazia')
            return None
        dados_brinde = []
        for brinde in self.lista_brindes:
            dados_brinde.append({"nome": brinde.nome, "quantidade": self.calcula_estoque(brinde),
                                               "preco": brinde.preco_atual(), "id": brinde.id, "categoria": brinde.categoria_brinde})
        self.__tela_brinde.mostrar_brinde(dados_brinde)

    # Altera os atributos de um Brinde
    def alterar_brinde(self):
        #Procura o brinde na lista de brindes
        nome_brinde = self.__tela_brinde.seleciona_brinde()

        brinde_alterar = self.procura_brindes(nome_brinde)
        #Tratamento de Dados
        try:
            if brinde_alterar == None:
                raise KeyError
            else:
                dados_brinde = self.__tela_brinde.pega_dados_brinde()
                if dados_brinde["quantidade"] == None:
                    return
                brinde_alterar.nome = dados_brinde["nome"]
                brinde_alterar.quantidade = dados_brinde["quantidade"]
                categoria_brinde = dados_brinde["categoria_brinde"]
                if categoria_brinde in self.__controlador_sistema.controlador_categoria_brinde.lista_categoria:
                    brinde_alterar.categoria_brinde = categoria_brinde
                else:
                    self.__tela_brinde.mostrar_mensagem('Categoria não encontrada - Adicionado valor padrão')
                self.__brinde_DAO.update(brinde_alterar)
                self.__tela_brinde.mostrar_mensagem('**Brinde Alterado com sucesso!**')
        except KeyError:
            self.__tela_brinde.mostrar_mensagem('Brinde não encontrado!')
            return

    def excluir_brinde(self):
        self.__tela_brinde.mostrar_mensagem('Digite o Brinde que deseja excluir')
        nome_brinde = self.__tela_brinde.seleciona_brinde()
        #Procura o brinde na lista de brindes
        brinde_excluir = self.procura_brindes(nome_brinde)
        try:
            if brinde_excluir == None:
                raise KeyError
            else:
                self.__brinde_DAO.remove(brinde_excluir.id)
                self.__tela_brinde.mostrar_mensagem('Brinde excluido com sucesso!')
        except KeyError:
            self.__tela_brinde.mostrar_mensagem('Brinde não encontrado!')
            return

    #Calcula o estoque de um brinde a partir da lista de movimentações
    def calcula_estoque(self, brinde):
        #Recebe a lista de movimentações
        lista_mov = self.__controlador_sistema.controlador_mov.lista_mov
        #Pega o estoque inicial e soma com as movimentações e retorna
        estoque = brinde.quantidade
        for mov in lista_mov:
            if mov.brinde["id"] == brinde.id:
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
