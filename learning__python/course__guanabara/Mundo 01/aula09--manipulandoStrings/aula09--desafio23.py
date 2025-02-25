#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados

# Ex: Digite um número: 1834 = Unidade 4, dezena 3, centena 8, milhar 1. Tente fazer isso como string e matematicamente

# =====   RESOLUÇÃO RONAN   =====

num = str(input('Insira um número entre 0 a 9999: ').strip()) # VER CORREÇÃO 01

print('\nO valor inserido foi {}!\n'.format(num)) # mostra valor inserido

print("""Referente ao valor inserido, que corresponde a {num}, segue as operações desejadas:
- A unidade é: {un}
- A dezena é: {dez}
- A centena é: {cen}
- O milhar é: {mil}""".format(
    num = num,
    un = num[3],
    dez = num[2],
    cen = num[1],
    mil = num[0]
    ))

# =====   OBSERVAÇÃO + RESOLUÇÃO GUANABARA  =====

# Guanabara solicitou para fazer como string E matematicamente. Eu resolvi APENAS como string e em sua resolução chega-se até esse ponto mesmo, com o problema de que se colocar valores com menos do que 4 casas o programa não rodará, pois, para seu funcionamento a string obrigatoriamente deverá ter o comprimento de 4 caracteres.

# Para ser possível resolver este problema sem utilizar método matemático, devemos utilizar estrutura de repetição (o qual não será utilizado neste módulo)

# Para resolver este problema sem utilizar estrutura de repetição, deve-se utilizar do método matemático, o qual abordaremos na resolução aula09--desafio23--matematicamente.py

# ===   DIFERENÇAS   =====

# CORREÇÃO 01: Guanabara configurou o input para receber com número inteiro, não string. Depois do input dado, ele transforma este em string, provavelmente fez isso (pediu input direto em string) para não deixar inserir um decimal (como string).