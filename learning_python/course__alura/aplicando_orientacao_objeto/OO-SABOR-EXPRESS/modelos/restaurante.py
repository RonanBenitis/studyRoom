from modelos.avaliacao import Avaliacao

class Restaurante:
    '''Representa um restaurante e suas características.'''
    restaurantes = []

    # NOTE: Importante não iniciar com avaliações
    # pois não é responsabilidade do construtor de Restaurante
    # definir avaliações. Isso define-se em função específica
    def __init__(self, nome, categoria):
        '''
        Inicializa uma instância de Restaurante.

        Parâmetros:
        - nome (str): O nome do restaurante.
        - categoria (str): A categoria do restaurante.
        '''
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        '''Retorna uma representação em string do restaurante.'''
        return f'{self._nome} | {self._categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        '''Exibe uma lista formatada de todos os restaurantes.'''
        print(
            f'{'Nome do restaurante'.ljust(25)} | '
            f'{'Categoria'.ljust(25)} | '
            f'{'Avaliação'.ljust(25)} | '
            f'{'Status'}'
        )

        for restaurante in cls.restaurantes:
            media = restaurante.media_avaliacoes if restaurante.media_avaliacoes else 'Restaurante não avaliado'

            print(
                f'{restaurante._nome.ljust(25)} | '
                f'{restaurante._categoria.ljust(25)} | '
                f'{media.ljust(25)} | '
                f'{restaurante.ativo}'
            )
    
    @property
    def ativo(self):
            '''Retorna um símbolo indicando o estado de atividade do restaurante.'''
            return 'Ativo' if self._ativo else 'Inativo'
    
    def _alternar_estado(self):
        '''Alterna o estado de atividade do restaurante.'''
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        '''
        Registra uma avaliação para o restaurante.

        Parâmetros:
        - cliente (str): O nome do cliente que fez a avaliação.
        - nota (float): A nota atribuída ao restaurante (entre 1 e 5).
        '''
        def insert_rating(self, cliente, nota):
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
            print(f'Nota {nota} de {cliente} para o restaurante {self._nome} ' 
                  f'registrada com sucesso!')

        if 0 <= nota <= 5:
            insert_rating(self, cliente, nota)
        else:
            print(f'Nota de {cliente} para restaurante {self._nome} invalida!')

            while True:
                nota = int(input(f'Insira uma nota de 0 a 5 para o restaurante {self._nome}: '))
                if 0 <= nota <= 5:
                    insert_rating(self, cliente, nota)
                    break
                else:
                    print('Nota inserida invalida!')
        

    @property
    def media_avaliacoes(self):
        '''Calcula e retorna a média das avaliações do restaurante.'''
        # se o restaurante tiver nenhuma avaliação
        # ou seja, lista vazia:
        if not self._avaliacao:
            return None
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)

        # round arredonda o número para o número de casas
        # que definimos em seu parametro. round(valor, num_casas)
        return f'{round(soma_notas / quantidade_notas, 1)}'