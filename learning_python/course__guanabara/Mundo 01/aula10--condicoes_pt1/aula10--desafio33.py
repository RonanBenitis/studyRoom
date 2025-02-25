# Faça um programa que leia três números e mostre qual é o maior e qual é o menor

# =====   RESOLUÇÃO RONAN   =====

n1 = float(input('Insira o 1º número: '))
n2 = float(input('Insira o 2º número: '))
n3 = float(input('Insira o 3º número: '))

maiorNumero = n1

if n2 > maiorNumero:
    maiorNumero = n2
    menorNumero = n1
else:
    menorNumero = n2
if n3 > maiorNumero:
    maiorNumero = n3
if n3 < menorNumero:
    menorNumero = n3

print("""Referente aos números inseridos, segue:
- Maior número: {:.2f}
- Número do meio: {:.2f}
- Menor número: {:.2f}
""".format(maiorNumero, (n1 + n2 + n3) - (maiorNumero + menorNumero), menorNumero))

# SINTO QUE DÁ PRA MELHORAR

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara demonstrou duas formas de resolver diferentes, mas a nossa creio que está correta.

# RES 1 - Condicional simples
# Pode-se também usar:
    # if n1 < n2 and n1 < n3:
        # menor = n1
    # if n2 < n3 and n2 < n1:
        # menor = n2
    # E por aí vai.

# RES 2 - Condicional simples mais concisa
# Verificando quem é menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print("""Referente aos números inseridos, segue:
- Maior número: {:.2f}
- Número do meio: {:.2f}
- Menor número: {:.2f}
""".format(maior, (n1 + n2 + n3) - (maior + menor), menor))