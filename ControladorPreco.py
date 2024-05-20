from entidades.Preco import Preco
from telas.TelaPreco import TelaPreco

class ControladorPreco:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__lista_precos = []
        self.__tela_preco = TelaPreco()
    
    @property
    def lista_precos(self):
        return self.__lista_precos
    
    def procura_precos(self, id_preco):
        if len(self.lista_precos) > 0:
            for preco in self.lista_precos:
                if id_preco == preco.id:
                    return preco
        else:
            return None
    
    def incluir_preco(self):
        dados_preco = self.__tela_preco.pega_dados_preco()
        preco = Preco(dados_preco["valor"], dados_preco["data"], dados_preco["id"])
        self.__lista_precos.append(preco)
        self.__tela_preco.mostrar_mensagem('**Preço criado com Sucesso!**')

    def excluir_preco(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('Digite o id do Preço que deseja excluir')
        id_preco = self.__tela_preco.seleciona_preco()
        #Procura o preco na lista de preços
        preco_excluir = self.procura_precos(id_preco)
        if isinstance(preco_excluir, Preco):
            self.__lista_precos.remove(preco_excluir)
            self.__tela_preco.mostrar_mensagem('Preço excluido com sucesso!')
        else:
            self.__tela_preco.mostrar_mensagem('Preço não encontrado')
            
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
            preco_alterar.id = dados_preco["id"]
            self.__tela_preco.mostrar_mensagem('**Preço alterado com sucesso!**')

        else:
            self.__tela_preco.mostrar_mensagem('Preço não encontrado!')

    def listar_precos(self):
        if len(self.__lista_precos) == 0:
            self.__tela_preco.mostrar_mensagem('Lista de preços está vazia')
            return None
        self.__tela_preco.mostrar_mensagem('LISTA DE PREÇOS')        
        for preco in self.__lista_precos:
            self.__tela_preco.mostrar_preco({"valor": preco.valor, "data": preco.data,"id": preco.id})
    
    def vincular_preco(self):
        if len(self.lista_precos) > 0:
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
