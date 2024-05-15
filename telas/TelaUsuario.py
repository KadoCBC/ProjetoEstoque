class TelaUsuario():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Criar Novo Usuario')
        print('[2] - listar Usuario')
        print('[3] - Alterar Usuario')
        print('[4] - exluir Usuario')
        print('[0] - Retornar')
        escolha_usuario = int(input('Escolha um numero'))
        return escolha_usuario
        
    def pega_dados_usuario(self):
        nome = input('Nome: ')
        return {"nome": nome}
    
    def mostrar_usuario(self, dados_usuario):
        print("ID:" , dados_usuario["id"])
        print("Nome:" , dados_usuario["nome"])

    def seleciona_usuario(self):
        id = int(input("ID do usuario que deseja selecionar: "))
        return id