#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

# Ex: Digite um número: 1834 = Unidade 4, dezena 3, centena 8, milhar 1. Tente fazer isso como string e matematicamente

# =====   RESOLUÇÃO MATEMATICA GUANABARA   =====

num = int(input('Insira um número entre 0 a 9999: ').strip())

un = num // 1 % 10
    # Se num = 1234, dividindo por 1 sua Divisão inteira (//) será 1234 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 4 (Divisão inteira será 123)
        # Se num = 1, dividindo por 1 sua Divisão inteira (//) será 1 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 1 (Divisão inteira será 0)
    # Para relemebrar e visualizar os operadores de Divisão Inteira e de Módulo: http://www.vision.ime.usp.br/~pmiranda/mac2166_1s13/aulas/aula05/aula05.html
dez = num // 10 % 10
    # Se num 1234, dividindo por 10 sua Divisão Inteira (//) será 123 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 3 (Divisão inteira será 12)
        # Se num = 1, dividindo por 10 sua Divisão inteira (//) será 0 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 0 (Divisão inteira será 0)
cen = num // 100 % 10
    # Se num 1234, dividindo por 100 sua Divisão Inteira (//) será 12 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 2 (Divisão inteira será 1)
        # Se num = 1, dividindo por 100 sua Divisão inteira (//) será 0 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 0 (Divisão inteira será 0)
mil = num // 1000 % 10
    # Se num 1234, dividindo por 1000 sua Divisão Inteira (//) será 1 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 1 (Divisão inteira será 0)
        # Se num = 1, dividindo por 100 sua Divisão inteira (//) será 0 e, em seguida, dividindo por 10 o resto desta divisão (%, módulo) será 0 (Divisão inteira será 0)

print('\nO valor inserido foi {}!\n'.format(num)) # mostra valor inserido

print("""Referente ao valor inserido, que corresponde a {num}, segue as operações desejadas:
- A unidade é: {un}
- A dezena é: {dez}
- A centena é: {cen}
- O milhar é: {mil}""".format(
    num = num,
    un = un,
    dez = dez,
    cen = cen,
    mil = mil
    ))