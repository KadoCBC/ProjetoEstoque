import PySimpleGUI as sg
from telas.TelaAbstract import TelaAbstract

class TelaPreco(TelaAbstract):

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
            [sg.Text('--------- Preços ---------', font=("Helvica", 25))],
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
            [sg.Text('-------- Dados Brinde --------', font=("Helvica", 25))],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='valor')],
            [sg.Text('Data:', size=(15, 1)), sg.InputText('', key='data')],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        valor = str(values['valor'])
        data = values['data']
        id_lido = values['id']
        id =  self.le_num_inteiro(id_lido)

        self.close()
        return {"valor": valor, "data": data, "id": id}
    
    def mostrar_preco(self, dados_preco):
        string_todos_preco = ""
        for dado in dados_preco:
            string_todos_preco = string_todos_preco + "VALOR: R$" + str(dado["valor"]) + '\n'
            string_todos_preco = string_todos_preco + "DATA: " + str(dado["data"]) + '\n'
            string_todos_preco = string_todos_preco + "ID: " + str(dado["id"]) + '\n\n'
        sg.Popup('-------- LISTA DE PREÇOS ----------', string_todos_preco)

    def seleciona_preco(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Preço --------', font=("Helvica", 25))],
            [sg.Text('Digite o id do Preço:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Preço').Layout(layout)

        button, values = self.open()
        id_lido = values['id']
        id =  self.le_num_inteiro(id_lido)
        
        self.close()
        return id
    
    def seleciona_fornecedor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Fornecedor --------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do fornecedor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='ID')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona fornecedor').Layout(layout)

        button, values = self.open()
        id = values['ID']
        self.close()
        return self.le_num_inteiro(id)
    
    def seleciona_brinde(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Brinde --------', font=("Helvica", 25))],
            [sg.Text('Digite o nome do Brinde:', font=("Helvica", 15))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Preço').Layout(layout)

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
