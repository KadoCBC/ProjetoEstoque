class TelaMov():

    def tela_opcoes(self):
        print('---------TELA DE OPÇÕES----------')
        print('[1] - Registrar movimento')
        print('[2] - listar movimento')
        print('[3] - exluir movimento')
        print('[4] - ranking de brindes')
        print('[0] - Retornar')
        # Faz um loop até o input retornar um numero inteiro entre dois numeros
        while True:
            escolha_usuario = input('Escolha um número: ')
            try:
                escolha_usuario = int(escolha_usuario)
                if 0 <= escolha_usuario <= 4:
                    return escolha_usuario
                else:
                    print('Digite um número válido entre 0 e 4.')
            except ValueError:
                print('Entrada inválida. Por favor, digite um número.')
        
    def dados_movimento(self):
        qt_mov = int(input('Quantidade: '))
        instituidor = input('Instituidor: ')
        motivo = input('Motivo: ')
        return {"quantidade": qt_mov, "instituidor": instituidor, "motivo": motivo}
    
    def escolhe_brinde(self):
        escolha_brinde = input("Qual é o brinde: ")
        return escolha_brinde
    
    def escolhe_usuario(self):
        escolha_usuario = int(input("Escolha o id do usuario: "))
        return escolha_usuario
    
    def mostrar_movimento(self, dados_mov):
        print('--------------------------------------------')
        print("Data: ", dados_mov["data"])
        print("Brinde: ", dados_mov["brinde"] )
        print("Tipo: ", dados_mov["tipo"])
        print("Quantidade:" , dados_mov["qt_mov"])
        print("Instituidor:" , dados_mov["instituidor"])
        print("Motivo:", dados_mov["motivo"])
        print("Responsavel", dados_mov["usuario"])
        print("Codigo:", dados_mov["codigo"])
    
    def seleciona_movimento(self):
        codigo = int(input("Codigo da movimentacao que deseja selecionar: "))
        return codigo
    
    def mostrar_mensagem(self, msg, complemento = ''):
        if complemento != '':
            print(msg , end = '')
            print(f" ({complemento})")
        else: 
            print(msg)
