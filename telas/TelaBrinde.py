import PySimpleGUI as sg
from telas.TelaAbstract import TelaAbstract 


class TelaBrinde(TelaAbstract):

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
        if values['5']:
            opcao = 5
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('------------ Brindes ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir Brinde', "RD1", key='1')],
            [sg.Radio('Listar Brinde', "RD1", key='2')],
            [sg.Radio('Alterar Brinde', "RD1", key='3')],
            [sg.Radio('Excluir Brinde', "RD1", key='4')],
            [sg.Radio('Informações Brinde', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

    def pega_dados_brinde(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS BRINDE ----------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Text('Quantidade:', size=(15, 1)), sg.InputText('', key='quantidade')],
            [sg.Text('Categoria:', size=(15, 1)), sg.InputText('', key='categoria_brinde')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        nome = str(values['nome'])
        qt = values['quantidade']
        quantidade = self.le_num_inteiro(qt)
        categoria_brinde = values['categoria_brinde']

        self.close()
        return {"nome": nome, "quantidade": quantidade, "categoria_brinde": categoria_brinde}
    
    def mostrar_brinde(self, dados_brinde):
        string_todos_brinde = ""
        for dado in dados_brinde:
            string_todos_brinde = string_todos_brinde + "ID: " + str(dado["id"]) + '\n'
            string_todos_brinde = string_todos_brinde + "BRINDE: " + str(dado["nome"]) + '\n'
            string_todos_brinde = string_todos_brinde + "QUANTIDADE: " + str(dado["quantidade"]) + '\n\n'
            #falta incluir preco e categoria(no controlador também)
        sg.Popup('-------- LISTA DE BRINDES ----------', string_todos_brinde)

    def seleciona_brinde(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR BRINDE ----------', font=("Helvica", 25))],
            [sg.Text('Digite o nome do Brinde:', font=("Helvica", 15))],
            [sg.Text('NOME:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Brinde').Layout(layout)

        button, values = self.open()
        nome = values['nome']
        self.close()
        return nome
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
