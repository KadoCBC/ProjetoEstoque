class TelaSistema():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Usuarios')
        print('[2] - Fornecedores')
        print('[3] - Brindes')
        print('[4] - Movimentações')
        print('[5] - Preços')
        print('[6] - Categorias')
        print('[0] - Encerrar sistema')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True :
            escolha_usuario = int(input('Escolha um numero: '))
            if escolha_usuario >= 0 and escolha_usuario <= 6:
                return escolha_usuario
            else:
                print('Digite um número valido')
