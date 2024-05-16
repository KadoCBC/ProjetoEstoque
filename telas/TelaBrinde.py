class TelaBrinde():

    def tela_opcoes(self):
        print('----------- TELA DE OPÇÕES -----------')
        print('[1] - Criar novo Brinde')
        print('[2] - Listar Brindes')
        print('[3] - Alterar Brinde')
        print('[4] - Excluir Brinde')
        print('[5] - Informações de Brinde')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True :
            escolha_usuario = int(input('Escolha um numero'))
            if escolha_usuario >= 0 and escolha_usuario <= 5:
                return escolha_usuario
            else:
                print('Digite um número valido')
        
    def pega_dados_brinde(self):
        nome = input('Nome: ')
        quantidade = int(input('Quantidade: '))
        categoria_brinde = input('Categoria *caso não tenha digite 0:')
        return {"nome": nome, "quantidade": quantidade, "categoria_brinde": categoria_brinde}
    
    def mostrar_brinde(self, dados_brinde):
        print('------------------------------------------')
        print(dados_brinde["nome"])
        print("Quantidade:" , dados_brinde["quantidade"])
        print("Preço_atual: R$ ", dados_brinde["preco"])
        print('------------------------------------------')
    
    def seleciona_brinde(self):
        nome = input("Nome do brinde: ")
        return nome
    
    def mostrar_mensagem(self, msg):
        print(msg)


