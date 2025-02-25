# Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão.
class Livro:
    livros = []
    livros_disponiveis = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)
        Livro.livros_disponiveis.append(self)

    # Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.
    def __str__(self):
        return (
            f'Titulo: {self._titulo.ljust(25)} | '
            f'Autor: {self._autor.ljust(25)} | '
            f'Publicação: {self._ano_publicacao.ljust(25)}'
        )
    
    # Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False. 
    def emprestar(self):
        Livro.livros_disponiveis.remove(self)
        self._disponivel = False

    # Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @classmethod
    def verificar_disponibilidade(cls, ano):
        ano = str(ano)
        lista_geral = cls.livros
        lista_disponiveis = cls.livros_disponiveis
        lista_disponiveis_ano = [livro._ano_publicacao for livro in lista_disponiveis]

        if not lista_geral:
            print('Lista completamente vazia')
        elif not lista_disponiveis:
            print('Todos os livros encontram-se emprestados')
        elif ano not in lista_disponiveis_ano:
            print('Não há livros disponiveis com esta data de publicação')
        else:
            print(f'>> Livros disponiveis publicados em {ano}: ')
            for livro in lista_disponiveis:
                if livro._ano_publicacao == ano:
                    print(livro)