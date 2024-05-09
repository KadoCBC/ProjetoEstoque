class TelaUsuario():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Criar Novo Usuario')
        print('[0] - Retornar')
        escolha_usuario = int(input('Escolha um numero'))
        return escolha_usuario
        
    def pega_dados_usuario(self):
        nome = input('Nome: ')
        id = input('id: ')
        
        return {"nome": nome, "id": id}
    
    