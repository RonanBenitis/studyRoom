#============= IMPORTAR MODULOS / BIBLIOTECAS =============

#Guanabara explica, em uma biblioteca chamada "Bebidas", para importa-la ao nosso corpo, caso nosso corpo rodasse python, seria:
#import bebida (import biblioteca) = Mais generalista

#Caso quisessemos importar um elemento especifico dessa biblioteca, não TODA ELA, no caso, só queremos o cafezinho, fariamos, então:
#from bebida import cafezinho (from biblioteca import elemento) = mais especifico, economiza memória

#============= MODULO MATH =============

#o módulo math, biblioteca nativa do Python (mas necessita importação) tem as seguintes funções em seu escopo:

## ceil = arredonda um numero para cima
## floor = arredonda um numero pra baixo
## trunc = deixa o numero truncado, ou seja, tira todo o valor decimal e deixa só o valor inteiro. 7.98 viraria 7.
## pow = Power, potência, semelhante aos **
## sqrt = Square root, ou seja, raiz quadrada
## factorial = calculo fatorial

#Import generico: import math = chama todo o modulo
#Import especifico: from math import sqrt = chama apenas a função da raiz quadrada, todas as outras funções não funcionarão.
#Import especifico multiplo: from math import sqrt, ceil = Importa-se, da biblioteca math, a função sqrt e ceil.

import math

num = int(input('Digite um numero: '))
raiz = math.sqrt(num)
    #Para chamar função de uma importação genérica, é necessário indicar a biblioteca da função seguido de ponto: math.sqrt() no caso.

print('A raiz de {} é {:.2f}. Arrendondando pra cima dá {} e para baixo dá {}'.format(num, raiz, math.ceil(raiz), math.floor(raiz)))

from math import sqrt, floor, ceil
    #Se apertar ctrl + espaço abrirá menu de sugestões a qualquer momento. Professor fez isso após o import pra mostrar as ferramentas que o módulo math possui

num = int(input('Digite um numero: '))
raiz = sqrt(num)
    #Fazendo importação especifica de uma função, não há a necessidade de indicar o caminho da biblioteca (math.sqrt, vai diero para a função sqrt)

print('A raiz de {} é {:.2f}. Arrendondando pra cima dá {} e para baixo dá {}'.format(num, raiz, ceil(raiz), floor(raiz)))

# === Onde vejo as bibliotecas que posso importar? ===
# Vá no site oficial (python.org) > 
# Docs (menu sup) > 
# Veja a versão digitando "python" no console e deixe na versão desejada no site > 
# Library Reference: Acessa a documentação de todos os módulos padrão de Python (estamos usando o módulo math, que faz parte da categoria Numeric and Mathematical Modules)

# === Trabalhando com o módulo random ===

import random

num = random.randint(1, 10)
    # a função random, da bibloteca random, retorna um valor float randomizado entre 0 a 1, Caso queiramos ter um valor randomico int em determinado range, colocamos randint(x, y)
print(num)

# === PyPi, Python Package Index ===
# No site oficial do python, menu superior, clique em PyPi. Lá conseguimos visualizar todos os pacotes externos que conseguiremos importar para nosso programa . Atualmente, para dar browse igual ao Guanabara, precisamos colocar > Navegar Projetos > Projetos compativeis com Python 3 > Filtrar por classificador > Topic (aí tem os tópicos igual ao do video do Guanabara)

# === Importando Pacote Externo ===

# Para importar, faremos diferente do Guanabara, pois, o PyCharm consegue baixar clicando no nome da biblioteca o qual não foi baixado e precisa ser importado. Aqui, usaremos o console atravéz do pip. A forma está documentada no modulo "emoji" em PyPi
# Forma, nesse caso: python -m pip install emoji --upgrade

import emoji
    # instalação feita, podemos utilizar agora

print(emoji.emojize("Olá, Mundo! 😎"))

# Agora parou de funcionar, pois desinstalamos usando: python -m pip uninstall emoji