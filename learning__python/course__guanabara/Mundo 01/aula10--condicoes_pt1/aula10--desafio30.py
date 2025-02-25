# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR

# =====   RESOLUÇÃO RONAN   =====
n = int(input('Informe um número inteiro: '))

if n % 2 == 0:
    print('O valor inserido é par!')
else:
    print('O valor inserido é impar!')

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara diz que o resto da divisão de um número par por 2 sempre é 0, e em um número impar por 2 sempre é 1.

# A diferença de como o Guanabara fez foi que ele atribuiu a conta do resto da divisão em uma variável, nós fizemos direto na estrutura de condição