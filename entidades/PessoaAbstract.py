from abc import ABC, abstractmethod

class Pessoa(ABC):
    @abstractmethod
    def __init__(self, nome: str, id:int):
        self.__nome = nome
        self.__id = id

    @property
    def nome(self):
        return self.__nome
    
    @property
    def id(self):
        return self.__id
    
    @nome.setter
    def nome(self, nome:str):
        self.__nome = nome
