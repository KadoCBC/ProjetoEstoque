class TelaUsuario():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Criar Novo Usuario')
        print('[2] - listar Usuario')
        print('[3] - Alterar Usuario')
        print('[4] - exluir Usuario')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True:
            escolha_usuario = input('Escolha um número: ')
            try:
                escolha_usuario = int(escolha_usuario)
                if 0 <= escolha_usuario <= 4:
                    return escolha_usuario
                else:
                    print('Digite um número válido entre 0 e 4.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')
        
    def pega_dados_usuario(self):
        nome = input('Nome: ')
        return {"nome": nome}
    
    def mostrar_usuario(self, dados_usuario):
        print("ID:" , dados_usuario["id"])
        print("Nome:" , dados_usuario["nome"])

    def seleciona_usuario(self):
        id = int(input("ID do usuario que deseja selecionar: "))
        return id
    
    def mostrar_mensagem(self, msg):
        print(msg)
