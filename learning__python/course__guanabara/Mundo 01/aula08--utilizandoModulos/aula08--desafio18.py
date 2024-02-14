# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desses angulos

from math import sin, cos, tan

ang = float(input('Insira o angulo desejado para calculo de seno, cosseno e tangente: '))

print('O angulo inserido foi {:.2f}º, seu seno, cosseno e tangente é:\n- Seno: {:.3f}\n- Cosseno: {:.3f}\n- Tangente: {:.3f}'.format(ang, sin(ang), cos(ang), tan(ang)))

# == Resolução Guanabara ==
# Erramos, nesse exercicio, o valor inserido, pois o valor do angulo inserido no sin, cos e tan deve ser representado em radianos, logo, precisa-se transformar o valor inserido.

# == Correção ==

from math import sin, cos, tan, radians

ang = float(input('Insira o angulo desejado: '))

print('O angulo inserido foi {:.2f}º. Seu valor em radianos equivale a {:.2f}, seu seno, cosseno e tangente é:\n- Seno: {:.2f}\n- Cosseno: {:.2f}\n- Tangente: {:.2f}'.format(ang, radians(ang), sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))