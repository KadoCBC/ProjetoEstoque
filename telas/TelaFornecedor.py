class TelaFornecedor():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Criar Novo Fornecedor')
        print('[2] - listar Fornecedores')
        print('[3] - Alterar Fornecedor')
        print('[4] - exluir Fornecedor')
        print('[0] - Retornar')
        while True :
            escolha_usuario = int(input('Escolha um numero'))
            if escolha_usuario >= 0 and escolha_usuario <= 4:
                return escolha_usuario
            else:
                print('Digite um número valido')
        
    def pega_dados_fornecdor(self):
        nome = input('Nome: ')
        return {"nome": nome}
    
    def mostrar_fornecedor(self, dados_fornecedor):
        print("ID:" , dados_fornecedor["id"])
        print("Nome:" , dados_fornecedor["nome"])

    def seleciona_usuario(self):
        id = int(input("ID do fornecedor que deseja selecionar: "))
        return id
    
    def mostrar_mensagem(self, msg):
        print(msg)