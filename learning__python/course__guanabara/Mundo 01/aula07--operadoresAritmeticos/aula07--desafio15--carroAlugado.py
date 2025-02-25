#=========================== Desafios 15 =========================
desaf = str('15')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorrido = float(input('Informe a quantidade em km percorrido neste carro: '))
qtdDias = int(input('Informe a quantidade de dias utilizados com este carro: '))
valorDia = 60.00
valorKm = 00.15

calcDia = qtdDias * valorDia
calcKm = valorKm * kmPercorrido

print('Para este carro alugado, o qual percorreu {:.2f} km em {} dia(s), terá como valor diario de R${:.2f}, somando o valor percorrido de R${:.2f}, totalizando R${:.2f}'.format(kmPercorrido , qtdDias , calcDia , calcKm , calcDia + calcKm))

#======================= Resolução Guanabara =====================
# Guanabara resolveu de forma mais modularizada, ou seja, calculou dia * valor, printou o valor. Calculo o resultado anterior * o km * valorKm, printou o valor. O intuito do exercicio é MODULARIZAR, DIVIDIR PRA CONQUISTAR, pra facilitar na identificação de problemas caso os encontre
# Ou seja, faça um pedaço e teste, faça outro pedaço e teste.