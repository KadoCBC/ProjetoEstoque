import PySimpleGUI as sg


class TelaPreco():

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
            [sg.Text('------------ Preços ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Criar Preço', "RD1", key='1')],
            [sg.Radio('Listar Preços', "RD1", key='2')],
            [sg.Radio('Alterar Preço', "RD1", key='3')],
            [sg.Radio('Excluir Preço', "RD1", key='4')],
            [sg.Radio('Vincular Preço', "RD1", key='5')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

    def pega_dados_preco(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- DADOS BRINDE ----------', font=("Helvica", 25))],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        valor = str(values['valor'])
        data = values['data']
        id = values['id']

        self.close()
        return {"valor": valor, "data": data, "id": id}
    
    def mostrar_preco(self, dados_preco):
        string_todos_preco = ""
        for dado in dados_preco:
            string_todos_preco = string_todos_preco + "VALOR" + str(dado["valor"]) + '\n'
            string_todos_brinde = string_todos_brinde + "DATA: " + str(dado["data"]) + '\n'
        sg.Popup('-------- LISTA DE PREÇOS ----------', string_todos_preco)

    def seleciona_preco(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR PREÇO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o id do Preço:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Preço').Layout(layout)

        button, values = self.open()
        id = values['id']
        self.close()
        return id
    
    def escolhe_fornecedor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- FORNECEDOR ----------', font=("Helvica", 25))],
            [sg.Text('Fornecedor:', size=(15, 1)), sg.InputText('', key='fornecedor')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        id_fornecedor = values['fornecedor']
        self.close()
        return id_fornecedor

    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
