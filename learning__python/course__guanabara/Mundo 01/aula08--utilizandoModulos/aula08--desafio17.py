# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo. Calcule e mostre o comprimento da hipotenusa

# Faça tudo isso usando modulos do math

from math import hypot

catOp = float(input('Valor do cateto oposto: '))
catAdj = float(input('Valor do cateto adjascente: '))

print('O valor do cateto oposto inserido foi {} e o valor do cateto adjascente inserido foi {} e, sendo um triangulo retangulo, sua hipotenusa será {}'.format(catOp, catAdj, hypot(catOp, catAdj)))

# == Resolução do Guanabara ==

# >>> Método escrita matematica
# Guanabara demonstrou primeiramente a maneira matematica, onde, ao invés de utilizar módulo math, utilizando a equação escrita:
# co = float(input('Comprimento do cateto oposto: ))
# ca = float(input('Comprimento do cateto adjascente: ))
# hi = (co ** 2 + ca ** 2) ** (1/2)
# print ('A hipotenusa vai meidr {:.f}'.format(hi))

# >>> Método importação de módulo
#Posteriormente, Guanabara realizou da forma que realizamo também.