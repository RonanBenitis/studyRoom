# Faça um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "A". 2) Em que posição ela aparece a primeira vez 3) Em que posição ela aparece a ultima vez.

# =====   Resolução Ronan   =====

frase = str(input('Insira uma frase: ').strip())

print('A frase inserida foi:\n- {}\n'.format(frase))

print("""Seguem as informações solicitadas:
- A letra "A" (seja maíuscula ou minuscula) aparece {vezes} vezes nesta frase;
- A posição da primeira letra "A" que aparece nesta frase é no indice {prim};
- A posição da ultima letra "A" que aparece nesta frase é no indice {ult}.
""".format(
    vezes = frase.upper().count('A'),
    prim = frase.upper().find('A'),
    ult = frase.upper().rfind('A')
))
    # NOTA:
        # .find encontra a primeira correspondência ao valor inserido;
        # rfind, ou reverse find, encontra a última ocorrência do valor;

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara salienta a importancia de dividir em etapas um problema e, também, sua resolução. Assim, possibilita realizar testes também por etapas para corrigir possiveis bugs de forma mais agil e precisa.

# Guanabara resolveu de forma similar a nós, com as seguintes diferenças:
    # Ele deu upper no input. Não fizemos isso pois nós retornamos ao usuário a frase desejada.
    # Ele fez o find('A')+1, para o valor retornado refletir a posição que nós enxergamos, não o seu indice.
    # Ele usou o rfind, mas disse que é right find (find a direita). Acredito que seja reverse find