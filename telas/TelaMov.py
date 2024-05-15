class TelaMov():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Registrar movimento')
        print('[2] - listar movimento')
        print('[3] - Alterar movimento')
        print('[4] - exluir movimento')
        print('[0] - Retornar')
        escolha_usuario = int(input('Escolha um numero'))
        return escolha_usuario
        
    def dados_movimento(self):
        qt_mov = int(input('Quantidade: '))
        instituidor = input('Instituidor: ')
        motivo = input('Motivo: ')
        return {"quantidade": qt_mov, "instituidor": instituidor, "motivo": motivo}
    
    def escolhe_brinde(self):
        escolha_brinde = input("Qual é o brinde: ")
        return escolha_brinde
    
    def mostrar_movimento(self, dados_mov):
        print('--------------------------------------------')
        print("Data: ", dados_mov["data"])
        print("Brinde: ", dados_mov["brinde"] )
        print("Tipo: ", dados_mov["tipo"])
        print("Quantidade:" , dados_mov["qt_mov"])
        print("Instituidor:" , dados_mov["instituidor"])
        print("Motivo:", dados_mov["motivo"])
        print("Codigo:", dados_mov["codigo"])
    
    def seleciona_movimento(self):
        codigo = int(input("Codigo da movimentacao que deseja selecionar: "))
        return codigo