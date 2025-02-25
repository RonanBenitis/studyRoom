# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno1 = input('Qual o nome do 1º aluno?: ')
aluno2 = input('Qual o nome do 2º aluno?: ')
aluno3 = input('Qual o nome do 3º aluno?: ')

print('O(a) aluno(a) que irá apagar o quadro será: {}'.format(choice([aluno1, aluno2, aluno3])))

#=== OU, resolvendo em switch case (mais linhas, não usa função direta da biblioteca mas exercita outros caminhos) ===

from random import randint

aluno1 = input('Qual o nome do 1º aluno?: ')
aluno2 = input('Qual o nome do 2º aluno?: ')
aluno3 = input('Qual o nome do 3º aluno²: ')

contAluno = randint(1 , 3)

match contAluno:
    case 1:
        alunoEscolhido = aluno1
    case 2:
        alunoEscolhido = aluno2
    case 3:
        alunoEscolhido = aluno3

print('O(a) aluno(a) que irá apagar o quadro será: {}'.format(alunoEscolhido))

# == Resolução Guanabara ==

# Exercicio corresponde ao exigido pelo Guanabara (na verdade, eram 4 alunos, ma sa lógica tá correta). A diferença é que Guanabara colocou a variável dos alunos dentro de uma variavel em lista, chamada "escolhido". Fizemos algo parecido, mas, ao invés de fazer choice(escolhido), especificamos a lista de alunos dentro do choice: choice([aluno1, aluno2, aluno3]).