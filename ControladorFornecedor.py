from telas.TelaFornecedor import TelaFornecedor
from entidades.Fornecedor import Fornecedor
from entidades.Endereco import Endereco
from DAOs.Fornecedor_dao import FornecedorDAO

class ControladorFornecedor:

    def __init__(self, controlador_sistema):
        self.__fornecedor_DAO = FornecedorDAO()
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema
        self.__enderecos = {}
    
    @property
    def fornecedores(self):
        return self.__fornecedor_DAO.get_all()

    def procura_fornecedor(self, id):
        print(id)
        if len(self.fornecedores) > 0:
            for fornecedor in self.fornecedores:
                if id == fornecedor.id:
                    print(fornecedor)
                    return fornecedor
        else:
            return None

    def incluir_fornecedor(self):
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecedor()
        cria_id = len(self.fornecedores)
        while self.procura_fornecedor(cria_id) is not None:
            cria_id = cria_id + 1
        fornecedor = Fornecedor(dados_fornecedor["nome"], cria_id)
        self.__fornecedor_DAO.add(fornecedor)

    def lista_fornecedores(self):
        if len(self.fornecedores) == 0:
            self.__tela_fornecedor.mostrar_mensagem('Lista de Fornecedores está vazia')
            return None
        dados_fornecedor = []
        for fornecedor in self.fornecedores:
            dados_fornecedor.append({"id": fornecedor.id, "nome": fornecedor.nome})
        self.__tela_fornecedor.mostrar_fornecedor(dados_fornecedor)

    def alterar_fornecedor(self):
        id_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor_alterar = self.procura_fornecedor(id_fornecedor)
        if isinstance(fornecedor_alterar, Fornecedor):
            dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecdor()
            fornecedor_alterar.nome = dados_fornecedor["nome"]
            self.__fornecedor_DAO.update(fornecedor_alterar)
        else:
            self.__tela_fornecedor.mostrar_mensagem('Fornecedor não encontrado!')

    def excluir_fornecedor(self):
        self.__tela_fornecedor.mostrar_mensagem('Excluir Fornecedor: ')
        id_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        #Fazer codigo para verificar se é inteiro
        fornecedor_excluir = self.procura_fornecedor(id_fornecedor)
        if isinstance(fornecedor_excluir, Fornecedor):
            self.__fornecedor_DAO.remove(fornecedor_excluir)
        else:
            self.__tela_fornecedor.mostrar_mensagem('Fornecedor não encontrado!')

    def mostrar_lista_enderecos(self):
        if len(self.__enderecos) == 0:
            self.__tela_fornecedor.mostrar_mensagem('Lista de endereços está vazia')
            return None
        dados_endereco = []
        for id_fornecedor in self.__enderecos:
            endereco = self.__enderecos[id_fornecedor]
            dados_endereco.append({"id_fornecedor": id_fornecedor, "rua": endereco.rua, "complemento": endereco.complemento, "bairro": endereco.bairro, "cidade": endereco.cidade, "cep": endereco.cep})
        self.__tela_fornecedor.mostrar_endereco(dados_endereco)
    
    def adicionar_endereco(self):
        self.__tela_fornecedor.mostrar_mensagem('Adicionar Endereço a um fornecedor:')
        id_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor_selecionado = self.procura_fornecedor(id_fornecedor)
        if isinstance(fornecedor_selecionado, Fornecedor):
            dados_endereco = self.__tela_fornecedor.pega_dados_endereco()
            endereco = Endereco(dados_endereco["rua"], dados_endereco["complemento"], dados_endereco["bairro"], dados_endereco["cidade"], dados_endereco['cep'])
            self.__enderecos[id_fornecedor] = endereco
            self.__tela_fornecedor.mostrar_mensagem("Endereço adicionado com sucesso!")
        else:
            self.__tela_fornecedor.mostrar_mensagem("Fornecedor não encontrado")

            
    def retornar(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_fornecedor, 2: self.lista_fornecedores, 
                        3: self.alterar_fornecedor, 4: self.excluir_fornecedor, 
                        5: self.adicionar_endereco, 6: self.mostrar_lista_enderecos,
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fornecedor.tela_opcoes()]()
