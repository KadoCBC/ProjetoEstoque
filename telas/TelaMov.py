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
            [sg.Text('--------- Movimentações ---------', font=("Helvica", 25))],
            [sg.Text('Escolha sua opção', font=("Helvica", 15))],
            [sg.Radio('Registrar movimento', "RD1", key='1')],
            [sg.Radio('Listar movimento', "RD1", key='2')],
            [sg.Radio('Excluir movimento', "RD1", key='3')],
            [sg.Radio('Ranking de brindes', "RD1", key='4')],
            [sg.Radio('Retornar', "RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de Brindes').Layout(layout)


    def dados_movimento(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Movimentação --------', font=("Helvica", 25))],
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
            [sg.Text('-------- Qual Brinde Deseja Movimentar --------', font=("Helvica", 25))],
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
            [sg.Text('-------- Selecionar Movimentação --------', font=("Helvica", 25))],
            [sg.Text('Digite o codigo da movimentação:', font=("Helvica", 15))],
            [sg.Text('CODIGO:', size=(15, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Seleciona Brinde').Layout(layout)

        button, values = self.open()
        codigo_lido = values['codigo']
        codigo = self.le_num_inteiro(codigo_lido)
        
        self.close()
        return codigo
    
    def mostrar_rank(self, matriz_rank):
        string_todos_rank = ""
        lista_nome = matriz_rank[0]
        lista_quantidade = matriz_rank[1]
        posicao_rank = 1
        while len(lista_quantidade) > 0 or posicao_rank > 10:
            maior_qt = lista_quantidade[0]
            indice_nome = 0
            indice_atual = 0
            for dado in lista_quantidade:
                if maior_qt > dado:
                    maior_qt = dado
                    indice_nome = indice_atual
                indice_atual = indice_atual + 1
            string_todos_rank = string_todos_rank + str(posicao_rank)+ "° BRINDE: " + str(lista_nome[indice_nome]) + '\n'
            string_todos_rank = string_todos_rank + "Quantidade: " + str(maior_qt) + '\n\n'
            del lista_nome[indice_nome]
            del lista_quantidade[indice_nome]
            posicao_rank = posicao_rank + 1

        sg.Popup('-------- LISTA DE MOVIMENTAÇÕES ----------', string_todos_rank)
    
    def mostrar_mensagem(self, msg):
        sg.popup("", msg)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

