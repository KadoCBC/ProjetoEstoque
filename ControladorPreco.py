from entidades.Preco import Preco
from telas.TelaPreco import TelaPreco
from DAOs.Preco_dao import PrecoDAO

class ControladorPreco:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_precos = []
        self.__tela_preco = TelaPreco()
        self.__preco_DAO = PrecoDAO()
    
    @property
    def precos(self):
        self.__fornecedor_DAO.get_all() 
    
    def procura_precos(self, id_preco):
        if len(self.precos) > 0:
            for preco in self.precos:
                if id_preco == preco.id:
                    return preco
        else:
            return None
    
    def incluir_preco(self):
        id_fornecedor = self.__tela_preco.escolhe_fornecedor()
        fornecedor = self.__controlador_sistema.controlador_fornecedor.procura_fornecedor(id_fornecedor)
        if fornecedor is None:
            self.__tela_preco.mostrar_mensagem('Fornecedor não encontrado')
            return None
        dados_preco = self.__tela_preco.pega_dados_preco()
        valor = dados_preco["valor"]
        data = dados_preco["data"]
        id = dados_preco["id"]
        try:
            if valor == '' or data == '' or id == '':
                raise KeyError
            else:
                preco = Preco(valor, data, id)
                self.__preco_DAO.add(preco)
                self.__lista_precos.append(preco)
        except KeyError:
            self.__tela_preco.mostrar_mensagem('Campo de valor, data ou id vazio, tente novamente')

    def excluir_preco(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('Excluir Preço:')
        id_preco = self.__tela_preco.seleciona_preco()
        preco_excluir = self.procura_precos(id_preco)
        if isinstance(preco_excluir, Preco):
            self.__preco_DAO.remove(preco_excluir)
            self.__lista_precos.remove(preco_excluir)
            self.__tela_preco.mostrar_mensagem('**Preço excluido com sucesso!**')
        else:
            self.__tela_preco.mostrar_mensagem('Preço não encontrado!')
            
    def alterar_preco(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('Alterar Preço:')
        id_preco = self.__tela_preco.seleciona_preco()
        preco_alterar = self.procura_precos(id_preco)
        if isinstance(preco_alterar, Preco):
            dados_preco = self.__tela_preco.pega_dados_preco()
            preco_alterar.valor = dados_preco["valor"]
            preco_alterar.data = dados_preco["data"]
            self.__preco_DAO.update(preco_alterar)
            self.__tela_preco.mostrar_mensagem('**Preço alterado com sucesso!**')
        else:
            self.__tela_preco.mostrar_mensagem('Preço não encontrado!')

    def listar_precos(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        dados_preco = []
        for preco in self.__lista_precos:
            dados_preco.append({"valor": preco.valor, "data": preco.data, "id": preco.id})
        self.__tela_preco.mostrar_preco(dados_preco)

    def vincular_preco(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        if len (self.__controlador_sistema.controlador_brinde.lista_brindes) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de brindes está vazia')
            return None
        self.listar_precos()
        self.__tela_preco.mostrar_mensagem('Escolha o Id que deseja vincular a um brinde')
        id = self.__tela_preco.seleciona_preco()
        preco = self.procura_precos(id)
        self.__tela_preco.mostrar_mensagem('Escolha o brinde que deseja vincular')
        nome_brinde = self.__tela_preco.vincula_preco()
        brinde = self.__controlador_sistema.controlador_brinde.procura_brindes(nome_brinde)
        brinde.add_preco(preco)
        self.__lista_precos.remove(preco)
        self.__tela_preco.mostrar_mensagem('**Preco vinculado com sucesso**')
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_preco, 2: self.listar_precos, 
                        3: self.alterar_preco, 4: self.excluir_preco, 5: self.vincular_preco,  0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_preco.tela_opcoes()]()
