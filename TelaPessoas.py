class TelaPessoas():

    def tela_opcoes(self):
        print('Escolha o que fazer')
        opcao = int(input('Escolha um numero'))
        return opcao
        
    def pega_dados_usuario(self):
        nome = input('Nome: ')
        id = input('id: ')
        
        return {"nome": nome, "id": id}
    
    