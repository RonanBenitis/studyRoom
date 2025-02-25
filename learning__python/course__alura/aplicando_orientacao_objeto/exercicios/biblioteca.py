# Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from livro import Livro

# Crie duas instâncias da classe Livro e imprima essas instâncias.
livro_um = Livro('Duna', 'Frank Herbert', '1997')
livro_dois = Livro('Senhor dos Aneis', 'Tolkien', '1950')
print(livro_um)
print(livro_dois)

# No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está disponível ou não após o empréstimo.
livro_dois.emprestar()
print(livro_dois._disponivel)

# No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Livro.verificar_disponibilidade(1997)

# Crie um arquivo chamado main.py, importe a classe Livro e, no arquivo main.py, instancie dois objetos da classe Livro e exiba a mensagem formatada utilizando o método str.
# Este exercicio considerarei realizado pois seria fazer a mesma coisa em um arquivo de nome diferente com, talvez, configurando-o como main através da validação do dunder method __name__ == '__main__".