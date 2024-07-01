import PySimpleGUI as sg
from telas.TelaAbstract import TelaAbstract 


class TelaFornecedor(TelaAbstract):

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
        if values['6']:
            opcao = 6
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao

    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('--------- Fornecedores ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir fornecedor', "RD1", key='1')],
            [sg.Radio('Listar fornecedores', "RD1", key='2')],
            [sg.Radio('Alterar fornecedor', "RD1", key='3')],
            [sg.Radio('Excluir fornecedor', "RD1", key='4')],
            [sg.Radio('Adicionar endereço', "RD1", key='5')],
            [sg.Radio('Listar endereços', "RD1", key='6')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)


    def pega_dados_fornecedor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Dados Fornecedor --------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return {"nome": nome}
    
    def pega_dados_endereco(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Dados Endereço--------', font=("Helvica", 25))],
            [sg.Text('rua:', size=(15, 1)), sg.InputText('', key='rua')],
            [sg.Text('complemento:', size=(15, 1)), sg.InputText('', key='complemento')],
            [sg.Text('bairro:', size=(15, 1)), sg.InputText('', key='bairro')],
            [sg.Text('Cidade:', size=(15, 1)), sg.InputText('', key='cidade')],
            [sg.Text('CEP:', size=(15, 1)), sg.InputText('', key='cep')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        rua = values['rua']
        complemento = values['complemento']
        bairro = values['bairro']
        cidade = values['cidade']
        cep = values['cep']
        
        self.close()
        return {"rua": rua, "complemento": complemento,"bairro": bairro, "cidade": cidade,"cep": cep}
    
    def mostrar_fornecedor(self, dados_fornecedor):
        string_todos_fornecedores = ""
        for dado in dados_fornecedor:
            string_todos_fornecedores = string_todos_fornecedores + "NOME DO FORNECEDOR: " + dado["nome"] + '\n'
            string_todos_fornecedores = string_todos_fornecedores + "ID: " + str(dado["id"]) + '\n'

        sg.Popup('-------- LISTA DE FORNECEDORES ----------', string_todos_fornecedores)

    def mostrar_endereco(self, dados_endereco):
        string_todos_enderecos = ""
        for dado in dados_endereco:
            string_todos_enderecos = string_todos_enderecos + "RUA: " + dado["rua"] + '\n'
            string_todos_enderecos = string_todos_enderecos + "COMPLEMENTO: " + dado["complemento"] + '\n'
            string_todos_enderecos = string_todos_enderecos + "BAIRRO: " + dado["bairro"] + '\n'
            string_todos_enderecos = string_todos_enderecos + "CIDADE: " + dado["cidade"] + '\n'
            string_todos_enderecos = string_todos_enderecos + "CEP: " + dado["cep"]

        sg.Popup('-------- LISTA DE ENDEREÇOS ----------', string_todos_enderecos)

    def seleciona_fornecedor(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Fornecedor ----------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do fornecedor que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='ID')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona fornecedor').Layout(layout)

        button, values = self.open()
        id = values['ID']
        self.close()
        return self.le_num_inteiro(id)
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values