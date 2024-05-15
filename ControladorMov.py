from telas.TelaMov import TelaMov
from entidades.Movimentacao import Movimentacao



class ControladorMov():

    def __init__(self, controlador_sistema):
        self.__tela_mov = TelaMov()
        self.__controlador_sistema = controlador_sistema
        self.__lista_mov = []
    
    @property
    def lista_mov(self):
        return self.__lista_mov
    
    def procura_movimentacao(self, codigo):
        #Busca a movimentacão pelo codigo, caso não tenha returna None
        if len(self.lista_mov) > 0:
            for movimentacao in self.lista_mov:
                if codigo == movimentacao.codigo:
                    return movimentacao
        else:
            return #mensagem não tem na lista
    
    def incluir_mov(self):
        #Confere se o brinde escolhido para movimentar está na lista de brindes 
        nome_brinde = self.__tela_mov.escolhe_brinde()
        brinde = self.__controlador_sistema.controlador_brinde.procura_brindes(nome_brinde)
        if brinde is None:
            return print('Brinde não existe, tente novamente') ##mudar para mensagem depois
        #Escolhe um usuario dentro da lista de usuarios
        id_usuario = self.__tela_mov.escolhe_usuario()
        usuario = self.__controlador_sistema.controlador_usuario.procura_usuario(id_usuario)
        if usuario is None:
            return print('usuario não existe, tente novamente') ##mudar para mensagem depois
        #Pega os dados da movimentação
        dados_mov = self.__tela_mov.dados_movimento()
        #Cria um codigo diferente para cada movimentacao
        cria_codigo = len(self.lista_mov)
        while self.procura_movimentacao(cria_codigo) is not None:
            cria_codigo = cria_codigo + 1
        #Cria e inclui a movimentação na lista
        movimentacao = Movimentacao(dados_mov["quantidade"], dados_mov["instituidor"], dados_mov["motivo"], 
                                     cria_codigo, brinde.nome, usuario)
        self.lista_mov.append(movimentacao)
    
    #Mostra a lista de movimentaçoes - Mensagem
    def listar_mov(self):
        # Verifica se a lista está vazia
        if len(self.lista_mov) == 0:
            return None   #criar mensagem de lista vazia
        # Percorre a lista e mostra os atributos das mov ela com a funcão da tela
        for mov in self.lista_mov:
            self.__tela_mov.mostrar_movimento({"brinde": mov.brinde, "tipo": mov.tipo_mov, "qt_mov": mov.qt_mov,
                                                "instituidor": mov.instituidor, "motivo": mov.motivo, 
                                                "codigo": mov.codigo, "data": mov.data, "usuario": mov.responsavel})
    
    def exclui_mov(self):
        #Mensagem de excluir usuario
        codigo_mov = self.__tela_mov.seleciona_movimento()
        codigo_valido = isinstance(codigo_mov, int)
        #Validação se é Inteiro 
        while codigo_valido == False:
            print('Codigo deve ser um inteiro, tente novamente') ##Mudar depois essa funcão para a Tela
            codigo_mov = self.__tela_mov.seleciona_movimento()
            codigo_invalido = isinstance(codigo_mov, int)
        #Verifica se existe a movimentação e, caso sim,  exclui da lista
        mov_excluir = self.procura_movimentacao(codigo_mov)
        if isinstance(mov_excluir, Movimentacao):
            self.lista_mov.remove(mov_excluir)
        else:
            pass # Mensagem - Usuario não encontrado, procure na lista

    #Rankea os brindes com maior saida
    def rank_brindes(self):
        lista_brindes = self.__controlador_sistema.controlador_brinde.lista_brindes
        dicionario_brindes = {}
        # Para Cada brinde na lista de brindes procura as movimentacoes de saida associadas a ele, soma e adiciona 
        # no dicionario 
        for brinde in lista_brindes:
            quantidade = 0
            for mov in self.lista_mov:
                if mov.brinde == brinde.nome and mov.tipo_mov == 'Saida':
                    quantidade = mov.qt_mov + quantidade
            dicionario_brindes[brinde.nome] = quantidade
        #ordena o dicionario do maior para o menor
        for i in sorted(dicionario_brindes, key = dicionario_brindes.get, reverse=True):
            print(i, dicionario_brindes[i])

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_mov, 2: self.listar_mov, 
                        3: self.exclui_mov, 4: self.rank_brindes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_mov.tela_opcoes()]()
    

