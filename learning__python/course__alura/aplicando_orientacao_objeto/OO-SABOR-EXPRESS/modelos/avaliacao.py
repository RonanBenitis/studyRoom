class Avaliacao:
    def __init__(self, cliente, nota):
        # Lembrando de acrescentar o underscore
        # É a forma pythonica de dizer "Cuidado ao manipular estes dados"
        # sendo a forma de dizer que são privados/protegidos
        self._cliente = cliente
        self._nota = nota