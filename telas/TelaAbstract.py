from abc import ABC, abstractmethod

class TelaAbstract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def le_num_inteiro(self, num):
        while True:
            valor_lido = num
            try:
                valor_valido = int(valor_lido)
                if isinstance(valor_valido,int):
                    return valor_valido
                else: 
                    raise ValueError #será lançada apenas se o número não é o esperado
            except ValueError: #aqui cai se não for int
                self.mostrar_mensagem('Digite um inteiro Valido!')
                return None
