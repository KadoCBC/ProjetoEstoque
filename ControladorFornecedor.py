from telas.TelaFornecedor import TelaFornecedor
from entidades.Fornecedor import Fornecedor
from entidades.Endereco import Endereco

class ControladorFornecedor:

    def __init__(self, controlador_sistema):
        self.__fornecedores = []
        self.__tela_fornecedor = TelaFornecedor()
        self.__controlador_sistema = controlador_sistema
        self.__enderecos = {}
    
    @property
    def fornecedores(self):
        return self.__fornecedores
    
    def procura_fornecedor(self, id):
        if len(self.fornecedores) > 0:
            for fornecedor in self.fornecedores:
                if id == fornecedor.id:
                    return fornecedor
        else:
            return None

    def incluir_fornecedor(self):
        dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecdor()
        cria_id = len(self.fornecedores)
        while self.procura_fornecedor(cria_id) is not None:
            cria_id = cria_id + 1
        fornecedor = Fornecedor(dados_fornecedor["nome"], cria_id)
        self.__fornecedores.append(fornecedor)
        self.__tela_fornecedor.mostrar_mensagem('**Fornecedor criado com sucesso!**')

    
    def mostrar_lista_fornecedores(self):
        if len(self.fornecedores) == 0:
            self.__tela_fornecedor.mostrar_mensagem('Lista de Fornecedores está vazia')
            return None  
        for id_fornecedor, endereco in self.__enderecos.items():
            mensagem = (
                f"Fornecedor ID: {id_fornecedor}\n"
                f"Rua: {endereco.rua}\n"
                f"Complemento: {endereco.complemento}\n"
                f"Bairro: {endereco.bairro}\n"
                f"Cidade: {endereco.cidade}\n"
                f"CEP: {endereco.cep}\n"
                "------------------------"
            )
            self.__tela_fornecedor.mostrar_mensagem(mensagem)

    def alterar_fornecedor(self):
        self.__tela_fornecedor.mostrar_mensagem('Alterar Fornecedor:')
        id_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor_alterar = self.procura_fornecedor(id_fornecedor)
        if isinstance(fornecedor_alterar, Fornecedor):
            dados_fornecedor = self.__tela_fornecedor.pega_dados_fornecdor()
            fornecedor_alterar.nome = dados_fornecedor["nome"]
            self.__tela_fornecedor.mostrar_mensagem('**Fornecedor alterado com sucesso!**')

        else:
            self.__tela_fornecedor.mostrar_mensagem('Fornecedor não encontrado!')
            
    def excluir_fornecedor(self):
        self.__tela_fornecedor.mostrar_mensagem('Excluir Fornecedor: ')
        id_fornecedor = self.__tela_fornecedor.seleciona_fornecedor()
        fornecedor_excluir = self.procura_fornecedor(id_fornecedor)
        if isinstance(fornecedor_excluir, Fornecedor):
            self.fornecedores.remove(fornecedor_excluir)
            self.__tela_fornecedor.mostrar_mensagem('**Fornecedor excluido com sucesso!**')
        else:
            self.__tela_fornecedor.mostrar_mensagem('Fornecedor não encontrado!')

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
        lista_opcoes = {1: self.incluir_fornecedor, 2: self.mostrar_lista_fornecedores, 
                        3: self.alterar_fornecedor, 4: self.excluir_fornecedor, 5: self.adicionar_endereco, 
                        0: self.retornar}

        continua = True
        while continua:
            lista_opcoes[self.__tela_fornecedor.tela_opcoes()]()
