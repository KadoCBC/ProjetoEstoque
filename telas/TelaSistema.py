class TelaSistema():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Usuarios')
        print('[2] - Brindes')
        print('[3] - Movimentações')
        print('[0] - Encerrar sistema')
        escolha_usuario = int(input('Escolha um numero'))
        return escolha_usuario
