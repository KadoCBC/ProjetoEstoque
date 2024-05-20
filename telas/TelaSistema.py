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
