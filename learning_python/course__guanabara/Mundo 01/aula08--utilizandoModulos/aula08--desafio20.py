# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

# Precisa retornar: Temos o aluno 1, o 2, o 3 e o 4. Retorna a ordem dos alunos que apresentação: 1º o aluno 1, depois aluno 4, depois aluno [...]

from random import shuffle

alunos = []
x = 1
    # Nota: Havia colocado o x dentro do loop. Não se comprotou como queriamos, pois, ele sempre configurará o x como 1 no inicio do loop. Fazendo-o fora possibilita-se o incremento.

for i in range(4):
    alunos.append(input('Insira o nome do {}º aluno: '.format(x)))
    x += 1 

print('Os alunos cadastrados são estes: {}'.format(alunos))
shuffle(alunos)
    #Shuffle precisou ficar fora do format, pois o format retorna a formatação de um valor. No caso do shuffle, é uma função para reordenar a lista, logo, precisamos da funcionalidade da operação e não de sua formatação. Então, chamamos a função para reordenar a lista de alunos e depois retornamos a mesma variável como format para ser substituido no placeholder ({})
print('A ordem de apresentação será: {}'.format(alunos))

# == Resolução Guanabara ==
# Guanabara resolveu, neste momento, de forma similar ao exercicio anterior em termos de atribuição de variável e lista. Algo que diferencia, também, é que Guanabara trata os dados fora do format para depois retornar o resultado no format de forma pura. Nós, tratamos o dado dentro do format.