import PySimpleGUI as sg
from telas.TelaAbstract import TelaAbstract 


class TelaMov(TelaAbstract):

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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- MOVIMENTAÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('QUANTIDADE:', size=(15, 1)), sg.InputText('', key='qt_mov')],
            [sg.Text('INSTITUIDOR:', size=(15, 1)), sg.InputText('', key='instituidor')],
            [sg.Text('MOTIVO:', size=(15, 1)), sg.InputText('', key='motivo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        instituidor = values['instituidor']
        quantidade = values['qt_mov']
        motivo = values['motivo']
        qt_mov = self.le_num_inteiro(quantidade)

        self.close()
        return {"instituidor": instituidor, "qt_mov": qt_mov, "motivo": motivo}
    
    def escolhe_brinde(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- QUAL BRINDE DESEJA MOVIMENTAR ----------', font=("Helvica", 25))],
            [sg.Text('NOME DO BRINDE:', size=(15, 1)), sg.InputText('', key='brinde')],
            [sg.Text('ID DO RESPONSAVEL:', size=(15, 1)), sg.InputText('', key='id')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)

        button, values = self.open()
        brinde = str(values['brinde'])
        id = values['id']
        usuario_id = self.le_num_inteiro(id)
        
        self.close()
        return {"brinde": brinde, "usuario": usuario_id}
    
    def mostrar_movimento(self, dados_mov):
        string_todos_mov = ""
        for dado in dados_mov:
            string_todos_mov = string_todos_mov + "DATA: " + str(dado["data"]) + '\n'
            string_todos_mov = string_todos_mov + "BRINDE: " + str(dado["brinde"]) + '\n'
            string_todos_mov = string_todos_mov + "TIPO: " + str(dado["tipo"]) + '\n'
            string_todos_mov = string_todos_mov + "QUANTIDADE: " + str(dado["qt_mov"]) + '\n'
            string_todos_mov = string_todos_mov + "INSTITUIDOR: " + str(dado["instituidor"]) + '\n'
            string_todos_mov = string_todos_mov + "MOTIVO: " + str(dado["motivo"]) + '\n'
            string_todos_mov = string_todos_mov + "RESPONSAVEL: " + str(dado["usuario"]) + '\n'
            string_todos_mov = string_todos_mov + "CODIGO: " + str(dado["codigo"]) + '\n\n'


        sg.Popup('-------- LISTA DE MOVIMENTAÇÕES ----------', string_todos_mov)

    def seleciona_movimento(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- SELECIONAR MOVIMENTAÇÃO ----------', font=("Helvica", 25))],
            [sg.Text('Digite o codigo da movimentação:', font=("Helvica", 15))],
            [sg.Text('CODIGO:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Brinde').Layout(layout)

        button, values = self.open()
        codigo = int(values['codigo'])
        self.close()
        return codigo
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
