class BrindeRepetidoException(Exception):
    def __init__(self, nome):
        self.mensagem = "O brinde com nome {} já existe"
        super().__init__(self.mensagem.format(nome))