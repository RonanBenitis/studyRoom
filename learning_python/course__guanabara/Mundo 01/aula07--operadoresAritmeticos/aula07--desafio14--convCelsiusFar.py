#=========================== Desafios 06 =========================
#Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
desaf = str('14')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

varCelsius = float(input('Informe o valor em graus celsius (apenas valor númerico separado por pontos): '))

print('O valor de {0:.2f} ºC equivale a {1:.2f} ºF'.format( varCelsius , ( varCelsius * 9 / 5 ) + 32 ))

#======================= Resolução Guanabara =====================
#O valor de 0 e 1 dentro das mascaras equivale a ordem de apresentação das informações no format. 0, equivale a 1º declaração dentro do format (1º valor antes da virgula), 1 equivale a 2º. Deixar vazio faz a mesma coisa nesse caso.