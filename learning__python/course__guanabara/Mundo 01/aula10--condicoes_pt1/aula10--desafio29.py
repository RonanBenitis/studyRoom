# Escreva um programa que leia a velocidade de um carro.
    # Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
    # A multa vai custar R$7.00 por cada Km acima do limite.

# =====   RESOLUÇÃO RONAN   =====
velocidadeCarro = int(input('Velocidade do carro ao passar no radar (km/h): ')) # CORREÇÃO: Guanabara usou float, disse que km/h é float.
velocidadeRadar = 80 # km/h
valorMulta = 7.00 # por km/h ultrapassado 

if velocidadeCarro > velocidadeRadar:
    print('\nO motorista foi multado por ultrapassar {a} km/h da velocidade máxima ({b} km/h)!\nO total do valor da multa ficou: R${c:.2f}\n'.format(
        a = velocidadeCarro - velocidadeRadar,
        b = velocidadeRadar,
        c = (velocidadeCarro - velocidadeRadar) * valorMulta
        ))
else:
    print('\nO motorista está dentro do limite da velocidade!\n')
    print()

# =====   RESOLUÇÃO GUANABARA   =====

# Minha resolução está proxima da do Guanabara. A diferença está na utilização da condição simples pelo Guanabara, passada a condição, tendo uma mensagem ao usuário fora da estrutura de condição.
    
# Lembrando:
    # Condição simples: Realiza o algoritmo apenas quando a condição for verdadeira, pulando-a se falsa.
    # Condição composta: Realiza algoritmos tanto para quando a condição é verdadeira (algoritmo quando verdade) tanto quando a condição é falsa (algoritmo quando falso).

# COMENTARIOS
    # Refinamento sucessivo: Particionar uma task em mini tarefas, resolvendo-as e testando-as parte a parte. Dividir para conquistar.
    