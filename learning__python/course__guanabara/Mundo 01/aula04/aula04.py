nomeFixo='Ronan'
idadeFixo=31
pesoFixo=82

#Desafio 1
nomeInput=input('Qual seu nome?: ')
idadeInput=input('Qual sua idade?: ')
pesoInput=input('Qual seu peso?: ')

print('===========================')
print('Olá, mundo!')
print(2+5)
print('2'+'5')
print('Para unir uma string a um número, concatene com vírgula e não com o +, pois o + só concatenará string com string, veja este exemplo colocando a virgula concatenando:',15)
print('===========================')

# Nome fixo
print(nomeFixo,'tem',idadeFixo,'anos e',pesoFixo,'quilos')

# Nome variável (Desafio 1)
print('===========================')
print('Bem vindo',nomeInput,'!')
print(nomeInput,'tem',idadeInput,'anos e',pesoInput,'quilos')
print('===========================')

#Desafio 2
diaNasc=input('Que dia do mÊs você nasceu?: ')
mesNasc=input('Que mês você nasceu? (numeral): ')
anoNasc=input('Que ano você nasceu?: ')

print(nomeInput,'Você nasceu em',diaNasc,'/',mesNasc,'/',anoNasc,'Correto?')
print('===========================')

num1=int(input('Dê o 1º numero da soma: ')) #Feito o int() para transformar o valor de string para interger. Se não tiver o int, ele virá como string.
num2=int(input('Dê o 2º numero da soma: '))
soma=num1+num2

print('A soma de',num1,'com',num2,'é:',soma)
print('===========================')

print('Uma outra forma de chamar uma variável, {}, é dessa maneira que estamos fazendo aqui.'.format(nomeInput))
