#==================== OPERADORES ARITMÉTICOS ==================

# + : Adição
# - : Subtração
# * : Multiplicação
# / : Divisão
# ** : Potencia
# // : Divisão inteira
    # Divisão inteira retorna o valor do quociente inteiro. Se para continuar necessitaria este valor virar float, ele para por aí deixando a divisão com resto.
# % : Resto da divisão (módulo)
    # Retorna o valor do resto de uma divisão inteira (a que para antes de seu quociente virar decimal/float)
# (operador relacional) usa-se o == para dizer se uma operação é igual à outra. Um = só significa (recebe)
# Ordem de precedência: O que é executado primeiro, similar à matematica, mas só é utilizado parentenses e não chaves e colchetes para isso, eles tem outra função
# Logo, precedencia: 1º - Parenteses, 2º - Potencia (**), 3º - Multiplacação, divisão, divisão inteira e resto da divisão, na ordem de que eles aparecerem, 4º - Por fim, soma e subtração
# Um código funcioar != estar correto, seu resultado pode não estar correto.

#Função interna pow(x, y), sendo x o numero e y a pontecia. Pow, de power, funciona igual a potencialização mas perde-se a caracteristica de precedencia.

print(5+3*2) #Segue ordem 3, faz multiplicação antes
print(3*5+4**2) #Ordem: Precedencia 2, **, precedencia 3, *, precedencia 4.
print(3*(5+4)**2) #Prec 1, resolve parenteses, prec 2, **, prec 3, *

#========================== Raiz quadrada ===============

# Para fazer raiz quadrada, raiz cubica e afins necessita utilizar o operador de potencia e utilizar fração em parenteses, por exemplo:
# raiz quadrada == x**(1/2) // sendo x um numero qualquer
# raiz cubica == x**(1/3) // sendo x um numero qualquer

#======================= Operadores em string ==================

#Utilizar + em uma string irá concatenar
print('oi'+'olá') #retorna oiolá

#Multiplicação multiplicará a repetição da string
print('Oi'*5) #retornará 'OiOiOiOiOi'

#======================= Print e Operadores ==================

nome = input('Qual é seu nome?: ')

print('Prazer em conhecer {:20}'.format(nome)) #Printa a informação de dentro da mascara de subtituição em 20 caracteres/espaços
print('Prazer em conhecer {:>20}'.format(nome)) #Printa em 20 caracteres, colocando o valor da variavel alinhada a direita
print('Prazer em conhecer {:<20}'.format(nome)) #Idem de cima, mas a esquerda
print('Prazer em conhecer {:=20}'.format(nome)) #Idem de cima, mas coloca o valor da variável centralizada
print('Prazer em conhecer {:=^20}'.format(nome)) #Idem de cima, mas coloca o valor da variável centralizada e com iguais em volta

#======================= Operações ==================
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))

print('A soma de {} com {} é {}'.format(n1, n2, n1+n2)) #Geralmente se faz assim quando previsamos apenas do valor imediatamente. Se precisaremos utilizar o valor da soma posteriormente e varias vezes, aí recomenda-se atribuir em uma variavel.

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ') 
    #Veja que a 3º mascara está com o :.3f, isso significa que queremos que nesta mascara seja retornada um valor float de até 3 casas decimais
    # end=' ' = para não haver quebra de linha entre prints. Tem um espaço no meio para eles não ficarem colados. Se colocar algo dentro do end, retornará uma string do valor inserido no final deste print e no começo do próximo
    #\n = quebra de linha dentro do mesmo print

print('A divisão inteira {} e a potência {}'.format(di, e))
    #Nas masacaras é possivel setar ordem. Colocando 1, 2, 3 dentro das mascaras dizemos qual virá primeiro, qual virá depois e etc.