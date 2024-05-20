class TelaFornecedor():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Criar Novo Fornecedor')
        print('[2] - Listar Fornecedores')
        print('[3] - Alterar Fornecedor')
        print('[4] - Exluir Fornecedor')
        print('[5] - Adicionar endereço')
        print('[6] - Listar Endereços')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True:
            escolha_usuario = input('Escolha um número: ')
            try:
                escolha_usuario = int(escolha_usuario)
                if 0 <= escolha_usuario <= 6:
                    return escolha_usuario
                else:
                    print('Digite um número válido entre 0 e 6.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')
        
    def pega_dados_fornecdor(self):
        nome = input('Nome: ')
        return {"nome": nome}
    
    def pega_dados_endereco(self):
        rua = input("Rua: ")
        complemento = input("Complemento: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        cep = input("CEP: ")
        return {"rua": rua, "complemento": complemento, "bairro": bairro, "cidade": cidade, "cep": cep}
    
    def mostrar_fornecedor(self, dados_fornecedor):
        print("ID:" , dados_fornecedor["id"])
        print("Nome:" , dados_fornecedor["nome"])    
        print('------------------------------------------')

    def seleciona_fornecedor(self):
        id = int(input("ID do fornecedor que deseja selecionar: "))
        return id
    
    def mostrar_mensagem(self, msg):
        print(msg)
