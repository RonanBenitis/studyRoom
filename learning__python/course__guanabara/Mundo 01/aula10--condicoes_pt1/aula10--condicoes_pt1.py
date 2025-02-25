# ===== CONDIÇÕES (DESVIOS) PARTE 1 ======

# === ESTRUTURA SEQUENCIAL ====
    # Estrutura de operação de das instruções em um código, o qual é em forma de sequência no sentido de cima para baixo, esquerda para direita, instrução por instrução, uma atrás da outra (passo a passo).

    # Conjunto de passos = Algoritmo

# === ESTRUTURA DE DESVIO / CONDICIONAL ====
    # Estrutura que roda determinados blocos de instrução, e, as vezes, ignorando outros, a depender de uma condição.
    # Em exemplo grafico, Guanabara ilustrou como um desvio em uma estrada que gera dois caminhos para o mesmo destino
    # Estrutura de condição: se algo é verdadeiro - Roda o fluxo verdadeiro \ senão - roda o fluxo se falso (opcional a segunda parte)

    # ESTRUTURA EM PYTHON
        # if algo:
            # bloco True
        # else:
            # bloco False

        # Só será executado UM DOS BLOCOS, ou executará o bloco True, ou executará o bloco False.

        # Estrutura simples: Usa apenas IF
        # Estrutura composta: Usa IF/ELSE

        # Exemplo:
tempo = int(input('Quantos anos tem seu carro?: '))
if tempo <=3: # Inicio condicional
    print('Carro novo')
else:
    print('Carro velho') # Fim condicional
print('--FIM--')

    # ESTRUTURA SIMPLIFICADA PY
tempo = int(input('Quantos anos tem seu carro?: '))
print('carro novo' if tempo<=3 else 'carro velho') # Estrutura simplificada
print('--FIM--')

# === INDENTAÇÃO ===
    # Indente com TAB. A estrutura do bloco verdadeiro indenta abaixo da instrução IF (para demonstrar que o bloco verdade está dentro do IF). O bloco falso indenta dentro do else.
    # Indentação é de suma importância para demonstrar o que é filho do que, principalmente no Python onde a indentação FAZ PARTE DA SINTAXE.

# === PARTE PRATICA ===

# Estrutura condicional simples
nome = str(input('Qual é o seu nome?: '))
if nome == 'Ronan':
    print('Que nome lindo você tem') # Instrução só ocorrerá se a condição for atendida
print('Bom dia {}'.format(nome))

# Estrutura condicional composta
nome = str(input('Qual é o seu nome?: '))
if nome == 'Ronan':
    print('Que nome lindo você tem')
else:
    print('Seu nome é tão normal!')
print('Bom dia {}'.format(nome))

# Exemplo: notas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >=6.0:
    print('Sua média foi boa, parabéns!')
else:
    print('Sua média foi ruim! Estude mais!')
print('PARABÉNS' if m >= 6.0 else 'ESTUDE MAIS!') # Estrutura simplificada