import PySimpleGUI as sg



class TelaSistema():

    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('------------ TELA INICIAL ------------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Usuarios', "RD1", key='1')],
            [sg.Radio('Fornecedores', "RD1", key='2')],
            [sg.Radio('Brindes', "RD1", key='3')],
            [sg.Radio('Movimentações', "RD1", key='4')],
            [sg.Radio('Preços', "RD1", key='5')],
            [sg.Radio('Categorias', "RD1", key='6')],
            [sg.Radio('Encerrar sistema', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
