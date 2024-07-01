from telas.TelaMov import TelaMov
from entidades.Movimentacao import Movimentacao
from DAOs.Mov_dao import MovimentacaoDAO


class ControladorMov():

    def __init__(self, controlador_sistema):
        self.__tela_mov = TelaMov()
        self.__controlador_sistema = controlador_sistema
        self.__movimentacao_DAO = MovimentacaoDAO()
    
    @property
    def lista_mov(self):
        return self.__movimentacao_DAO.get_all()
    
    def procura_movimentacao(self, codigo):
        #Busca a movimentacão pelo codigo, caso não tenha returna None
        if len(self.lista_mov) > 0:
            for movimentacao in self.lista_mov:
                if codigo == movimentacao.codigo:
                    return movimentacao
        else:
            return None
    
    def incluir_mov(self):
        #Confere se o brinde escolhido para movimentar está na lista de brindes 
        nome_brinde = self.__tela_mov.escolhe_brinde()
        brinde = self.__controlador_sistema.controlador_brinde.procura_brindes(nome_brinde["brinde"])
        if brinde is None:
            self.__tela_mov.mostrar_mensagem('Brinde não encontrado')
            return
        #Escolhe um usuario dentro da lista de usuarios
        id_usuario = nome_brinde["usuario"]
        usuario = self.__controlador_sistema.controlador_usuario.procura_usuario(id_usuario)
        if usuario is None:
            self.__tela_mov.mostrar_mensagem('Usuario não encontrado')
            return
        #Pega os dados da movimentação
        dados_mov = self.__tela_mov.dados_movimento()
        quantidade = dados_mov["qt_mov"]
        if quantidade == None:
            return 
        #Verifica se tem o brinde em estoque
        qt_em_estoque = self.__controlador_sistema.controlador_brinde.calcula_estoque(brinde)
        operacao_vef = qt_em_estoque + quantidade
        if operacao_vef < 0:
            self.__tela_mov.mostrar_mensagem(f'Quantidade insuficiente em estoque!, quantidade em estoque: {qt_em_estoque}')
            return 
        #Cria um codigo diferente para cada movimentacao
        cria_codigo = len(self.lista_mov)
        while self.procura_movimentacao(cria_codigo) is not None:
            cria_codigo = cria_codigo + 1
        #Cria e inclui a movimentação na lista
        brinde_mov = {"nome": brinde.nome, "id": brinde.id}
        movimentacao = Movimentacao(quantidade, dados_mov["instituidor"], dados_mov["motivo"], 
                                     cria_codigo, brinde_mov, usuario)
        self.__movimentacao_DAO.add(movimentacao)
        self.__tela_mov.mostrar_mensagem('**Movimento criado com sucesso!**')
    
    #Mostra a lista de movimentaçoes - Mensagem
    def listar_mov(self):
        # Verifica se a lista está vazia
        if len(self.lista_mov) == 0:
            self.__tela_mov.mostrar_mensagem('Lista de movimentações está vazia!')
            return None   
        self.__tela_mov.mostrar_mensagem('LISTA DE MOVIMENTAÇÕES')
        # Percorre a lista e mostra os atributos das mov ela com a funcão da tela
        dados_movimentacoes = []
        for mov in self.lista_mov:
            nome_brinde = mov.brinde['nome']
            dados_movimentacoes.append({"brinde": nome_brinde, "tipo": mov.tipo_mov, "qt_mov": mov.qt_mov,
                                                "instituidor": mov.instituidor, "motivo": mov.motivo, 
                                                "codigo": mov.codigo, "data": mov.data, "usuario": mov.responsavel.nome})
        self.__tela_mov.mostrar_movimento(dados_movimentacoes)
    
    def exclui_mov(self):
        codigo_mov = self.__tela_mov.seleciona_movimento()
        #Validação se é Inteiro 
        while codigo_mov == None:
            codigo_mov = self.__tela_mov.seleciona_movimento()
        #Verifica se existe a movimentação e, caso sim,  exclui da lista
        mov_excluir = self.procura_movimentacao(codigo_mov)
        try:
            if mov_excluir == None:
                raise KeyError
            else:
                self.__movimentacao_DAO.remove(mov_excluir.codigo)
                self.__tela_mov.mostrar_mensagem('Movimento excluido com sucesso!')
        except KeyError:
            self.__tela_mov.mostrar_mensagem('Movimentação não encontrado')
            return

    #Rankea os brindes com maior saida
    def rank_brindes(self):
        brindes = self.__controlador_sistema.controlador_brinde.lista_brindes
        lista_brindes = []
        lista_quantidades = []
        # Para Cada brinde na lista de brindes procura as movimentacoes de saida associadas a ele, soma e adiciona 
        # Adiciona o nome do brinde na lista de brindes e a quantidade na lista de quantidades com indice sendo a referencia
        for brinde in brindes:
            lista_brindes.append(brinde.nome)
            quantidade = 0
            for mov in self.lista_mov:
                if mov.brinde["id"] == brinde.id and mov.tipo_mov == 'Saida':
                    quantidade = mov.qt_mov + quantidade
            lista_quantidades.append(quantidade)
        matriz_lista = [lista_brindes, lista_quantidades]
        self.__tela_mov.mostrar_mensagem('RANK DE BRINDES')
        self.__tela_mov.mostrar_rank(matriz_lista)
        #ordena o dicionario do maior para o menor

    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_mov, 2: self.listar_mov, 
                        3: self.exclui_mov, 4: self.rank_brindes, 0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_mov.tela_opcoes()]()
