import PySimpleGUI as sg
from telas.TelaAbstract import TelaAbstract 


class TelaUsuario(TelaAbstract):

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
            [sg.Text('--------- Usuarios ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Incluir usuario', "RD1", key='1')],
            [sg.Radio('Listar usuario', "RD1", key='2')],
            [sg.Radio('Alterar usuario', "RD1", key='3')],
            [sg.Radio('Excluir usuario', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)


    def pega_dados_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Dados Usuario --------', font=("Helvica", 25))],
            [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        nome = values['nome']

        self.close()
        return {"nome": nome}
    
    def mostrar_usuario(self, dados_usuario):
        string_todos_usuarios = ""
        for dado in dados_usuario:
            string_todos_usuarios = string_todos_usuarios + "NOME DO USUARIO: " + dado["nome"] + '\n'
            string_todos_usuarios = string_todos_usuarios + "ID: " + str(dado["id"]) + '\n'

        sg.Popup('-------- LISTA DE USUARIOS ----------', string_todos_usuarios)

    def seleciona_usuario(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Selecionar Usuario --------', font=("Helvica", 25))],
            [sg.Text('Digite o ID do usuario que deseja selecionar:', font=("Helvica", 15))],
            [sg.Text('ID:', size=(15, 1)), sg.InputText('', key='ID')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona usuario').Layout(layout)

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