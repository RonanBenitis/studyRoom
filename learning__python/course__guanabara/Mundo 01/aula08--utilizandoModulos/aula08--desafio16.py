# Crie um programa que leia um numero Real qualquer pelo teclado e mostre na tela a sua porção inteira

#Ex: Digite um número: 6.127, O número 6.127 tem a parte inteira 6.
from math import floor

num = float(input('Insira um número: '))

print('O número {} tem como sua parte inteira o número {}.\nEste retorno foi feito diretamento mostrando o valor do número inserido (recebido como float) em inteiro'.format(num, int(num)))
print('\nO número {} tem como sua parte inteira o número {}.\nEsse retorno foi usando o módulo math, colocando a função "floor" '. format(num, floor(num)))

# == Explicação Guanabara ==

# Guanabara utilizou o método "trunc" da biblioteca math, que é truncate. Guanabara mostrou as duas formas de importação (biblioteca inteira e só do método específico)