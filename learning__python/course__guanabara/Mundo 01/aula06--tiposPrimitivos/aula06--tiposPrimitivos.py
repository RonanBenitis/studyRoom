# Existem 4 tipos primitos principais, mas pro Python existem mais até. Focaremos nestes 4 por enquanto.
# Boas praticas para string: Usar aspas simples

n1=int(input('Digite um numero: ')) # Necessita informar o tipo do valor pois o input sempre retornará string, assim, transformaremos a string em outro valor.
n2=int(input('Digite um numero: '))
s=n1+n2

print('A soma entre {} e {} vale {}'.format(n1, n2, s)) # Essa é uma sintaxe nova, sintaxe Python 3, não usando mais %.
# Veja que no format estamos definindo os valores das três mascaras informadas dentro do texto, isso no mesma função (mesmo format)

# Os 4 tipos primitivos básicos no Python: 
# - int (interger/inteiro): 7 / -4 / 0 / 9875
# - float (Numero de ponto flutuante/numero real): 4.5 / 0.076 / -15.223 / 7.0 (esse ultimo valor não é inteiro, está sendo representado como ponto flutuante)
# - bool (Booleano: Aceita somente 2 valores que é True e False [True e False precisam estar com a primeira letra maiuscula]). Se tiver um valor declarado dentro do bool ele retornara True, se tiver nada ou 0 retornará False.
# - str (string/sequencia de caracteres): 'Olá' / '7.5' / ' ' (string vazia também é string)

# Função is (retorna True e False): isnumeric() = Verifica se é possivel converter este número inserido com um tipo primitivo int antes dele;
# = isalpha() = verifica se o valor inserido pode ser convertido em alfabetico (pois, podemos ter string de numeros e isso dara False); 
# - isalphanum() = verifica se o numero inserido é letra (alfabético) e se é numerico;
# - isupper() = Veja se está somente em letras maiusculas.

#=========================================================

#Desafio 1
n1=int(input('Insira numero: '))
n2=int(input('Insira numero: '))

print('A soma de {} e {} é {}'.format(n1, n2, n1+n2))

#Desafio 2
var=input('Insira algo: ')

print('EO tipo primito desse valor é {}'.format(type(var)))
print('Só tem espaços? {}'.format(var.isspace()))
print('Verifica se {} pode ser convertido em alfabetico (pois, podemos ter string de numeros e isso dara False): T/F - {} '.format(var,var.isalpha()))
print('Verifica se {} é possivel de converter este número inserido com um tipo primitivo int antes dele: T/F - {}'.format(var,var.isnumeric()))
print('{} é alfanúmerico? T/F - {}'.format(var.isalnum()))
print('Valida se {} é somente em letras maiusculas: T/F - {}'.format(var,var.isupper()))
print('{} está em minusculas? {}'.format(var.islower()))
print('{} está capitalizada (Somente com a primeira letra maiuscula)? T/F {}'.format(var.istitle))