import PySimpleGUI as sg


class TelaMov():

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        #fazer tratamento
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('------------ Brindes ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Registrar movimento', "RD1", key='1')],
            [sg.Radio('Listar movimento', "RD1", key='2')],
            [sg.Radio('Exluir movimento', "RD1", key='3')],
            [sg.Radio('Ranking de brindes', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

    def dados_movimento(self):
        qt_mov = int(input('Quantidade: '))
        instituidor = input('Instituidor: ')
        motivo = input('Motivo: ')
        return {"quantidade": qt_mov, "instituidor": instituidor, "motivo": motivo}

    def escolhe_brinde(self):
        escolha_brinde = input("Qual é o brinde: ")
        return escolha_brinde



    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
'''
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
        

    

    
    def escolhe_usuario(self):
        escolha_usuario = int(input("Escolha o id do usuario: "))
        return escolha_usuario
    
    def mostrar_movimento(self, dados_mov):
        print('--------------------------------------------')
        print("Data: ", dados_mov["data"])
        print("Brinde: ", dados_mov["brinde"] )
        print("Tipo: ", dados_mov["tipo"])
        print("Quantidade:" , dados_mov["qt_mov"])
        print("Instituidor:" , dados_mov["instituidor"])
        print("Motivo:", dados_mov["motivo"])
        print("Responsavel", dados_mov["usuario"])
        print("Codigo:", dados_mov["codigo"])
    
    def seleciona_movimento(self):
        codigo = int(input("Codigo da movimentacao que deseja selecionar: "))
        return codigo
    
    def mostrar_mensagem(self, msg, complemento = ''):
        if complemento != '':
            print(msg , end = '')
            print(f" ({complemento})")
        else: 
            print(msg)
'''