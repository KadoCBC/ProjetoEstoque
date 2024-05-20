class TelaCategoriaBrinde:
    def tela_opcoes(self):
        print('----------- TELA DE OPÇÕES -----------')
        print('[1] - Criar nova Categoria')
        print('[2] - Listar Categorias')
        print('[3] - Alterar Categoria')
        print('[4] - Excluir Categoria')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True :
            escolha_usuario = int(input('Escolha um numero'))
            if escolha_usuario >= 0 and escolha_usuario <= 4:
                return escolha_usuario
            else:
                print('Digite um número valido')
        
    def pega_dados_categoria(self):
        nome = input('Nome: ')
        return {"nome": nome}
    
    def seleciona_categoria(self):
        nome = input("Nome da Categoria: ")
        return nome
    
    def mostrar_mensagem(self, msg):
        print(msg)

