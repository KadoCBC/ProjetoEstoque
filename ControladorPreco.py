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
        return self.__preco_DAO.get_all() 
    
    def procura_precos(self, id_preco):
        if len(self.precos) > 0:
            for preco in self.precos:
                if id_preco == preco.id:
                    return preco
        else:
            return None     
    
    def incluir_preco(self):
        id_fornecedor = self.__tela_preco.seleciona_fornecedor()
        if id_fornecedor == None:
            return
        fornecedor_selecionado = self.__controlador_sistema.controlador_fornecedor.procura_fornecedor(id_fornecedor)
        try:
            if fornecedor_selecionado == None:
                raise KeyError
            else:
                dados_preco = self.__tela_preco.pega_dados_preco()
                valor = dados_preco["valor"]
                data = dados_preco["data"]
                id = dados_preco["id"]
                try:
                    if valor == '' or data == '' or id == None:
                        raise KeyError
                    else:
                        tem_id = self.procura_precos(id)
                        if tem_id == None:
                            preco = Preco(valor, data, id, fornecedor_selecionado)
                            self.__preco_DAO.add(preco)
                            self.__tela_preco.mostrar_mensagem('Preço adicionado com Sucesso!')
                except KeyError:
                    self.__tela_preco.mostrar_mensagem('Campo de valor, data ou id invalido, tente novamente')
        
        except KeyError:
            self.__tela_preco.mostrar_mensagem('Fornecedor não existe')
        
    def excluir_preco(self):
        if len(self.precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('Excluir Preço:')
        id_preco = self.__tela_preco.seleciona_preco()
        if id_preco == None:
            return
        preco_excluir = self.procura_precos(id_preco)
        try:
            if preco_excluir == None:
                raise KeyError
            else:
                self.__preco_DAO.remove(preco_excluir.id)

        except KeyError:
            self.__tela_preco.mostrar_mensagem('Preço não existe')
    
    def alterar_preco(self):
        if len(self.precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de Preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('Alterar Preço:')
        id_preco = self.__tela_preco.seleciona_preco()
        preco_alterar = self.procura_precos(id_preco)
        if isinstance(preco_alterar, Preco):
            dados_preco = self.__tela_preco.pega_dados_preco()
            preco_alterar.id = dados_preco["id"]
            self.__tela_preco.mostrar_mensagem('**Preço alterado com sucesso!**')
        else:
            self.__tela_preco.mostrar_mensagem('Preço não encontrado!')

    def listar_precos(self):
        if len(self.precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de Preços está vazia')
            return None
        dados_preco = []
        for preco in self.precos:
            dados_preco.append({"valor": preco.valor, "data": preco.data, "id": preco.id})
        self.__tela_preco.mostrar_preco(dados_preco)

    def vincular_preco(self):
        if len (self.__controlador_sistema.controlador_brinde.lista_brindes) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de brindes está vazia')
            return None
        self.listar_precos()
        id = self.__tela_preco.seleciona_preco()
        preco = self.procura_precos(id)
        print(preco)
        nome_brinde = self.__tela_preco.seleciona_brinde()
        brinde = self.__controlador_sistema.controlador_brinde.procura_brindes(nome_brinde)
        if brinde == None:
            return
        brinde.add_preco(preco)
        self.__preco_DAO.remove(preco.id)
        self.__tela_preco.mostrar_mensagem('**Preco vinculado com sucesso**')
        
    def retornar(self):
        self.__controlador_sistema.abre_tela()
    
    def abre_tela(self):
        lista_opcoes = {1: self.incluir_preco, 2: self.listar_precos, 
                        3: self.alterar_preco, 4: self.excluir_preco, 5: self.vincular_preco,  0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_preco.tela_opcoes()]()
