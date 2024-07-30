from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(
            f'{'Nome do restaurante'.ljust(25)} | '
            f'{'Categoria'.ljust(25)} | '
            f'{'Avaliação'.ljust(25)} | '
            f'{'Status'}'
        )

        for restaurante in cls.restaurantes:
            print(
                f'{restaurante._nome.ljust(25)} | '
                f'{restaurante._categoria.ljust(25)} | '
                f'{str(restaurante.media_avaliacoes).ljust(25)} | '
                f'{restaurante.ativo}'
            )
    
    @property
    def ativo(self):
            return 'Ativo' if self._ativo else 'Inativo'
    
    def _alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        # se o restaurante tiver nenhuma avaliação
        # ou seja, lista vazia:
        if not self._avaliacao:
            return 0
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)

        # round arredonda o número para o número de casas
        # que definimos em seu parametro. round(valor, num_casas)
        return f'{round(soma_notas / quantidade_notas, 1)}'