# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200km e R$0.45 para viagens mais longas.

# =====   RESOLUÇÃO RONAN   =====

dist = float(input('Insira a distância a ser percorrida na viagem desejada (em Km): '))

if dist <= 200:
    valorPorKm = 0.50 # em reais (R$)
else:
    valorPorKm = 0.45 # em reais (R$)

print('O valor da passagem para percorrer {:.2f}km é R${:.2f}'.format(dist, dist * valorPorKm))

print('='*50)
preço = dist * 0.50 if dist <= 200 else dist * 0.45
print('E o preço da sua passagem, utilizando operador ternário, será de R${:.2f}'.format(preço)) # COMENTÁRIO 1
print('='*50)
 
# =====   RESOLUÇÃO GUANABARA   =====

# COMENTÁRIO 1: Guanabara resolveu também com a condição simplificada. Essa estrutura pode ser chamada de IF inline ou operador ternario.