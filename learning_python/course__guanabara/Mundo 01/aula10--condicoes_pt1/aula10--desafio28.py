# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
    # O programa deverá escrever na tela se o usuário venceu ou perdeu.

# =====   RESOLUÇÃO RONAN   =====
from random import randint
from time import sleep # VER: Alteração 2

n = randint(0, 5) # Computador "pensa" em um número

print('-=-' * 20) # VER: Alteração 1
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!') # VER: Alteração 1
print('-=-' * 20) # VER: Alteração 1

escolha = int(input('Bem vindo(a) ao joguinho de adivinhação! Insira um número entre 0 a 5: ')) # Usuário tenta descobrir

print('Pensando...') # VER: Alteração 2
sleep(3) # VER: Alteração 2

if escolha == n: # Demonstra se o usuário venceu ou perdeu
    print("Boa! Você acertou!")
else:
    print('Vish! Não foi dessa vez. O número que saiu foi {}'.format(n))

# =====   RESOLUÇÃO GUANABARA   =====

# Nossa resolução foi muito próxima a do Guanabara, com os seguintes comentários e alterações.

# COMENTARIO
    #Sobre comentários:
        # É interessante ter costume de comentar seus códigos para faciliar a interpretação. A cada final de linha de código, neste exercicio, Guanabara está inserido um resumo do que a linha faz (bem resumido)
        # Alura diz que comentários são muito bons, mas melhor ainda é seu código também ser semântico para reduzir o máximo comentários desnecessários que podem pesar o arquivo ou poluir o código. É sempre bom ter equilibrio.
    # Auto indentação na condição:
        # O PyCharm e o VSCode auto indentam nas condições ao colocarmos os dois pontos após o IF e o ELSE. Ao escrevermos o IF + a condição e colocarmos dois pontos, ao darmos espaço a linha seguinte já virá indentada; Quando dermos o espaço para escrevermos o else, quando dermos dois pontos em seguida do else a IDE automaticamente o jogará para mesma linha do IF e identará a próxima linha ao darmos espaço.

# ALTERAÇÃO 01
    # Guanabara utilizou este método para estilizar o prompt, onde podemos multiplifcar, com operadores matematicos, strings, replicando-as.
# ALTERAÇÃO 02
    # Guanabara importa a função sleep da biblioteca time para pausar temporariamente o código (botá-lo para dormir por um tempo) para dar a impressão de que o computador está pensando.