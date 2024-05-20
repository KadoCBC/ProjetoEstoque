class TelaPreco():

    def tela_opcoes(self):
        print('----------- TELA DE OPÇÕES -----------')
        print('[1] - Criar novo Preco')
        print('[2] - Listar Preços')
        print('[3] - Alterar Preço')
        print('[4] - Excluir Preço')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True :
            escolha_usuario = int(input('Escolha um numero: '))
            if escolha_usuario >= 0 and escolha_usuario <= 4:
                return escolha_usuario
            else:
                print('Digite um número valido')
        
    def pega_dados_preco(self):
        valor = input('Valor: ')
        data = str(input('Data: '))
        id = input("Id (Brinde): ")
        return {"valor": valor, "data": data, "id":id}
    
    def mostrar_preco(self, dados_preco):
        print('------------------------------------------')
        print (f'Valor: R${dados_preco["valor"]}')
        print("Data:", dados_preco["data"])
        print("Id:", dados_preco["id"])
        print('------------------------------------------')
    
    def seleciona_preco(self):
        id = input("Id do Preco: ")
        return id
    
    def mostrar_mensagem(self, msg):
        print(msg)


