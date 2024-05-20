class TelaPreco():

    def tela_opcoes(self):
        print('----------- TELA DE OPÇÕES -----------')
        print('[1] - Criar novo Preco')
        print('[2] - Listar Preços')
        print('[3] - Alterar Preço')
        print('[4] - Excluir Preço')
        print('[5] - Vincular Preço')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True:
            escolha_usuario = input('Escolha um número: ')
            try:
                escolha_usuario = int(escolha_usuario)
                if 0 <= escolha_usuario <= 5:
                    return escolha_usuario
                else:
                    print('Digite um número válido entre 0 e 5.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')
        
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

    def escolhe_fornecedor(self):
        esocolha_fornecedor = int(input("Escolha o id do fornecedor: "))
        return esocolha_fornecedor
    
    
    def seleciona_preco(self):
        id = input("Id do Preco: ")
        return id
    
    def vincula_preco(self):
        brinde = input("nome do Brinde: ")
        return brinde
    
    def mostrar_mensagem(self, msg):
        print(msg)
