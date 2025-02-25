from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Decorator de indicação de classe abstrada
    # Necessita da classe ABC ou derivada da metaclasse ABCMethod
    @abstractmethod
    def aplicar_desconto(self):
        pass